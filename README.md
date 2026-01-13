# Agentic Conversational AI Assistant

An agent-based conversational AI system that understands user intent using transformer models and autonomously selects and executes task-specific tools.
Designed to demonstrate scalable, real-world conversational AI beyond static chatbots.

# Architecture & System Workflow
User Input
   ↓
Web UI (HTML / JavaScript)
   ↓
Flask REST API
   ↓
Intent Classification (Transformer NLP Model)
   ↓
Agent Planner
   ↓
Dynamic Tool Selection
   ↓
Tool Execution
   ↓
Response Formatting
   ↓
User Output

# How the System Works
User sends a natural language query through the web interface.
The backend classifies user intent using a transformer-based zero-shot NLP model.
An agent planner determines the required action.
The system dynamically selects the appropriate tool.
The tool is executed and results are formatted into a conversational response.
The response is returned to the user in real time.

This design enables easy expansion by adding new tools without retraining the model.

# Tech Stack
Backend: Python, Flask, REST APIs
NLP: Hugging Face Transformers (BERT-family, FLAN-T5)
Frontend: HTML, CSS, Vanilla JavaScript
Architecture: Agent-based, tool-oriented design



