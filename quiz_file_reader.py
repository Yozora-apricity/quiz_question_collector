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
                print("File is empty")
                return []
            
            question_blocks = file_content.split("--- Question")
            questions = []

            for block in question_blocks:
                if block.strip() == "":
                    continue
                
            lines = block.strip().split("\n")
            question_data = {}