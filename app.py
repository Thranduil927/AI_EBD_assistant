import streamlit as st



from ebd_ai import (
    generate_research_questions,
    answer_research_question,
    generate_search_keywords,
    recommend_papers
)

# Streamlit Interface Configuration
st.set_page_config(page_title="AI-EBD Research Assistant with RAG", layout="wide")
st.title("AI-EBD Research Assistant (Llama 3 + RAG)")
st.subheader("Generate research questions, analyze behavior using TASKS, and recommend papers using RAG-enhanced insights 📖")

# User Input: Project Topic
project_topic = st.text_input("Enter your research project topic:")

if st.button("Generate Research Questions"):
    with st.spinner("Generating research questions with EBD and RAG..."):
        research_questions = generate_research_questions(project_topic)
        st.session_state["research_questions"] = research_questions
    st.success("Research questions generated successfully!")
    for i, rq in enumerate(research_questions.split("\n"), 1):
        st.write(f"**{i}. {rq}**")

# AI Answer Generation with TASKS Analysis
if "research_questions" in st.session_state:
    selected_rq = st.selectbox("Select a research question for AI to answer:", st.session_state["research_questions"].split("\n"))
    if st.button("Generate AI Answer"):
        with st.spinner("AI is analyzing using TASKS framework and RAG..."):
            answer = answer_research_question(selected_rq)
            st.write("### AI Answer:")
            st.write(answer)

# Search Keywords and Paper Recommendations
if "research_questions" in st.session_state:
    selected_rq = st.selectbox("Select a research question for search keywords:", st.session_state["research_questions"].split("\n"))
    if st.button("Generate Search Keywords"):
        with st.spinner("Generating search keywords using RAG..."):
            search_keywords = generate_search_keywords(selected_rq)
            st.write("### Recommended Search Keywords:")
            for keyword in search_keywords:
                st.write(f"- {keyword}")
        if st.button("Recommend Related Papers"):
            with st.spinner("Searching for papers based on RAG insights..."):
                search_results = recommend_papers(search_keywords)
                st.write("### Recommended Papers:")
                for result in search_results:
                    st.write(f"- [{result['title']}]({result['url']})")
