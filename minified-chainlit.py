import os
from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain, PromptTemplate
import chainlit as cl

# Load the environment variable for the Hugging Face token
load_dotenv()
token = os.getenv('HUGGINGFACE_API_TOKEN')

# Set up the Hugging Face LLM with Falcon-7B
llm = HuggingFaceHub(
    huggingfacehub_api_token=token,
    repo_id="tiiuae/falcon-7b-instruct",
    model_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 200
    }
)

# Define the prompt template for the Chainlit UI
template = """Question: {question}
Answer: Let's think step by step.
"""

# Define the chat start event for Chainlit UI
@cl.on_chat_start
def on_chat_start():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)
    cl.user_session.set("llm_chain", llm_chain)

# Define the message received event for Chainlit UI
@cl.on_message
async def on_message(message: str):
    llm_chain = cl.user_session.get("llm_chain")  # Retrieve the chain from the session
    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])
    
    # The response is sent back to the user
    await cl.Message(content=res["text"]).send()

if __name__ == "__main__":
    # Chainlit does not require an explicit call to start the server, but you can add other initialization logic here if needed
    pass
