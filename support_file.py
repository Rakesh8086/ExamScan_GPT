import textwrap
from google.api_core.exceptions import ResourceExhausted
from llm_interaction import provide_images_and_extract_topics_from_llm
from llm_interaction import generate_llm_text_response
from llm_interaction import provide_topic_names_to_llm_to_get_questions
from prompts_to_llm import analyse_page_by_page_prompt
from prompts_to_llm import combined_analysis_of_every_page_prompt
from prompts_to_llm import analyse_paper_while_generating_mock_test_prompt
from prompts_to_llm import generate_questions_prompt
from prompts_to_llm import generate_information_for_mind_map_topic_prompt
from temporary_file_creation import save_images_temporarily
from temporary_file_creation import load_images_from_temporary_folder
import streamlit as st
import time


def combine_responses_and_prompt_as_one(responses_dictionary, prompt):
    combined_response = ""
    for value in responses_dictionary.values():
        combined_response += value
    combined_prompt_with_responses = f"{combined_response}\n\n{prompt}"
    return combined_prompt_with_responses


def combine_analysis_of_two_papers_and_prompt(paper_1, paper_2, prompt):
    combined_prompt_with_two_papers = "Paper_1 " + paper_1 + "\n" + "Paper_2" + paper_2 + "\n" + prompt
    return combined_prompt_with_two_papers


def to_markdown(text):
    text = text.replace('•', '  * ')
    formatted_text = textwrap.indent(text, '> ', predicate=lambda _: True)
    return formatted_text


def perform_analysis(question_paper, pages_to_be_processed, llm_model):
    path_of_images_of_uploaded_paper, folder_path, total_pages = save_images_temporarily(question_paper,
                                                                                         pages_to_be_processed)
    load_saved_images = load_images_from_temporary_folder(folder_path)
    try:
        prompt_for_analysing_paper = analyse_page_by_page_prompt()
        topic_names = provide_images_and_extract_topics_from_llm(load_saved_images, prompt_for_analysing_paper,
                                                                 llm_model)
    except ResourceExhausted as e:
        st.error(f"API Error. Please try again later.")
        return
    except Exception as e:
        st.error(f"Error in extracting topics. Please try again later.")
        return

    try:
        prompt_for_analysing_combined_responses = combined_analysis_of_every_page_prompt()
        responses_and_prompt_combined = combine_responses_and_prompt_as_one(topic_names,
                                                                            prompt_for_analysing_combined_responses)
        combined_analysis_of_single_paper = generate_llm_text_response(llm_model, responses_and_prompt_combined)
    except ResourceExhausted as e:
        st.error(f"API Error. Please try again later.")
        return
    except Exception as e:
        st.error(f"Error in generating combined analysis. Please try again later.")
        return
    analysis_of_question_paper = to_markdown(combined_analysis_of_single_paper)

    return analysis_of_question_paper


def perform_analysis_on_multiple_papers(question_paper, pages_to_be_processed, llm_model):
    path_of_images_of_uploaded_paper, folder_path, total_pages = save_images_temporarily(question_paper,
                                                                                         pages_to_be_processed)
    load_saved_images = load_images_from_temporary_folder(folder_path)
    try:
        prompt_for_analysing_paper = analyse_page_by_page_prompt()
        topic_names = provide_images_and_extract_topics_from_llm(load_saved_images, prompt_for_analysing_paper,
                                                                 llm_model)
    except ResourceExhausted as e:
        st.error(f"API Error.Please try again later.")
        return " "
    except Exception as e:
        st.error(f"Error in extracting topics. Please try again later.")
        return " "

    try:
        prompt_for_analysing_combined_responses = combined_analysis_of_every_page_prompt()
        responses_and_prompt_combined = combine_responses_and_prompt_as_one(topic_names,
                                                                            prompt_for_analysing_combined_responses)
        combined_analysis_of_single_paper = generate_llm_text_response(llm_model, responses_and_prompt_combined)
    except ResourceExhausted as e:
        st.error(f"API Error. Please try again later.")
        return " "
    except Exception as e:
        st.error(f"Error in generating combined analysis. Please try again later.")
        return " "

    return combined_analysis_of_single_paper


def perform_analysis_while_mock_test_generation(question_paper, question_type, pages_to_be_processed, llm_model):
    path_of_images_of_uploaded_paper, folder_path, total_pages = save_images_temporarily(question_paper,
                                                                                         pages_to_be_processed)
    load_saved_images = load_images_from_temporary_folder(folder_path)

    try:
        prompt_for_analysing_paper = analyse_paper_while_generating_mock_test_prompt()
        topic_names = provide_images_and_extract_topics_from_llm(load_saved_images, prompt_for_analysing_paper,
                                                                 llm_model)
    except ResourceExhausted as e:
        st.error(f"API Error. Please try again later.")
        return " "
    except Exception as e:
        st.error(f"Error in extracting topics. Please try again later.")
        return " "

    st.write("mock test would be generated shortly!!")
    time.sleep(20)

    try:
        questions_generate_prompt = generate_questions_prompt(question_type)
        generated_questions = provide_topic_names_to_llm_to_get_questions(topic_names, questions_generate_prompt,
                                                                          llm_model)
    except ResourceExhausted as e:
        st.error(f"API Error. Please try again later.")
        return " "
    except Exception as e:
        st.error(f"Error in generating mock test. Please try again later.")
        return " "

    return generated_questions, total_pages


def generate_mind_map_data(topic, llm_model):
    mind_map_prompt = generate_information_for_mind_map_topic_prompt()
    mind_map_prompt = mind_map_prompt + "\n" + "The topic is : " + topic
    generated_data = generate_llm_text_response(llm_model, mind_map_prompt)

    return generated_data
