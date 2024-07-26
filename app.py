import streamlit as st
from pdf2image import convert_from_path
from convert_pdf_to_images import convert_specific_pages
import tempfile



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

    process_page = st.sidebar.selectbox("Process :", ["Every page", "Every Even-numbered page", "Every odd-numbered "
                                                                                                "page"])

    if number_of_papers == "One":
        uploaded_paper_one = st.file_uploader("Upload your Question Paper 1", type=["pdf"])
        pdf_one = ""
        total_pages = 0
        images_paper_one = []
        if st.button("Analyze Paper"):
            if uploaded_paper_one is not None:
                # Save the uploaded PDF to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                    tmp_file.write(uploaded_paper_one.read())
                    pdf_as_path = tmp_file.name
                    st.write(pdf_as_path)

                try:
                    total_pages = len(convert_from_path(pdf_as_path))
                    st.write(total_pages)

                    images_paper_one = convert_specific_pages(pdf_as_path, process_page, total_pages)

                    '''if process_page == "Every page":
                        images_paper_one = convert_specific_pages(pdf_one, "Every page", total_pages)

                    if process_page == "Every Even-numbered page":
                        images_paper_one = convert_specific_pages(pdf_one, "Every Even-numbered page", total_pages)

                    if process_page == "Every Odd-numbered page":
                        images_paper_one = convert_specific_pages(pdf_one, "Every Odd-numbered page", total_pages)'''

                    temp_image_files = []
                    for idx, image in enumerate(images_paper_one):
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpeg')
                        image.save(temp_file.name, "JPEG")
                        temp_image_files.append(temp_file.name)

                    st.success("Analysis complete!")
                    st.write(temp_image_files)

                except Exception as e:
                    st.error(f"An error occurred while processing the PDF: {e}")

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
