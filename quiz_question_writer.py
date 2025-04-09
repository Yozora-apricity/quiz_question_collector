# Pseudo Code:
# 1. START
# 2. DISPLAY Main Menu with options:
#    a. Create Questions
#    b. Developer Info
#    c. See Questions
#    d. Exit
# 3. IF user selects 'Create Questions' THEN
#    a. OPEN "questions.txt" in append mode
#    b. WHILE True DO
#       i. GET question and options (a, b, c, d)
#       ii. GET correct answer (a-d)
#       iii. SAVE question, options, correct answer, and timestamp TO "questions.txt"
#       iv. ASK "Add another question? (y/n)"
#       v. IF 'n' THEN BREAK
#    c. CLOSE file
#    d. RETURN to Main Menu
# 4. IF user selects 'Developer Info' THEN
#    a. DISPLAY developer info (name, email, GitHub)
#    b. ASK "Go back to main menu? (y/n)"
#    c. IF 'y' THEN RETURN to Main Menu
#    d. IF 'n' THEN EXIT
# 5. IF user selects 'See Questions' THEN
#    a. OPEN "questions.txt"
#    b. IF file is empty THEN DISPLAY "No questions"
#    c. ELSE DISPLAY all questions
#    d. RETURN to Main Menu
# 6. IF user selects 'Exit' THEN EXIT
# 7. IF invalid choice THEN REPEAT Main Menu
# 8. END

from datetime import datetime

def main_menu():
    print("\n\033[32mWelcome to the Main Menu!\033[0m")
    print("1. \033[34m[📝] Create Questions\033[0m")
    print("2. \033[35m[💻] Developer Info\033[0m")
    print("3. \033[33m[📚] See Questions\033[0m")
    print("4. \033[36m[⚙️ ] Manage Questions\033[0m")
    print("5. \033[91m[🚪] Exit Like a Legend\033[0m")
    
    choice = input("\033[97mEnter your choice 1-5: \033[0m")
    if choice == '1':
        create_quiz()
    elif choice == '2':
        developer_info()
    elif choice == '3':
        see_questions()
    elif choice == '4':
        manage_questions()
    elif choice == '5':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def developer_info():
    print("\nDeveloper: \033[96mGerald Tan Rogado\033[0m")
    print("Email: \033[95mgeraldtanrogado@gmail.com\033[0m")
    print("Github Profile: \033[33mhttps://github.com/Yozora-apricity\033[0m")

    while True:
        choice = input("\nWould you like to go back to the main menu? (y/n): ").lower()
        if choice == 'y':
            main_menu()
            break
        elif choice == 'n':
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def get_next_question_number():
    try:
        with open('questions.txt', 'r') as file:
            lines = file.readlines()
            return len([line for line in lines if line.startswith('Q')]) + 1
    except FileNotFoundError:
        return 0

def create_quiz():
    print("\n--- Create Quiz Questions ---")
    with open('questions.txt', 'a') as file:
        while True:
        #Ask for question and options
            question = input("Enter question: ")
            a = input("Enter option a: ")
            b = input("Enter option b: ")
            c = input("Enter option c: ")
            d = input("Enter option d: ")
        
            #Ask for correct answer
            correct = input("Enter the correct answer (a-d): ").lower()
            while correct not in {'a', 'b', 'c', 'd'}:
                print("Invalid answer! Please enter a, b, c, or d.")
                correct = input("Enter the correct answer (a-d): ").lower()
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            question_number = get_next_question_number()
            
            # Write file to make it more readable
            file.write(f'Q{question_number}: {question}\n')
            file.write(f"A) {a}\n")
            file.write(f"B) {b}\n")
            file.write(f"C) {c}\n")
            file.write(f"D) {d}\n")
            file.write(f"ANSWER: {correct}\n")
            file.write(f"--- Added on {timestamp} ---\n\n")
        
             # Check if user wants to continue
            if input("\nAdd another question? (y/n): ").lower() != 'y':
                print("\nQuestions saved to questions.txt")
                break

    main_menu()

def see_questions():
    print("\n--- View Questions ---")
    try:
        with open('questions.txt', 'r') as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("No questions available.")
    except FileNotFoundError:
        print("No questions have been added yet.")
        
    while True:
        choice = input("\nWould you like to go back to the main menu? (y/n): ").lower()
        if choice == 'y':
            main_menu()
            break
        elif choice == 'n':
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def manage_questions():
    print("\n--- Manage Questions ---")
    try:
        with open('questions.txt', 'r') as file:
            content = file.readlines()

        if not content:
            print("No questions available.")
            return
        
        print("\nCurrent Questions:")
        question_num = 1
        for line in content:
            if line.startswith('Q:'):
                print(f"{question_num}. {line.strip()}")
                question_num += 1
                
        print("\nOptions:")
        print("1. Delete all questions")
        print("2. Delete a specific question")
        print("3. Go back to the main menu")

        choice = input("\033[97mEnter your choice (1-3): \033[0m")

        if choice == '1':
            delete_all_questions()
        elif choice == '2':
            delete_specific_question(content)
        elif choice == '3':
            main_menu()
        else:
            print("Invalid choice. Please try again.")
            manage_questions()
    except FileNotFoundError:
        print("No questions have been added yet.")

#Delete all questions
def delete_all_questions():
    confirm = input("Are you sure you want to delete all questions? (y/n): ").lower()
    if confirm == 'y':
        with open('questions.txt', 'w') as file:
            file.truncate(0)
        print("All questions have been deleted.")
    else:
        print("No questions were deleted.")
    main_menu()

#Delete a specific question
def delete_specific_question(content):
    try:
        question_num = int(input("Enter the question number to delete: "))
        question_start = f'Q{question_num}:'
        
        #Find all lines related to the question number
        question_lines = []
        question_block = False
        
        for idx, line in enumerate(content):
            if line.startswith(question_start):
                question_block = True
            if question_block:
                question_lines.append(line)
            if question_block and line.startswith("---"):
                question_block = False
                break
            
        #Check if the question exists
        if not question_lines:
            print(f'Question {question_num} does not exist.')
            return
        
        #Filter out the question block from the content
        filtered_content = [line for line in content if line not in question_lines]
        
        #Save updated content to file
        with open('questions.txt', 'w') as file:
            file.writelines(filtered_content)
            
        print(f"Question {question_num} has been deleted.")
        manage_questions()
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        manage_questions()
        
main_menu()