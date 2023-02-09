print("""
  _____               _        _____                           _     _ 
 |  __ \             | |      |  __ \                         (_)   | |
 | |__) |   _ _______| | ___  | |__) |   _ _ __ __ _ _ __ ___  _  __| |
 |  ___/ | | |_  /_  / |/ _ \ |  ___/ | | | '__/ _` | '_ ` _ \| |/ _` |
 | |   | |_| |/ / / /| |  __/ | |   | |_| | | | (_| | | | | | | | (_| |
 |_|    \__,_/___/___|_|\___| |_|    \__, |_|  \__,_|_| |_| |_|_|\__,_|
                                      __/ |                            
                                     |___/                             
""")

# while input("Ready to enter the Pyramid? Y/N ").upper() == "Y":

playing = input("Do wish to enter the Pyramid? ").lower()

if playing == "no":
    quit()
elif playing != "yes":
    print("invalid")
else:
    print("okay")

















# questions = (
#     "What name was given to the writing system used in Ancient Egypt?",
#     "What was the name of the sun god worshipped in Acient Eygpt?",
#     "Which pharaoh's tomb was discovered in 1922 by Howard Carter?")

# options = (
#     ("A - Hieroglyphics", "B - Cyrillic", "C - Graphemics"),
#     ("A - Anubis", "B - Ra", "C - Osiris"),
#     ("A - Djoser", "B - Cleopatra", "C - Tutankhamun"))

# answers = ("A", "B", "C")
# guesses = []
# question_num = 0

# for question in questions:
#     print("-----------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Pick A, B or C ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1
