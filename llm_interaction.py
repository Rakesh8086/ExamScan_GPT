import time
from pylatexenc.latex2text import LatexNodes2Text
import streamlit as st


def process_image_with_llm(text_prompt, image, model):
    response = model.generate_content([text_prompt, image], stream=True)
    response.resolve()
    string_text = str(response.text)
    return string_text


def provide_images_and_extract_topics_from_llm(images, text_prompt, model):
    topic_names = {}

    # Initialize the counter and start time
    image_counter = 0
    start_time = time.time()

    # Iterate over images and process them
    for image_file, image in images.items():
        # Process the image
        response_text = process_image_with_llm(text_prompt, image, model)
        topic_names[image_file] = response_text

        # Increment the counter
        image_counter += 1

        # Check if 14 images have been processed
        if image_counter >= 12:
            # Calculate elapsed time
            elapsed_time = time.time() - start_time

            # If less than 60 seconds have passed, sleep for the remaining time
            if elapsed_time < 60:
                st.write('Please Wait, your paper is being analysed.')
                time.sleep(60 - elapsed_time)

            # Reset the counter and start time
            image_counter = 0
            start_time = time.time()

    return topic_names


def provide_topic_names_to_llm_to_get_questions(topic_names, generate_question_prompt, model):
    generated_questions = {}
    # Initialize the counter and start time
    response_counter = 0
    start_time = time.time()
    page_number = 1

    for topics in topic_names.values():
        text_prompt_to_llm = f"{topics}\n\n{generate_question_prompt}"
        questions_received = generate_llm_text_response(model, text_prompt_to_llm)
        generated_questions[page_number] = questions_received
        page_number += 1

        response_counter += 1

    # Check if 13 images have been processed
    if response_counter >= 12:
        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # If less than 60 seconds have passed, sleep for the remaining time
        if elapsed_time < 60:
            st.write('Please Wait, the mock test is being generated.')

        # Reset the counter and start time
        response_counter = 0
        start_time = time.time()

    return generated_questions


def generate_llm_text_response(model, prompt):
    response = model.generate_content([prompt], stream=True)
    response.resolve()
    raw_text = response.text
    # Clean up LaTeX formatting by converting it to a readable format
    cleaned_text = latex(raw_text)

    return cleaned_text


def latex(text):
    plain_text = LatexNodes2Text().latex_to_text(text)
    return plain_text
