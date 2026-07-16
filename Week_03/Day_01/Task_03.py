import os
from dotenv import load_dotenv
from groq import Groq
# Load API Key
load_dotenv()

# Create Groq 
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Prompt
prompt = "Explain what Artificial Intelligence is in 3 sentences."

# Temperature = 0
print("=" * 60)
print("Responses with Temperature = 0")
print("=" * 60)

for i in range(3):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }])

    print(f"\nResponse {i+1}:\n")
    print(response.choices[0].message.content)



# Temperature = 1
print("\n")
print("=" * 60)
print("Responses with Temperature = 1.0")
print("=" * 60)

for i in range(3):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=1.0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }])

    print(f"\nResponse {i+1}:\n")
    print(response.choices[0].message.content)

    


# Observation
print("\n")
print("Observation:")
print("Temperature 0 gives almost the same response every time, while Temperature 1.0 produces more creative and varied responses.")