import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)  # Loads `.env` file

def main():

    # get API key from environment variable or replace with your OpenRouter API key
    API_KEY = os.getenv("OPENROUTER_API_KEY", "")

    if not API_KEY:
        raise ValueError("Please set the OPENROUTER_API_KEY environment variable or replace it in the code.")

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
    )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="deepseek/deepseek-chat-v3-0324:free",
    messages=[
        {
        "role": "user",
        "content": "What is the meaning of life?"
        }
    ]
    )
    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
