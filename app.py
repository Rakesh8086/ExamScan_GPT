import streamlit as st
from temporary_file_creation import save_images_temporarily
from temporary_file_creation import load_images_from_temporary_folder
from prompts_to_llm import analyse_page_by_page_prompt
from prompts_to_llm import combined_analysis_of_every_page_prompt
import google.generativeai as genai
from llm_interaction import provide_images_and_extract_topics_from_llm
from llm_interaction import generate_llm_text_response
from support_file import combine_responses_and_prompt_as_one
from support_file import to_markdown

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
    st.markdown(
        """
        <style>
        .title {
            position: absolute;
            align: center;
            top: 100px;
            left: 20px;
            font-size: 36px;
            font-weight: bold;
        }
        .header{
            position: absolute;
            align: center;
            top: 170px;
            left: 20px;
            font-size: 30px;
            font-weight: bold;
        }
        .subheader {
            position: absolute;
            align: center;
            top: 240px;
            left: 20px;
            font-size: 24px;
            color: grey;
        }
        .content {
            margin-top: 150px; /* Adjust this to move content down */
        }
        </style>
        <div class="title">ExamScan GPT</div>
        <div class="header">A Close Quarters Studios Product</div>
        <div class="subheader">Your One stop solution for Costless Exam Preparation</div>
        """, unsafe_allow_html=True
    )

    # The rest of the content
    st.markdown('<div class="content">', unsafe_allow_html=True)


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
                path_of_images_of_paper_one, folder_path = save_images_temporarily(uploaded_paper_one,
                                                                                   pages_to_be_processed)
                load_saved_images = load_images_from_temporary_folder(folder_path)
                prompt_for_analysing_paper = analyse_page_by_page_prompt()
                topic_names = provide_images_and_extract_topics_from_llm(load_saved_images, prompt_for_analysing_paper,
                                                                         llm_model)
                prompt_for_analysing_combined_responses = combined_analysis_of_every_page_prompt()
                responses_and_prompt_combined = combine_responses_and_prompt_as_one(topic_names,
                                                                                prompt_for_analysing_combined_responses)
                combined_analysis_for_user = generate_llm_text_response(llm_model, responses_and_prompt_combined)
                analysis_of_question_paper = to_markdown(combined_analysis_for_user)
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


def show_generate_mind_map():
    st.header("Generate Mind Map")
    st.subheader("Upload Image or Mention topic name to generate mind map.")


def show_analyse_syllabus():
    st.header("Analyse Syllabus")
    st.subheader("Upload Syllabus and get Suggestions for streamlined preparation.")


if __name__ == "__main__":
    main()
