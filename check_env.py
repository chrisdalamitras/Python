from dotenv import load_dotenv
import os

load_dotenv(override=True)
key = os.getenv("OPENAI_API_KEY")
print("Το κλειδί φορτώθηκε σωστά:", key is not None and key.startswith("sk-"))