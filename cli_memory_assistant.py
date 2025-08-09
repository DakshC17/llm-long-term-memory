import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from memory_storage import add_memory, get_memories, delete_memory
from memory_agent import recall_with_gemini

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def classify_input(user_input):
    """Classify user input as add_memory, ask_question, or delete_memory"""
    prompt = f"""
You are an input classifier for a Long-Term Memory CLI Assistant.

Classify the user's input into one of:
1. "add_memory" → The user wants to store personal/contextual info.
2. "ask_question" → The user is asking something without storing or deleting.
3. "delete_memory" → The user wants to delete memory (keyword or all).

Rules:
- For "add_memory", extract only the clean memory text (no "remember that").
- For "delete_memory", extract keyword or "all".
- For "ask_question", no memory/keyword fields.
- Respond ONLY with a valid JSON object matching:
  {{"intent": "<add_memory|ask_question|delete_memory>", "memory": "<string>", "keyword": "<string>"}}
- Do not include any code fences, markdown, or extra text.

Example:
{{"intent": "add_memory", "memory": "I like pizza"}}

Input: "{user_input}"
"""

    for attempt in range(2):
        response = model.generate_content(prompt)
        raw_text = response.candidates[0].content.parts[0].text.strip()
        print(f"[DEBUG] Raw classification output: {raw_text}")

        # Remove code fences if present
        if raw_text.startswith("```"):
            raw_text = raw_text.strip("`").replace("json", "", 1).strip()

        try:
            parsed = json.loads(raw_text)
            if "intent" in parsed:  # Make sure schema is correct
                return parsed
        except json.JSONDecodeError:
            pass

        # Retry with stricter instruction
        prompt = f"Return ONLY valid JSON in the schema: intent, memory (optional), keyword (optional) for: {user_input}"

    return {"intent": "ask_question"}


def recall_with_gemini(memories, question):
    """Ask Gemini a question using stored memories."""
    if not memories:
        return "I don't remember anything yet."

    prompt = (
        "Here are my memories:\n"
        + "\n".join(f"- {m}" for m in memories)
        + f"\n\nNow answer this question based ONLY on these memories:\n{question}"
    )
    response = model.generate_content(prompt)
    return response.text



print("\n---------------- Welcome to LLM Long-Term Memory CLI Assistant --------------------")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    classification = classify_input(user_input)
    intent = classification.get("intent")

    if intent == "add_memory":
        memory = classification.get("memory", user_input)
        add_memory(memory)
        print(f"💾 Memory saved: \"{memory}\"")

    elif intent == "delete_memory":
        keyword = classification.get("keyword", "")
        if keyword.lower() == "all":
            delete_memory("")  
            print("🗑 All memories deleted!")
        else:
            delete_memory(keyword)
            print(f"🗑 Memories containing '{keyword}' deleted.")

    elif intent == "ask_question":
        memories = get_memories()
        answer = recall_with_gemini(memories, user_input)
        print(f"🤖 {answer}")

    else:
        print("⚠️ Could not classify input. Please try again.")
