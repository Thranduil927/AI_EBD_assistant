import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import PromptTemplate
from langchain.tools import DuckDuckGoSearchRun

# Set API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize GPT-4 model
llm = ChatOpenAI(model_name="gpt-4")

# Initialize search tool
search_tool = DuckDuckGoSearchRun()

# Research question generation template
ebd_prompt_template = """
You are an AI assistant proficient in the Environment-Based Design (EBD) method.
Based on the following project topic and the EBD methodology (environment analysis, conflict identification, solution generation),
generate five high-quality research questions (RQs).

### Project Topic:
{project_topic}

### Research Question Format:
1. Environment Analysis: ...
2. Conflict Identification: ...
3. Solution Generation: ...

Please use professional and precise academic language.
"""

# Research question answering template
answer_prompt_template = """
You are an AI research assistant specializing in answering academic research questions.
Based on your knowledge, provide a detailed response to the following research question:

### Research Question:
{research_question}

### Your Answer:
"""

# Keyword generation template for paper search
search_prompt_template = """
You are an AI literature recommendation assistant skilled in generating precise academic search keywords.
Based on the following research question, generate 3-5 high-quality Google Scholar / Semantic Scholar search keywords.

### Research Question:
{research_question}

### Keyword Format:
1. ...
2. ...
3. ...
"""

def generate_research_questions(project_topic):
    """Generate research questions using the EBD method."""
    prompt = PromptTemplate.from_template(ebd_prompt_template)
    messages = [SystemMessage(content=prompt.format(project_topic=project_topic))]
    response = llm(messages)
    return response.content.split("\n")

def answer_research_question(research_question):
    """Provide an AI-generated answer to a research question."""
    prompt = PromptTemplate.from_template(answer_prompt_template)
    messages = [SystemMessage(content=prompt.format(research_question=research_question))]
    response = llm(messages)
    return response.content

def generate_search_keywords(research_question):
    """Generate search keywords for academic literature."""
    prompt = PromptTemplate.from_template(search_prompt_template)
    messages = [SystemMessage(content=prompt.format(research_question=research_question))]
    response = llm(messages)
    return response.content.split("\n")

def recommend_papers(search_keywords):
    """Recommend related research papers based on search keywords."""
    query = " ".join(search_keywords)
    results = search_tool.run(query)
    return results
