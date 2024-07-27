import time


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
        if image_counter >= 13:
            # Calculate elapsed time
            elapsed_time = time.time() - start_time

            # If less than 60 seconds have passed, sleep for the remaining time
            if elapsed_time < 60:
                print('waiting')
                time.sleep(60 - elapsed_time)

            # Reset the counter and start time
            image_counter = 0
            start_time = time.time()

    return topic_names


def generate_llm_text_response(model, prompt):
    response = model.generate_content([prompt], stream=True)
    response.resolve()
    return response.text
