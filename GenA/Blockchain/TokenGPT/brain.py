import openai
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TokenGPT:
    def __init__(self):
        self.initial_text = "My name is Token GPT, and I am here to help you with tokenomics."
        self.gpt_memory = [{"role": "assistant", "content": self.initial_text}]

        # Load API key
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found. Please set it in the .env file.")
        openai.api_key = api_key

    def conversation(self, text):
        system_message = (
            "I am your AI token engineering Assistant. I will help you navigate the complex landscape "
            "of decentralized token-based economies. Please ask your questions."
        )

        messages = [{"role": "system", "content": system_message}] + self.gpt_memory + [{"role": "user", "content": text}]
        self.gpt_memory.append({"role": "user", "content": text})

        # Use an accessible model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Switch to 'gpt-4' only if you have access
            messages=messages
        )

        answer = response['choices'][0]['message']['content']
        self.gpt_memory.append({"role": "assistant", "content": answer})
        return answer
# Example usage
if __name__ == "__main__":
    # Create an instance of TokenGPT
    token_gpt = TokenGPT()

    # Test conversation
    user_query = "Can you fetch the top 5 Uniswap pools?"
    response = token_gpt.conversation(user_query)
    print("Response:", response)
