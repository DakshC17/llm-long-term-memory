

import json
import os

MEMORY_FILE = "memory.json"
#Initialise locsal memory system as a json
def load_memories():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memories(memories):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f, indent=2)
#usimng simple read and write functions of filw handling
def add_memory(memory_text):
    memories = load_memories()
    memories.append(memory_text)
    save_memories(memories)

def get_memories():
    return load_memories()

def delete_memory(keyword):
    memories = load_memories()
    updated = [m for m in memories if keyword not in m]
    save_memories(updated)
