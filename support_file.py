import textwrap


def combine_responses_and_prompt_as_one(responses_dictionary, prompt):
    combined_response = ""
    for value in responses_dictionary.values():
        combined_response += value
    combined_prompt_with_responses = f"{combined_response}\n\n{prompt}"
    return combined_prompt_with_responses


def to_markdown(text):
    text = text.replace('•', '  * ')
    formatted_text = textwrap.indent(text, '> ', predicate=lambda _: True)
    return formatted_text
