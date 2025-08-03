import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def recall_with_gemini(memories, question):
    """
    Ask Gemini: what do I (the user) remember about X?
    """
    prompt = (
        "Here are my memories:\n"
        + "\n".join(f"- {m}" for m in memories) +
        f"\n\nNow answer this question based on these memories:\n{question}"
    )

    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    memories = ["I use Shram and Magnet as productivity tools"]
    question = "What are the productivity tools that I use?"
    answer = recall_with_gemini(memories, question)
    print("\nAnswer from Gemini:")
    print(answer)
