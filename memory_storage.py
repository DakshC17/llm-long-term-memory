

import json
import os

MEMORY_FILE = "memory.json"
def load_memories():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memories(memories):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f, indent=2)
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
