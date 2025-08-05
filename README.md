# LLM Long-Term Memory System 

A simple Python project that provides GPT models with long-term memory capabilities by storing, retrieving, and deleting user-provided facts across conversations.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

##  Overview

This project implements a memory storage & retrieval system that gives LLM models the ability to "remember" facts across conversations using:

- **Python** for core logic
- **JSON file** as local storage
- **Google Gemini API** (gemini-1.5-flash-latest free tier) for intelligent recall

### Example Use Case
```
User: "I use Shram and Magnet as productivity tools"
[Memory stored]

Later in another conversation:
User: "What are the productivity tools that I use?"
Agent: "You use Shram and Magnet"
```

##  Features

The agent provides three core functionalities:

-  **Add memories** - Store new facts and information
-  **Recall memories** - Retrieve information using AI-powered search
-  **Delete memories** - Remove specific memories by keyword

##  How It Works

The system maintains a `memories.json` file where it stores user memories (facts, notes, preferences). The agent can then:

1. **Store** new information as structured memories
2. **Recall** relevant information using Gemini's natural language understanding
3. **Remove** specific memories based on keywords or content

##  Quick Start

### Prerequisites

- Python 3.7+
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DakshC17/llm-long-term-memory.git
   cd llm-long-term-memory
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run the agent**
   ```bash
   python memory_agent.py
   ```

##  Usage Examples

### Step 1: Adding Memories

Store new information in the memory system:

```python
memories = [
    "I use Shram and Magnet as productivity tools",
    "I work as a Machine Learning Engineer at Shram AI"
]
save_memories(memories)
```

**Result:** Memories are saved to `memories.json`

![Add memories](output_images/add1.png)
![Add memories](output_images/add2.png)





### Step 2: Recall with Gemini

Query the agent to retrieve stored information:

```python
question = "What are the productivity tools that I use?"
answer = recall_with_gemini(memories, question)
print(answer)
```

**Output:** "You use Shram and Magnet as productivity tools"

![Recalled with Gemini](output_images/recall1.png)
![Recalled with Gemini](output_images/recall2.png)


### Step 3: Delete Memories

Remove specific memories using keywords:

```python
memories = delete_memory(memories, "Magnet")
save_memories(memories)
```

**Result:** All memories containing "Magnet" are removed

![memory Deletion](output_images/delete1.png)
![memory Deletion](output_images/delete2.png)



##  Project Structure

```
llm-long-term-memory/
├── memory_agent.py      # Main agent script with core functionality
├── memory_storage.py    # Memory management utilities
├── memories.json        # JSON storage for user memories
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── LICENSE             # MIT license
├── output_images/      # Screenshots and demo images
└── __pycache__/        # Python cache files
```

##  Core Components

### `memory_agent.py`
Main script containing the agent logic for adding, recalling, and deleting memories.

### `memory_storage.py`
Utility functions for JSON file operations and memory management.

### `memories.json`
Local storage file that persists memories across sessions.

##  Key Benefits

- **Persistent Memory**: Maintains context across multiple conversation sessions
- **AI-Powered Recall**: Uses Gemini's natural language understanding for intelligent retrieval
- **Simple Architecture**: Easy to understand and extend
- **Local Storage**: No external database required
- **Cost-Effective**: Uses free tier of Gemini API

##  Environment Setup

Create a `.env` file with your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

> **Note:** The `.env` file is not committed to version control for security reasons.


## FURTHER IMPROVEMENTS
1. Removing the json and fitting a vector database something like pinecone..
2. LLM can remeber the things through embeddings and do semantic matching through the embeddings...


## Workflow (Made by me)
---> Tried to make RAG AI Agent earlier. Gave memory to LLM made it conversational Do check out....

![RAG Memory workflow](output_images/Rag_memory_agent.png)

1. Used Supabase for embedding storage
2. Used LLM for Retrieval
3. Used n8n

## Linkedin URL(RAG AGENT)

 --> [RAG Memory AI Agent Workflow](https://www.linkedin.com/posts/daksh-choudhary-18336b249_n8n-rag-automation-activity-7357441527003959297-2RIg?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD10pTMBrpyL0Ptk6GIYChMQGcmFlGdhhBE)


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)

---


