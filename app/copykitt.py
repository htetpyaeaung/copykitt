from cmd import PROMPT
import os
from urllib import response
import openai


openai.api_key = os.getenv(
    "OPENAI_API_KEY")

subject = "coffee"
prompt = f"Generate upbeat branding snippet for {subject}"

response = openai.Completion.create(
    engine="davinci", prompt=prompt, max_tokens=36)

print(response)
