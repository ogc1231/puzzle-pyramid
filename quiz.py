quiz_questions = (
    "What writing systems did the Ancient Eygptians use? ",
    "Which pharaoh's tomb was discovered in 1922 by Howard Carter? ",
    "The most famous Egyptian pyramids are found at which location? ",
    "Who was the Eygptian God of the Sun? "
)

quiz_options = (
    ("A - Cyrillic", "B - Sanskrit", "C - Hieroglyphs"),
    ("A - Tutankhamun", "B - Cleopatra", "C - Djoser"),
    ("A - Alexandria", "B - Giza", "C - Nile"),
    ("A - Osiris", "B - Isis", "C - Ra"),
)

quiz_answers = ("C", "A", "B", "C", "B")

quiz_guesses = []
quiz_score = 0

question_number = 0

for quiz_question in quiz_questions:
    print("")
    print(quiz_question)
    for quiz_option in quiz_options[question_number]:
        print(quiz_option)
        
    print("")
    quiz_guess = input("Enter 'A', 'B' or 'C' ").upper()
    quiz_guesses.append(quiz_guess)
    if quiz_guess == quiz_answers[question_number]:
        quiz_score += 1
        print("-Correct Answer!-")
    else:
        print("-Incorrect Answer!-")
    
    question_number += 1

