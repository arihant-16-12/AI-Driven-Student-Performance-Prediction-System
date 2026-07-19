from google import genai

client = genai.Client(api_key="AIzaSyAIcYwmzjG8GI0lwZMrG7mA_eLVoQ0opFA")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello!"
)

print(response.text)