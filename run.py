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