# Sunbeam Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot developed during a Generative AI internship to answer user queries using information extracted from the Sunbeam website.

## Overview

Sunbeam Chatbot combines semantic search, vector embeddings, and Large Language Models (LLMs) to provide context-aware responses. Instead of relying solely on the language model's internal knowledge, the chatbot retrieves relevant information from a custom knowledge base and uses it as context before generating a response.

The project was developed as a team effort during a Generative AI internship. My contributions included working on retrieval pipelines, embeddings, semantic search, and LLM integration.

---

## Features

* Conversational question answering
* Retrieval-Augmented Generation (RAG)
* Semantic search using vector embeddings
* Context-aware response generation
* Website content extraction and processing
* Streamlit-based user interface
* Integration with Large Language Models

---

## Tech Stack

### Programming Language

* Python

### AI & Machine Learning

* LangChain
* Google Gemini
* Vector Embeddings
* Retrieval-Augmented Generation (RAG)

### Data Storage

* ChromaDB (Vector Database)

### Data Collection

* Selenium

### Frontend

* Streamlit

---

## Project Workflow

1. Extract content from the Sunbeam website.
2. Clean and preprocess the collected data.
3. Generate embeddings for the processed documents.
4. Store embeddings in ChromaDB.
5. Accept user queries through the Streamlit interface.
6. Retrieve relevant documents using semantic similarity search.
7. Provide retrieved context to the LLM.
8. Generate and display a context-aware response.

---

## Project Structure

```text
Sunbeam_Chatbot/
│
├── Core/
│   ├── agent.py
│   └── agent_tools/
│
├── Prepare_Docs/
│
├── Streamlit_UI/
│
├── data/
│
├── Runners/
│
├── chroma_db/
│
├── chat_history.json
│
└── README.md
```

---

## Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Information Retrieval
* Embedding-based Search
* Prompt Engineering
* Vector Databases
* LLM Integration
* Web Automation
* Streamlit Application Development

---

## Learning Outcomes

Through this project, I gained practical experience with:

* Building LLM-powered applications
* Retrieval-Augmented Generation workflows
* Semantic search and embeddings
* Vector databases and document retrieval
* LangChain pipelines
* End-to-end AI application development

---

## Future Improvements

* Multi-document knowledge base support
* Conversation memory optimization
* Evaluation and benchmarking of retrieval quality
* Support for multiple LLM providers
* Enhanced UI and analytics dashboard

```
```
