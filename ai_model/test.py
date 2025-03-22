import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

def debug_gpt4():
    """Check GPT-4 raw response."""
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": "Reply ONLY with: ✅ Valid Solution"}],
        temperature=0
    )

    print(f"\n🔍 DEBUG RAW RESPONSE:\n{response}")

# Run debug test
debug_gpt4()