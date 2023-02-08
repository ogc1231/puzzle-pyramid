import os

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

while input("Ready to enter the Pyramid? Y/N ").upper() == "Y":
    os.system("cls")

    print("Level 1")

    questions = (
        "1 - What name was given to the writing system used in Ancient Egypt?",
        "2 - What was the name of the sun god worshipped in Acient Eygpt?",
        "3 - Which pharaoh's tomb was discovered in 1922 by Howard Carter?")

    options = (
        ("A - Hieroglyphics", "B - Cyrillic", "C - Graphemics"),
        ("A - Anubis", "B - Ra", "C - Osiris"),
        ("A - Djoser", "B - Cleopatra", "C - Tutankhamun"))

    question_num = 0

    for question in questions:
        print("-----------")
        print(question)
        for option in options[question_num]:
            print(option)

        question_num += 1