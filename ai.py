from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API")
)

def request(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant name Delfin Python. Always answer with clear, clean, and short. You have brother named Delfin BOT make from Javascript, your developer/pencipta is Delfin"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

def tes():
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": "tes, say 'DAMN IT, IT'S AI WORKING GOOD'"
            }
        ]
    )
    print(response.choices[0].message.content)
tes()