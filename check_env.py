from dotenv import load_dotenv
import os

load_dotenv(override=True)
key = os.getenv("GROQ_API_KEY")
print("Το κλειδί φορτώθηκε σωστά:", key is not None and key.startswith("gsk-"))