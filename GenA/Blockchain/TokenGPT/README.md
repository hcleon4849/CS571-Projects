# TokenGPT
An AI-powered chatbot called TokenGPT was created to help with token engineering. It provides thorough insights and analysis for decentralized economies by utilizing the ChatGPT API, Retrieval-Augmented Generation (RAG), and function calling capabilities.

# Setup Instructions
## Step 1: Clone the Repository
First, clone the repository to your local machine:


## Step2: Create a Virtual Environment
Create a virtual environment to manage dependencies:
```
python -m venv tgpt_venv
```
## Step 3: Activate the Virtual Environment
Activate the virtual environment:

On Windows:
```
    tgpt_venv\Scripts\activate
```
## Step 4: Install Dependencies
Install the required dependencies using pip
Install Dependencies Individually:
```
pip install openai
pip install dune-client
pip install flask
pip install requests
```
## Generate a requirements.txt File:
Once all dependencies are installed, you can generate a ``` requirements.txt ``` file from your virtual environment:
```
pip freeze > requirements.txt
```
Set Up Environment Variables
TokenGPT requires an OpenAI API key, a base path for saving files, and a Dune API key to function. You need to provide your own API keys and base path.

Create a .env file in the root directory of the project. Add the following environment variables to the .env file:
```
$env:OPENAI_API_KEY = "your_openai_api_key_here"
$env:BASE_PATH = "your_base_path_here"
$env:DUNE_API_KEY = "your_dune_api_key_here"
```

## Step 5: Run the Chatbot
Create the ``` chatbot.py ``` script to start the TokenGPT application:
```
python chatbot.py
```
Create the ``` brain.py ``` script interprets user queries and, if needed, delegates specific tasks to ``` uniswap.py ```
Create the ``` uniswap.py ``` script calls to get real-time data about tokens

