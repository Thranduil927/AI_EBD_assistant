# ebd_ai.py (Revised for Llama 3 & RAG)
import os
from llama_cpp import Llama
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from dotenv import load_dotenv

# Load API keys and environment variables
load_dotenv()

# Initialize Llama 3 7B model
llm = Llama(model_path="./models/llama-3-7b.Q4_0.gguf", n_ctx=2048)

# Load EBD and TASKS documents for RAG
reader = SimpleDirectoryReader(input_dir="./documents")
documents = reader.load_data()
index = VectorStoreIndex.from_documents(documents)
retriever = index.as_retriever()

# Research question generation using EBD and TASKS insights
def generate_research_questions(project_topic):
    query = f"Generate five research questions using EBD methodology for topic: {project_topic}"
    return llm(query)

# Provide answers with RAG and TASKS framework
def answer_research_question(research_question):
    query = f"Answer the research question using EBD and analyze behavior using TASKS framework: {research_question}"
    return llm(query)

# Generate search keywords for literature review
def generate_search_keywords(research_question):
    query = f"Generate academic search keywords from this research question: {research_question}"
    return llm(query).split("\n")

# Recommend research papers based on keywords
def recommend_papers(search_keywords):
    query = " ".join(search_keywords)
    results = retriever.retrieve(query)
    return [{"title": r.metadata["title"], "url": r.metadata["url"]} for r in results]
