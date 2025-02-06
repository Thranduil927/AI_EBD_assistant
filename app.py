import streamlit as st
from ebd_ai import (
    generate_research_questions,
    answer_research_question,
    generate_search_keywords,
    recommend_papers
)

# Streamlit Interface
st.set_page_config(page_title="AI-EBD Research Assistant", layout="wide")
st.title("AI-EBD Research Assistant")
st.subheader("Automatically generate research questions, answer them, and recommend papers using the EBD method 📖")

# User input for project topic
project_topic = st.text_input("Enter your research project topic:")

if st.button("Generate Research Questions"):
    with st.spinner("Generating research questions..."):
        research_questions = generate_research_questions(project_topic)
        st.session_state["research_questions"] = research_questions

    st.success("Research questions generated successfully!")
    for i, rq in enumerate(research_questions, 1):
        st.write(f"**{i}. {rq}**")

# Allow user to select a research question
if "research_questions" in st.session_state:
    selected_rq = st.selectbox("Select a research question for AI to answer:", st.session_state["research_questions"])

    if st.button("Generate AI Answer"):
        with st.spinner("AI is thinking..."):
            answer = answer_research_question(selected_rq)
            st.write("### AI Answer:")
            st.write(answer)

# Generate search keywords and recommend papers
if "research_questions" in st.session_state:
    selected_rq = st.selectbox("Select a research question to generate search keywords:", st.session_state["research_questions"])

    if st.button("Generate Search Keywords"):
        with st.spinner("Generating search keywords..."):
            search_keywords = generate_search_keywords(selected_rq)
            st.write("### Recommended Search Keywords:")
            for keyword in search_keywords:
                st.write(f"- {keyword}")

        # Search for related papers
        if st.button("Recommend Related Papers"):
            with st.spinner("Searching for papers..."):
                search_results = recommend_papers(search_keywords)
                st.write("### Recommended Papers:")
                for result in search_results:
                    st.write(f"- [{result['title']}]({result['url']})")
