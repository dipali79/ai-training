import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

print("Sending request to Gemini...")

response = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents='Explain artificial intelligence in simple terms.'
)

print("\nGemini Response:")
print(response.text)