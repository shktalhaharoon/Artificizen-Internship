import os
from dotenv import load_dotenv
from groq import Groq
# Load API Key
load_dotenv()

# Create Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# System Message
system_message = (
    "You are a strict JSON-only responder. "
    "Never output anything outside a JSON object."
)

# User Question
user_question = "Tell me about Pakistan."

# Call API
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": system_message
        },
        {
            "role": "user",
            "content": user_question
        }],
    temperature=0.7)
# Print Raw Output
print(response.choices[0].message.content)