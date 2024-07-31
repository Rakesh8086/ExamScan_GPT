import streamlit as st
import google.generativeai as genai
from support_file import perform_analysis
from support_file import perform_analysis_on_multiple_papers
from support_file import perform_analysis_while_mock_test_generation
from support_file import combine_analysis_of_two_papers_and_prompt
from support_file import to_markdown
from support_file import generate_mind_map_data
from support_file import perform_analysis_in_detail
from support_file import generate_topic_specific_questions
from llm_interaction import generate_llm_text_response
from prompts_to_llm import analysis_of_multiple_papers_prompt
from mind_map_generator import generate_mind_map_from_list
import time

llm_model = genai.GenerativeModel('gemini-1.5-flash')


def main():
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Home", "Analyse Question Paper as Whole", "Page by Page Analysis",
                                                  "Generate Mock Test", "Generate Topic specific Questions",
                                                  "Generate Mind Map"])

    if page == "Home":
        show_home()
    elif page == "Analyse Question Paper as Whole":
        show_analyse_question_paper()
    elif page == "Page by Page Analysis":
        show_page_by_page_analysis()
    elif page == "Generate Mock Test":
        show_generate_mock_test()
    elif page == "Generate Topic specific Questions":
        show_generate_topic_specific_questions()
    elif page == "Generate Mind Map":
        show_generate_mind_map()


def show_home():
    st.title("ExamScan GPT")
    st.subheader("A Close Quarter Studios Product")
    st.markdown("<h4 style='color: grey;'>Your One stop solution for Costless Exam Preparation</h2>",
                unsafe_allow_html=True)
    st.write("\n")
    st.markdown("<h3 style='color: blue;'>Please note that : </h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><h5>The processing time for analysing a question paper is approximately 1 minute for 12 pages, increasing proportionally with the number of pages. </h4></li>
        <li><h5>Generating a mock test can take at least 1 minute or longer.</h4></li>
        <li><h5>ExamScan GPT can make mistakes. Check important info.</h4></li>
    </ul>
    """, unsafe_allow_html=True)


def show_analyse_question_paper():
    st.header("Analyse Question Paper")
    st.subheader("Upload question paper and get in analysed in detail.")

    number_of_papers = st.sidebar.selectbox("Number of Question Papers to be analysed at once : ", ["One", "Two"])

    pages_to_be_processed = st.sidebar.selectbox("Process :",
                                                 ["Every page", "Every Even-numbered page", "Every Odd-numbered "
                                                                                            "page"])

    if number_of_papers == "One":
        uploaded_paper_one = st.file_uploader("Upload your Question Paper 1", type=["pdf"])
        if st.button("Analyze Paper"):
            if uploaded_paper_one is not None:
                try:
                    analysis_of_question_paper = perform_analysis(uploaded_paper_one, pages_to_be_processed, llm_model)
                    st.markdown(analysis_of_question_paper)

                except Exception as e:
                    st.error(f"An unexpected error occurred. Please try again later.")

            else:
                st.error("Please upload a PDF file.")

    if number_of_papers == "Two":
        uploaded_paper_one = st.file_uploader("Upload your Question Paper 1", type=["pdf"])
        uploaded_paper_two = st.file_uploader("Upload your Question Paper 2", type=["pdf"])
        if st.button("Analyze Paper"):
            if uploaded_paper_one is not None and uploaded_paper_two is not None:
                try:
                    analysis_of_question_paper_one = perform_analysis_on_multiple_papers(uploaded_paper_one,
                                                                                         pages_to_be_processed,
                                                                                         llm_model)
                    st.write("Hang Tight!!")
                    time.sleep(20)
                    analysis_of_question_paper_two = perform_analysis_on_multiple_papers(uploaded_paper_two,
                                                                                         pages_to_be_processed,
                                                                                         llm_model)
                    combined_analysis_prompt = analysis_of_multiple_papers_prompt()
                    combined_text = combine_analysis_of_two_papers_and_prompt(analysis_of_question_paper_one,
                                                                              analysis_of_question_paper_two,
                                                                              combined_analysis_prompt)
                    analysis_of_two_question_papers = generate_llm_text_response(llm_model, combined_text)
                    analysis_of_two_question_papers = to_markdown(analysis_of_two_question_papers)
                    st.markdown(analysis_of_two_question_papers)

                except Exception as e:
                    st.error(f"An unexpected error occurred. Please try again later.")

            else:
                st.error("Please upload a PDF file.")


def show_page_by_page_analysis():
    st.header("Page by Page Analysis")
    st.subheader("Upload question paper and get it analysed page by page, question by question.")
    pages_to_be_processed = st.sidebar.selectbox("Process :",
                                                 ["Every page", "Every Even-numbered page", "Every Odd-numbered page"])
    uploaded_paper = st.file_uploader("Upload your Question Paper 1", type=["pdf"])
    if st.button("Analyze Paper"):
        if uploaded_paper is not None:
            try:
                analysis_of_every_question = perform_analysis_in_detail(uploaded_paper, pages_to_be_processed,
                                                                        llm_model)
                # st.write(analysis_of_every_question)
                for image_file, response in analysis_of_every_question.items():
                    st.write(f"Image: {image_file}")
                    st.write(f"Response: {response}\n")

            except Exception as e:
                st.error(f"An unexpected error occurred. Please try again later.")

        else:
            st.error("Please upload a PDF file.")


def show_generate_mock_test():
    st.header("Generate Mock Test")
    st.subheader("Upload question paper and get mock test.")
    st.write("Once the questions are generated, Press CTRL+P or click on : and press print option to print the mock "
             "test.")

    pages_to_be_processed = st.sidebar.selectbox("Process :",
                                                 ["Every page", "Every Even-numbered page", "Every Odd-numbered page"])

    question_type = st.sidebar.selectbox("Type of questions to be generated :", ["Multiple-choice", "Descriptive"])

    uploaded_model_paper = st.file_uploader(" ", type=["pdf"])
    if st.button("Generate mock test"):
        if uploaded_model_paper is not None:
            try:
                generated_questions, total_pages = perform_analysis_while_mock_test_generation(uploaded_model_paper,
                                                                                               question_type,
                                                                                               pages_to_be_processed,
                                                                                               llm_model)
                if total_pages >= 4:
                    introduction_page_skipper = 0
                    for image_file, response in generated_questions.items():
                        introduction_page_skipper += 1
                        if introduction_page_skipper == 1:
                            continue
                        else:
                            st.write(f"Page: {image_file - 1}")
                            st.write(f"Response: {response}\n")

                else:
                    for image_file, response in generated_questions.items():
                        st.write(f"Page: {image_file}")
                        st.write(f"Response: {response}\n")

            except Exception as e:
                st.error(f"An unexpected error occurred. Please try again later.")

        else:
            st.error("Please upload a PDF file.")


def show_generate_topic_specific_questions():
    st.header("Generate Topic specific Questions")
    st.subheader("Mention topic name to generate questions.")
    difficulty_level = st.sidebar.selectbox("Choose Difficulty : ", ["Easy", "Medium", "Hard", "Challenging"])
    question_type = st.sidebar.selectbox("Type of questions to be generated :", ["Multiple-choice", "Descriptive"])
    input_topic = st.text_input(" ")
    if st.button("Generate Questions"):
        if input_topic.strip():
            try:
                generated_questions = generate_topic_specific_questions(input_topic, difficulty_level, question_type,
                                                                        llm_model)
                st.write(generated_questions)

            except Exception as e:
                st.error(f"An unexpected error occurred. Please try again later.")

        else:
            st.error("Please enter a topic name.")


def show_generate_mind_map():
    st.header("Generate Mind Map")
    st.subheader("Mention topic name to generate mind map.")
    mind_map_type = st.sidebar.selectbox("choose type : ", ["Circo", "Dot"])
    input_topic = st.text_input(" ")
    if st.button("Generate Mind Map"):
        if input_topic.strip():
            try:
                mind_map_data_list = generate_mind_map_data(input_topic, llm_model)
                generate_mind_map_from_list(mind_map_data_list, mind_map_type)

            except Exception as e:
                st.error(f"An unexpected error occurred. Please try again later.")

        else:
            st.error("Please enter a topic name.")


if __name__ == "__main__":
    main()
