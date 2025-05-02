# Quiz Program Pseudo Code
# 1. Start
# 2. Define function load_questions():
#    a. Try to open 'questions.txt' and read content
#    b. If file not found:
#       - Display "File not found"
#       - Return empty list
#    c. Split content by "--- Question"
#    d. For each block:
#       i.   Parse question text, options a–d, and correct answer
#       ii.  Store in a dictionary
#       iii. Add to list of questions
#    e. Return list of parsed questions
# 3. Define function start_quiz(questions):
#    a. Shuffle the list of questions randomly
#    b. Initialize score = 0
#    c. For each question in the list:
#       i.   Display question and options
#       ii.  Ask user for answer
#       iii. Validate input (must be a/b/c/d)
#       iv.  If answer is correct:
#                - Increment score
#                - Display "Correct!"
#            Else:
#                - Display "Wrong!" and show correct answer
#    d. After all questions, display final score and thank user
# 4. Call load_questions() and store result
# 5. If questions list is not empty:
#    - Call start_quiz(questions)
# 6. End

import random

def load_questions(filename='questions.txt'):
    try:
        with open(filename, 'r') as file:
            file_content = file.read().strip()
            if not file_content:
                print("System: File is empty")
                return []
            
            question_blocks = file_content.split("--- Question")
            question_list = []

            for block in question_blocks:
                if block.strip() == "":
                    continue

                lines = block.strip().split("\n")
                question_data = {}

                for line in lines:
                    if line.startswith('Q'):
                        question_data['question'] = line.split(':', 1)[1].strip()
                    elif line.startswith('A)'):
                        question_data['option_a'] = line[3:].strip()
                    elif line.startswith('B)'):
                        question_data['option_b'] = line[3:].strip()
                    elif line.startswith('C)'):
                        question_data['option_c'] = line[3:].strip()
                    elif line.startswith('D)'):
                        question_data['option_d'] = line[3:].strip()
                    elif line.startswith('ANSWER:'):
                        question_data['correct_answer'] = line.split(':')[1].strip().lower()

                if question_data:
                    question_list.append(question_data)

        return question_list

    except FileNotFoundError:
        print("Quiz file not found")
        return []
    
def start_quiz(question_list):
    print("\n\033[94m--- Welcome to the Quiz Game! ---\033[0m")
    random.shuffle(question_list)
    total_score = 0

    for question_number, question in enumerate(question_list, 1):
        print(f"\nQuestion {question_number}: {question['question']}")
        print(f"a) {question['option_a']}")
        print(f"b) {question['option_b']}")
        print(f"c) {question['option_c']}")
        print(f"d) {question['option_d']}")

        user_answer = input("Your answer (a/b/c/d): ").lower()
        while user_answer not in {'a', 'b', 'c', 'd'}:
            user_answer = input("Please enter a valid option (a/b/c/d): ").lower()

        if user_answer == question['correct_answer']:
            print("\033[92mCorrect!\033[0m")
            total_score += 1
        else:
            correct_key = question['correct_answer']
            correct_text = question.get(f"option_{correct_key}", "Unknown")
            print(f"\033[91mWrong! Correct answer was: {correct_key}) {correct_text}\033[0m")

    print(f"\n\033[96mYour final score is {total_score}/{len(question_list)}.\033[0m")
    print("\033[93mThanks for playing!\033[0m")

# Main execution
questions_from_file = load_questions()
if questions_from_file:
    start_quiz(questions_from_file)
