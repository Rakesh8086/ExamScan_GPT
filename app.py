import streamlit as st
import google.generativeai as genai
from support_file import perform_analysis
from support_file import perform_analysis_while_mock_test_generation


llm_model = genai.GenerativeModel('gemini-1.5-flash')


def main():
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Home", "Analyse Question Paper", "Generate Mock Test", "Generate "
                                                                                                          "Mind Map",
                                                  "Analyse Syllabus"])

    if page == "Home":
        show_home()
    elif page == "Analyse Question Paper":
        show_analyse_question_paper()
    elif page == "Generate Mock Test":
        show_generate_mock_test()
    elif page == "Generate Mind Map":
        show_generate_mind_map()
    elif page == "Analyse Syllabus":
        show_analyse_syllabus()


def show_home():
    st.title("ExamScan-GPT")
    st.subheader("A Close Quarter Studios Product")
    st.markdown("<h4 style='color: grey;'>Your One stop solution for Costless Exam Preparation</h2>", unsafe_allow_html=True)
    st.write("\n")
    st.markdown("<h3 style='color: blue;'>Please note that : </h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><h5>The processing time for analysing a question paper is approximately 1 minute for 12 pages, increasing proportionally with the number of pages. </h4></li>
        <li><h5>Generating a mock test can take atleast 1 minute or longer.</h4></li>
    </ul>
    """, unsafe_allow_html=True)


def show_analyse_question_paper():
    st.header("Analyse Question Paper")
    st.subheader("Upload question paper and get in analysed in detail.")

    number_of_papers = st.sidebar.selectbox("Number of Question Papers to be analysed at once : ", ["One", "Two",
                                                                                                    "Three"])

    pages_to_be_processed = st.sidebar.selectbox("Process :",
                                                 ["Every page", "Every Even-numbered page", "Every Odd-numbered "
                                                                                            "page"])

    if number_of_papers == "One":
        uploaded_paper_one = st.file_uploader("Upload your Question Paper 1", type=["pdf"])
        if st.button("Analyze Paper"):
            if uploaded_paper_one is not None:
                analysis_of_question_paper = perform_analysis(uploaded_paper_one, pages_to_be_processed, llm_model)
                st.markdown(analysis_of_question_paper)
                pass
            else:
                st.error("Please upload a PDF file.")

    if number_of_papers == "Two":
        uploaded_paper_one = st.file_uploader("Upload your Question Paper 1", type=["pdf"])
        uploaded_paper_two = st.file_uploader("Upload your Question Paper 2", type=["pdf"])
        if st.button("Analyze Paper"):
            if uploaded_paper_one is not None and uploaded_paper_two is not None:
                pass
            else:
                st.error("Please upload a PDF file.")

    if number_of_papers == "Three":
        uploaded_paper_one = st.file_uploader("Upload your Question Paper 1", type=["pdf"])
        uploaded_paper_two = st.file_uploader("Upload your Question Paper 2", type=["pdf"])
        uploaded_paper_three = st.file_uploader("Upload your Question Paper 3", type=["pdf"])
        if st.button("Analyze Paper"):
            if uploaded_paper_one is not None and uploaded_paper_two is not None and uploaded_paper_three is not None:
                pass
            else:
                st.error("Please upload a PDF file.")


def show_generate_mock_test():
    st.header("Generate Mock Test")
    st.subheader("Upload question paper and get mock test.")
    st.write("Once the questions are generated, Press Cltr+P or click on : and press print option to print the mock "
             "test.")

    pages_to_be_processed = st.sidebar.selectbox("Process :",
                                                 ["Every page", "Every Even-numbered page", "Every Odd-numbered "
                                                                                            "page"])

    question_type = st.sidebar.selectbox("Type of questions to be generated :",
                                                 ["Multiple-choice", "Descriptive"])

    uploaded_model_paper = st.file_uploader(" ", type=["pdf"])
    if st.button("Generate mock test"):
        if uploaded_model_paper is not None:
            generated_questions, total_pages = perform_analysis_while_mock_test_generation(uploaded_model_paper,
                                                                        question_type, pages_to_be_processed, llm_model)
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

        else:
            st.error("Please upload a PDF file.")


def show_generate_mind_map():
    st.header("Generate Mind Map")
    st.subheader("Upload Image or Mention topic name to generate mind map.")


def show_analyse_syllabus():
    st.header("Analyse Syllabus")
    st.subheader("Upload Syllabus and get Suggestions for streamlined preparation.")


if __name__ == "__main__":
    main()
