import streamlit as st


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

    option = st.sidebar.selectbox("Select number of Question Papers you want to analyse at once", ["One", "Two", "Three"
                                                                                                   ])


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
