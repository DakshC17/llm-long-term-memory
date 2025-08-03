import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

MEMORY_FILE = 'memory_store.json'

def load_memories():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_memories(memories):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memories, f, indent=2)

def add_memory(new_memory):
    memories = load_memories()
    memories.append(new_memory)
    save_memories(memories)

def recall_with_gemini(question):
    memories = load_memories()
    prompt = (
        "Here are my memories:\n"
        + "\n".join(f"- {m}" for m in memories) +
        f"\n\nNow answer this question based on these memories:\n{question}"
    )
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    
    add_memory("I use Shram and Magnet as productivity tools")
    
    
    question = "What are the productivity tools that I use?"
    answer = recall_with_gemini(question)
    print("\nAnswer from Gemini:")
    print(answer)
