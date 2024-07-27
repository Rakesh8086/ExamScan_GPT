def analyse_page_by_page_prompt():
    analyse_paper_text_prompt = (
        "Please perform the following tasks by using the image provided:\n\n"
        "1. Identify the key topics involved in each question and categorize its difficulty into easy, medium, hard."
        "Make sure that you do not give any additional explanation, notes, suggestions, advices etc and give the "
        "answer straight to the point as asked."
    )
    return analyse_paper_text_prompt


def combined_analysis_of_every_page_prompt():
    combined_analysis_text_prompt = (
        "Please perform the following tasks by using the content provided, knowing that it is a competitive exam:\n\n"
        "1. Identify the list of subjects that were asked along with the most commonly asked topics in each subject."
        "2. From each subject, find out sub-topics that were most asked or has the chances of being asked in the "
        "upcoming exam."
        "3. The template should be Subject name - sub-topic1, subtopic2, .."
        "4. Explain 5 topics on where more attention is to be given and 5 potential topics that can be expected that "
        "were not asked."
        "Make sure that you do not give any additional explanation, answers, notes, suggestions, advices etc and give "
        "the answer straight to the point as asked."
    )
    return combined_analysis_text_prompt
