import requests
from openai import OpenAI
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_mcqs():
    try:
        prompt = """
        Generate 5 CSIR NET level MCQs from Biochemistry.
        Include answers and short explanations.
        Avoid repetition.
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OpenAI Error:", e)
        return "Error generating MCQs"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

if __name__ == "__main__":
    mcqs = generate_mcqs()
    send_to_telegram(mcqs)