import gc
import tempfile
from pdf2image import convert_from_path
from convert_pdf_to_images import convert_specific_pages
import streamlit as st
from PIL import Image
import os
import psutil


def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss  # in bytes


def save_images_temporarily(uploaded_question_paper, pages_to_save):
    # Save the uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(uploaded_question_paper.read())
        pdf_as_path = tmp_file.name
        # st.write(pdf_as_path)

    try:
        total_pages = len(convert_from_path(pdf_as_path))

        # st.write(total_pages)

        images_of_paper = convert_specific_pages(pdf_as_path, pages_to_save, total_pages)

        '''if pages_to_save == "Every page":
            images_of_paper = convert_specific_pages(pdf_one, "Every page", total_pages)

        if pages_to_save == "Every Even-numbered page":
            images_of_paper = convert_specific_pages(pdf_one, "Every Even-numbered page", total_pages)

        if pages_to_save == "Every Odd-numbered page":
            images_of_paper = convert_specific_pages(pdf_one, "Every Odd-numbered page", total_pages)'''

        temp_folder_containing_images = tempfile.mkdtemp()
        # st.write(temp_folder_containing_images)  # address of folder containing the images to be processed.

        saved_list_of_temp_images_of_question_paper = []
        for image_number, image in enumerate(images_of_paper):
            # Create a meaningful file name
            temp_file_name = os.path.join(temp_folder_containing_images, f'image_{image_number + 1}.jpeg')
            image.save(temp_file_name, "JPEG")
            saved_list_of_temp_images_of_question_paper.append(temp_file_name)

        # st.success("Analysis complete!")
        # st.write(saved_list_of_temp_images_of_question_paper)
        # if delete=True, page count error pops up

    except Exception as e:
        st.error(f"An error occurred while processing the PDF: {e}")

    finally:
        del images_of_paper
        gc.collect()

    # print(f"Memory usage in temp: {get_memory_usage() / (1024 * 1024)} MB")

    return saved_list_of_temp_images_of_question_paper, temp_folder_containing_images, total_pages


def load_images_from_temporary_folder(folder_path):
    images = {}
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp'))]
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        images[image_file] = image
    return images
