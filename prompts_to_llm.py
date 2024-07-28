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


def analysis_of_multiple_papers_prompt():
    text_prompt = (
        "Please perform the following tasks by using the content provided and knowing that it is a competitive exam:\n\n"
        "1. Identify the topics that are common to the given papers."
        "2. Identify the sub-topics that are common to the given papers."
        "3. Identify any trends in the papers if present."
        "4. Identify the 3 topics and its sub-topics that had the most weightage in the given papers."
        "5. Identify 1 topic  that was easy in the given papers and 1 topic that was difficult in the given papers."
        "6. Explain 2 topics and sub-topics on where more attention is to be given based on the given paper."
        "Make sure that you o not include any additional notes, suggestions, advices, notes etc. Also If the given "
        "papers are of different subject and do not have anything in common, Reply as THE GIVEN PAPERS "
        "ARE OF DIFFERENT SUBJECTS AND DO NOT HAVE ANYTHING IN COMMON"
    )

    return text_prompt
