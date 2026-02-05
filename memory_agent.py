import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
# need to try the open ai sdk
load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash-latest')

MEMORY_FILE = "memories.json"

def load_memories():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []
# memories get loaded here
def save_memories(memories):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f, indent=2)

def recall_with_gemini(memories, question):
    prompt = (
        "Here are my memories:\n"
        + "\n".join(f"- {m}" for m in memories) +
        f"\n\nNow answer this question based on these memories:\n{question}"
    )
    response = model.generate_content(prompt)
    return response.text

def delete_memory(memories, keyword):
    print(f"\nDeleting memories containing '{keyword}'...")
    new_memories = [m for m in memories if keyword.lower() not in m.lower()]
    return new_memories

if __name__ == "__main__":
    
    memories = [
        "I use Shram and Magnet as productivity tools",
        "I work as a Machine Learning Engineer at Shram AI"
    ]
    print("Initial memories:")
    print(memories)
    save_memories(memories)
    print("Memories saved to JSON.")

    
    question = "What are the productivity tools that I use?"
    answer = recall_with_gemini(memories, question)
    print("\nAnswer from Gemini:")
    print(answer)

    
    memories = delete_memory(memories, "Magnet")
    save_memories(memories)
    print("\nMemories after deletion:")
    print(memories)
