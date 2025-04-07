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