from memory_storage import add_memory, get_memories, delete_memory
from memory_agent import recall_with_gemini
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Now i am trying to make it a cli interface which will make it more interactive for users 
# I can make it streamlit or CLi both best fit will be the one

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("---------------- Welcome to LLM Long-Term Memory CLI Assistant--------------------")
print("---------------- Type your messages below. Type 'exit' to quit.\n-----------------")

##Model will be used 



# """ prompt (testing it for now ---> You are an input classifier. Classify the following user input into one of three categories: ["add_memory", "ask_question", "delete_memory"].
# Also extract a 'keyword' if it helps with deletion, or a clean memory string if adding.

# Return your response as a JSON object with keys:
# - "intent": one of the 3 categories
# - "memory" (optional): string to save if intent is add_memory
# - "keyword" (optional): string keyword to delete if intent is delete_memory)"""


def classify_input(user_input):
    """Use LLM to classify input as memory, question, or deletion"""
    model = genai.GenerativeModel("gemini-1.5-flash-latest")   ##we will change the model for faster replies
                                                                # can also switch to local ollama or transformers model
                                                                
    
    prompt = f"""
You are an intelligent input classifier for a Long-Term Memory CLI Assistant.  
Your task is to carefully read the user's input and classify it into one of the following intent categories:  
1. "add_memory" → The user is providing personal or contextual information to be stored for future reference.  
2. "ask_question" → The user is asking a question or requesting information without intending to store or delete memory.  
3. "delete_memory" → The user wants to remove previously stored memory, either entirely or related to a specific keyword.

Rules & Requirements:
- If intent is "add_memory", extract the exact, clean statement the user wants stored, removing filler words like "remember that" or "my". Store this in the "memory" field.  
- If intent is "delete_memory", extract the relevant keyword or phrase to help identify the memory to delete. Store this in the "keyword" field. If the user requests deleting all memories, return "all" as the keyword.  
- If intent is "ask_question", do not return "memory" or "keyword".  
- Always classify based on the core meaning, even if phrased indirectly or conversationally.  
- Ignore polite phrases, greetings, or irrelevant text when extracting memory or keyword.

Return the result strictly in JSON format with the following structure:
{
  "intent": "<add_memory | ask_question | delete_memory>",
  "memory": "<string>",       // Only if intent is add_memory
  "keyword": "<string>"       // Only if intent is delete_memory
}

Input: "{user_input}"
"""
    


    
    
    
    
    response = model.generate_content(prompt)
    try:
        parsed = eval(response.text)  # Consider using json.loads() if using valid JSON
        return parsed
    except:
        return { "intent": "ask_question" }

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
        print(f"Memory saved: \"{memory}\"")

    elif intent == "delete_memory":
        keyword = classification.get("keyword", "")
        delete_memory(keyword)
        print(f"Memory containing '{keyword}' deleted!")

    elif intent == "ask_question":
        memories = get_memories()
        response = recall_with_gemini(memories, user_input)
        print(f"{response}")
    
    else:
        print("Could not classify input. Please try again.")