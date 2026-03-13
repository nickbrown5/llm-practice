from google import genai

"""If you set your API key as the environment variable GEMINI_API_KEY,
   it will be picked up automatically by the client when using the Gemini
   API libraries. Otherwise you will need to pass your API key as an
   argument when initializing the client."""
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
