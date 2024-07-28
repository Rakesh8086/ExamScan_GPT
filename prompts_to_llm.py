def analyse_page_by_page_prompt():
    text_prompt = (
        "Please perform the following tasks by using the image provided:\n\n"
        "1. Identify the key topics involved in each question and categorize its difficulty into easy, medium, hard."
        "Make sure that you do not give any additional explanation, notes, suggestions, advices etc and give the "
        "answer straight to the point as asked."
    )
    return text_prompt


def combined_analysis_of_every_page_prompt():
    text_prompt = (
        "Please perform the following tasks by using the content provided, knowing that it is a competitive exam:\n\n"
        "1. Identify the list of subjects(like history, mathematics, machine learning) that were asked along with the "
        "most commonly asked topics in each subject."
        "2. From each subject, find out 3 sub-topics that were most asked or has the chances of being asked in the "
        "upcoming exam. The template should be Subject name - sub-topic1, subtopic2, .."
        "3. Identify the topic that contains most number of questions and had more weightage."
        "4. Identify the topic that contains most number of easy questions and the topic with most number of hard "
        "questions"
        "5. Explain 3 topics on where more attention is to be given and 5 potential topics that can be expected that "
        "were not asked."
        "Make sure that you do not consider Examination Instructions, Exam format in analysis and do not give any "
        "additional explanation, answers, notes, suggestions, advices etc and give"
        "the answer straight to the point as asked. Give title as Analysis of Given Paper."
    )
    return text_prompt


def analyse_paper_while_generating_mock_test_prompt():
    text_prompt = (
        "Please perform the following tasks by using the image provided:\n\n"
        "1. Identify the potential adjacent topics involved in each question and categorize its difficulty into easy, "
        "medium, hard, challenging."
        "Make sure that you do not give any additional explanation, notes, suggestions, advices etc and give the "
        "answer straight to the point as asked."
    )

    return text_prompt


def generate_questions_prompt(mock_test_type):
    if mock_test_type == "Multiple-choice":
        text_prompt = (
            "Please perform the following tasks by using the content provided and knowing that it is a competitive "
            "exam:\n\n"
            "1. If the page contains rules, instructions for the exam, display as GOOD LUCK and do not generate "
            "any questions related to it."
            "2. Generate the Multiple choice questions with 4 options from the adjacent topics given here with the "
            "inflated difficulty than the one provided."
            "3. Make sure that the questions can test the in-depth understanding of the student."
            "4. Make sure that questions are not direct but requires understanding of the subject"
            "5. Ensure to properly display questions and not as html tags. use markdown formatting."
            "6. Do not display topic names and difficulty of generated questions."
            "7. Number the questions starting from 1 and increase it by one for the subsequent questions."
            "Make sure that you do not give any additional explanation, answers, notes, suggestions, advices etc and "
            "give the answer straight to the point as asked. Title it is Mock Test"
        )
    elif mock_test_type == "Descriptive":
        text_prompt = (
            "Please perform the following tasks by using the content provided and knowing that it is a competitive "
            "exam:\n\n"
            "1. If the page contains rules, instructions for the exam, display as GOOD LUCK and do not generate "
            "any questions related to it."
            "2. Generate the Descriptive and Numerical questions from the adjacent topics given here with the "
            "inflated difficulty than the one provided."
            "3. Make sure that the questions can test the in-depth understanding of the student."
            "4. Make sure that questions are not direct but requires understanding of the subject"
            "5. Ensure to properly display questions and not as html tags. use markdown formatting."
            "6. Do not display topic names and difficulty of generated questions."
            "7. Number the questions starting from 1 and increase it by one for the subsequent questions."
            "Make sure that you do not give any additional explanation, answers, notes, suggestions, advices etc and "
            "give the answer straight to the point as asked. Title it is Mock Test"
        )

    return text_prompt
