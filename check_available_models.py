import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
)

models = client.models.list()

for m in models.data:
    if m.active and "text" in m.output_modalities:
        print(m.id)