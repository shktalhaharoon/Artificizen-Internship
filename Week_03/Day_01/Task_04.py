import os
from dotenv import load_dotenv
from groq import Groq

# Load API Key
load_dotenv()

# Create Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# Wrapper Function
def ask(
    prompt,
    system=None,
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=512
):

    messages = []

    # Add system message if provided
    if system:
        messages.append(
            {
                "role": "system",
                "content": system
                })

    # Add user prompt
    messages.append(
        {
            "role": "user",
            "content": prompt
        })

    # Call Groq API
    response = client.chat.completions.create(

        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Return only the AI response text
    return response.choices[0].message.content

# Test the Function
answer = ask(
    prompt="What is Machine Learning?"
)
print(answer)