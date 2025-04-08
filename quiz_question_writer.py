#Pseudo code:
#1. START
#2. OPEN "questions.txt" IN APPEND MODE
#3. WHILE True DO
#   a. PROMPT "Enter question:" STORE TO question
#   b. PROMPT "Enter option a:" STORE TO a
#   c. PROMPT "Enter option b:" STORE TO b
#   d. PROMPT "Enter option c:" STORE TO c
#   e. PROMPT "Enter option d:" STORE TO d
#   f. WHILE True DO
#       i. PROMPT "Enter correct answer (a-d):" STORE TO correct
#       ii. IF correct NOT IN ['a','b','c','d'] THEN
#           - PRINT "Invalid answer"
#         ELSE
#           - BREAK
#   g. WRITE question|a|b|c|d|correct TO FILE
#   h. PROMPT "Add another? (y/n)" STORE TO choice
#   i. IF choice != 'y' THEN BREAK
#4. CLOSE FILE
#5. END

from datetime import datetime

def main_menu():
    print("\n\033[32mWelcome to the Main Menu!\033[0m")
    print("1. \033[34mCreate Questions\033[0m")
    print("2. \033[35mDeveloper Info\033[0m")
    print("3. \033[33mSee Questions\033[0m")
    print("4. \033[91mExit\033[0m")
    
    choice = input("\033[97mEnter your choice 1-4: \033[0m")
    if choice == '1':
        create_quiz()
    elif choice == '2':
        developer_info()
    elif choice == '3':
        print("Feature under development.")
        main_menu()
    elif choice == '4':
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
            
            # Write file to make it more readable
            file.write(f"Q: {question}\n")
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

main_menu()