from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)