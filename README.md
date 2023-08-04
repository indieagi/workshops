### Indie AGI

Description of your project.

## Getting Started

These instructions will help you get a copy of this project up and running on your local machine for development and testing purposes.

## Prerequisites

You need to have git, python, and pip installed on your local machine. Also, a Hugging Face account is needed to obtain the API token.

## Installation Steps

Fork this repository and create a codespace on GitHub, OR clone it locally using the following command:
```
git clone https://github.com/username/project-name.git
cd project-name
```
Copy sample.env to .env:
```
cp sample.env .env
```
Open the .env file and input your Hugging Face API token:
```
HUGGINGFACEHUB_API_TOKEN=your-huggingfacehub-api-token
```
Install the necessary Python packages:
```
pip install -r requirements.txt
```

## Running the Application

Once you have followed the installation steps, you can start the application with the following command:
streamlit run project_file.py -w
Make sure to replace project_file.py with the actual Python file you wish to run.
