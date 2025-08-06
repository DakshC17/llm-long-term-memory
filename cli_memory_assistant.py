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



""" prompt (testing it for now ---> You are an input classifier. Classify the following user input into one of three categories: ["add_memory", "ask_question", "delete_memory"].
Also extract a 'keyword' if it helps with deletion, or a clean memory string if adding.

Return your response as a JSON object with keys:
- "intent": one of the 3 categories
- "memory" (optional): string to save if intent is add_memory
- "keyword" (optional): string keyword to delete if intent is delete_memory)"""


def classify_input(user_input):
    """Use LLM to classify input as memory, question, or deletion"""
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    
    prompt = f"""
You are an input classifier. Classify the following user input into one of three categories: ["add_memory", "ask_question", "delete_memory"].
Also extract a 'keyword' if it helps with deletion, or a clean memory string if adding.

Return your response as a JSON object with keys:
- "intent": one of the 3 categories
- "memory" (optional): string to save if intent is add_memory
- "keyword" (optional): string keyword to delete if intent is delete_memory

Input: "{user_input}"
"""