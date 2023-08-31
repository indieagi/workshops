#!/usr/bin/env python
# coding: utf-8

# # Intro To Full Stack LLM Development

# ## Workshop Goals
# Our goal is for you to understand:
# * How and why Iron Python notebooks are used for prototyping
# * Each section of code
# 
# Overall, we hope you will feel enabled to do more advanced tutorials with standard data science tools in the future.
# 
# ## If You Get Stuck
# Just get someone's attention for help.

# ## Task 1: Run A Shell Command
# Lines of code that start with a `%` in an Iron Python notebook execute a `magic command`. In the next cell, the magic command executes a bash command to show you what system you are running on.
# 
# Run the code cell below by selecting it and using one of the following methods:
# * `shift + enter`: run and move to next
# * `ctrl + enter`: run
# * Press the run button in the toolbar above

# In[2]:


get_ipython().run_cell_magic('bash', '', 'lsb_release -a\n')


# ### Other

# In[1]:


get_ipython().run_cell_magic('bash', '', 'lsb_release -a\n')


# ## Task 2: Install Libraries
# ### Context
# Typically when you open a Juypter notebook file for the first time on JupyterHub, you will need to install the third-party libraries you will use to develop your software.
# 
# We are installing the following libraries:
# - `huggingface_hub`: the API we will use to access a hosted version of Falcon LLM
# - `dotenv`: allows you to securely store your Hugging Face token
# - `langchain`: a popular library for making LLMs easier to use
# 
# ### How To
# 1. Option 1: Click the cell and press `shift + enter` to execute and move to next cell
# 2. Option 2: Click the run button in the jupyterhub toolbar above

# In[2]:


get_ipython().run_line_magic('pip', 'install langchain huggingface_hub python-dotenv chainlit')


# ## Task 3: Get Hugging Face Access Token
# ### Context
# To use an API, you typically need to generate a "password" for your code to use to login to your account. This is typically called an "Access Token".
# 
# To store this password securely, it's traditional to use a `.env` file so that the password doesn't accidentally get committed to a Git reposititory. So, we will run a `bash` command below to create this `.env` file.
# 
# ### Instructions
# 1. Create an account at https://huggingface.co
# 2. Go to https://huggingface.co/settings/token
# 3. Click on "New Token" button
# 4. For **Name** put intro-to-full-stack-llm-token. For **Role** put Read.
# 5. Click generate token
# 6. Copy the token to your clipboard
# 7. Paste the token below, replacing `your_hugging_face_token`
# 8. Run the cell

# In[7]:


get_ipython().run_cell_magic('bash', '', 'echo "HUGGINGFACE_API_TOKEN=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" > .env\n\ncat .env\n')


# ## Task 4: Load Hugging Face Token Into Memory

# In[8]:


import os
from dotenv import load_dotenv

load_dotenv()

token=os.getenv('HUGGINGFACE_API_TOKEN')
print(token)


# ## Task 5: Setup Hosted LLM
# ### Context
# The model we will use today is [falcon-7b-instruct](https://huggingface.co/tiiuae/falcon-7b-instruct).
# 
# **Falcon** is what TII of the UAE government named this model, fittingly because they like falcons. For a while, the Falcon model was the highest performing LLM on the [Hugging Face LLM leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard). It has since been surpassed by Facebook's Llama 2 model and others.
# 
# **7b** refers to the number of parameters that the model has. There is a more resource-intensive but powerful model called `falcon-40b` that has 40b parameters.
# 
# **instruct** refers to the fact that the LLM is "instruction fine-tuned," which means that the model has been specially fine-tuned to have the UX of a human assistant. Non-instruction fine-tuned LLMs are much more difficult to use.
# 
# ### Instructions
# Run the code below.
# 
# Read the comments explaining what each line does.

# In[9]:


from langchain import HuggingFaceHub  # Allows us to use LLMs from Hugging Face Hub

# We set up an LLM for use in the next task
llm = HuggingFaceHub(
    huggingfacehub_api_token=token, # Your "password"
    repo_id="tiiuae/falcon-7b-instruct",
    model_kwargs={
        "temperature":0.7, # Adjusts how "random" or "deterministic" the model will output
        "max_new_tokens":200 # Maximum number of tokens the model will output
    }
)

print(llm)


# ## Task 6: Prompt Falcon-7B
# ### Context
# Now you can prompt Falcon-7B from the Python interpreter similar to how you prompt ChatGPT from its GUI interface.
# 
# ### Instructions
# 1. Run the code below
# 2. Understand the comments explaining the code

# In[10]:


# PromptTemplate is a feature of LangChain for defining reusable prompts
#
# LLMChain is called "chain" because LangChain started as a 
# library for "chaining together" multiple successive LLM calls
from langchain import LLMChain, PromptTemplate

template = """
You are a helpful assistant.

{question}
"""

prompt = PromptTemplate(template=template, input_variables= ["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = """
User: Give me step by step instructions to cook pasta
Assistant:
"""

print(llm_chain.run(question))


# ## Task 7: Make Another Prompt
# ### Instructions
# 1. Run the code below
# 2. Modify the code to make any other queries
# 3. Compare the performance against ChatGPT in a separate window

# In[11]:


question = """
You are a helpful assistant.

User: What is the capitol of British Columbia?
"""

completion = llm_chain.run(question)
print(completion)


# ## Task 8: Convert the notebook to a python file
# ### Instructions
# 1. Run the code below in your terminal
# 2. Open the generated .py file

# In[8]:


## Convert notebook to py (add ! to run in cell)

# jupyter nbconvert --to script intro-to-full-stack-llm.ipynb


# ## Task 9: Add Chainlit UI code to py file
# ### Instructions
# 1. Run the code below in your terminal
# 2. Open the generated .py file

# In[17]:


## Adding Chainlit code to .py file

from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

template = """Question: {question}

Answer: Let's think step by step."""


@cl.on_chat_start
def main():
    # Instantiate the chain for that user session
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

    # Store the chain in the user session
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message: str):
    # Retrieve the chain from the user session
    llm_chain = cl.user_session.get("llm_chain")  # type: LLMChain

    # Call the chain asynchronously
    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

    # Do any post processing here

    # "res" is a Dict. For this chain, we get the response by reading the "text" key.
    # This varies from chain to chain, you should check which key to read.
    await cl.Message(content=res["text"]).send()


# ## Task 10: Replace ipynb code with python code
# ### Instructions
# 1. Run the code below in your terminal
# 2. Open the generated .py file

# In[1]:


get_ipython().run_cell_magic('bash', '', "lsb_release -a\n\n## to py\n\nget_ipython().run_cell_magic('bash', '', 'lsb_release -a\\n')\n\n## by hand\n\nimport subprocess\nresult = subprocess.run(['lsb_release', '-a'], capture_output=True, text=True)\nprint(result.stdout)\n")


# In[ ]:


get_ipython().run_line_magic('pip', 'install langchain huggingface_hub python-dotenv chainlit')

## to py

get_ipython().run_line_magic('pip', 'install langchain huggingface_hub python-dotenv chainlit')

## by hand

subprocess.run(['pip', 'install', 'langchain', 'huggingface_hub', 'python-dotenv', 'chainlit'])


# In[ ]:


echo "HUGGINGFACE_API_TOKEN=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" > .env
cat .env

## to py

get_ipython().run_cell_magic('bash', '', 'echo "HUGGINGFACE_API_TOKEN=your_hugging_face_token" > .env\ncat .env\n')

## by hand

with open('.env', 'w') as f:
    f.write("HUGGINGFACE_API_TOKEN=your_hugging_face_token")
with open('.env', 'r') as f:
    print(f.read())

