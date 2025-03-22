import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def check_solution(solution_text):
    """Submits a solution to GPT-4 for validation and returns the response."""
    
    prompt = f"""
Evaluate this solution for correctness and completeness:
{solution_text}

Respond with:
✅ Valid Solution - [Brief reason]
❌ Invalid Solution - [Brief reason]
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        return response["choices"][0]["message"]["content"].strip()

    except openai.error.OpenAIError as e:
        return f"❌ API Error: {e}"

if __name__ == "__main__":
    # Minimal Example: Sorting an array
    test_solution = """
    python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
"""

print(check_solution(test_solution))