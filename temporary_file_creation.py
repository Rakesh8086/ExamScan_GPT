import tempfile
from pdf2image import convert_from_path
from convert_pdf_to_images import convert_specific_pages
import streamlit as st


def save_images_temporarily(uploaded_question_paper, pages_to_save):
    # Save the uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(uploaded_question_paper.read())
        pdf_as_path = tmp_file.name
        st.write(pdf_as_path)

    try:
        total_pages = len(convert_from_path(pdf_as_path))
        st.write(total_pages)

        images_of_paper = convert_specific_pages(pdf_as_path, pages_to_save, total_pages)

        '''if pages_to_save == "Every page":
            images_of_paper = convert_specific_pages(pdf_one, "Every page", total_pages)

        if pages_to_save == "Every Even-numbered page":
            images_of_paper = convert_specific_pages(pdf_one, "Every Even-numbered page", total_pages)

        if pages_to_save == "Every Odd-numbered page":
            images_of_paper = convert_specific_pages(pdf_one, "Every Odd-numbered page", total_pages)'''

        temp_image_files_paper_one = []
        for idx, image in enumerate(images_of_paper):
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpeg')
            image.save(temp_file.name, "JPEG")
            temp_image_files_paper_one.append(temp_file.name)

        # st.success("Analysis complete!")
        # st.write(temp_image_files_paper_one)
        # if delete=True, page count error pops up

    except Exception as e:
        st.error(f"An error occurred while processing the PDF: {e}")
        
    return images_of_paper
