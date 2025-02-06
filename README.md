AI-EBD Assistant is an intelligent research assistant designed to help researchers generate high-quality research questions based on the Environment-Based Design (EBD) methodology (with link: https://asmedigitalcollection.asme.org/IDETC-CIE/proceedings/IDETC-CIE2011/54860/237/354151). This tool leverages GPT-4 and LangChain to enhance academic research efficiency by:
✅ Generating Research Questions (RQs): Based on user-input project topics, AI-EBD formulates research questions following EBD principles (Environment Analysis, Conflict Identification, Solution Generation).
✅ Providing AI-Powered Answers: The system utilizes GPT-4 to generate insightful responses to the research questions.
✅ Recommending Relevant Research Papers: AI generates precise search keywords and retrieves strongly related academic papers from sources like Google Scholar and Semantic Scholar.

Key Features
🔹 EBD-Driven Research Question Generation – Ensures that research questions align with the EBD methodology.
🔹 AI-Powered Question Answering – Uses GPT-4 to provide detailed responses.
🔹 Automated Keyword Extraction – Enhances literature search efficiency with high-precision search queries.
🔹 Research Paper Recommendation – Uses web search APIs to retrieve strongly relevant academic papers.
🔹 User-Friendly Web Interface – Built with Streamlit for an interactive and intuitive research experience.

Tech Stack
Backend: Python, LangChain, GPT-4, FAISS (Vector Database)
Frontend: Streamlit (Web Interface)
Data Retrieval: DuckDuckGo API, Google Scholar Scraper
Deployment: Docker, Cloud Hosting
Use Cases
🔸 Academic Research: Quickly generate research questions for thesis/dissertation work.
🔸 Project Planning: Use AI-driven insights to refine project objectives.
🔸 Literature Review: Get relevant academic sources in a fraction of the time.

 Please install:
 pip install streamlit openai langchain faiss-cpu chromadb duckduckgo-search


References
1. Zeng Y. Environment-based design (EBD)[C]//International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. 2011, 54860: 237-250.
2. Zeng Y. Environment-based design (EBD): A methodology for transdisciplinary design[J]. Journal of Integrated Design and Process Science, 2015, 19(1): 5-24.
3. Sun X, Zeng Y, Liu W. Formalization of design chain management using environment-based design (EBD) theory[J]. Journal of Intelligent manufacturing, 2013, 24: 597-612.
4. Yang J, Dou Y, Zeng Y. Environment-based design (EBD): Using only necessary knowledge for designer creativity[J]. Proceedings of the Design Society, 2023, 3: 1675-1684.
