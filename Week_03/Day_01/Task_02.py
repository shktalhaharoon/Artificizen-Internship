import os
from dotenv import load_dotenv
from groq import Groq
# Load API Key
load_dotenv()

# Create Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

#
# 
#  Send Prompt
response = client.chat.completions.create(

    model="llama-3.1-8b-instant",

    messages=[
        {
            "role": "user",
            "content": "Summarise what a transformer model does in 3 sentences."
        }
    ]
)

# Print AI Response
print(response.choices[0].message.content)

# Print Token Usage
print("\nPrompt Tokens :", response.usage.prompt_tokens)
print("Completion Tokens :", response.usage.completion_tokens)
print("Total Tokens :", response.usage.total_tokens)