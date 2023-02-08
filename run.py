# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Welcome to level ")
questions = (
    "1 - What name was given to the writing system used in Ancient Egypt?",
    "2 - What was the name of the sun god worshipped in Acient Eygpt?",
    "3 - Which pharaoh's tomb was discovered in 1922 by Howard Carter?")

options = (
    ("A - Hieroglyphics", "B - Cyrillic", "C - Graphemics"),
    ("A - Anubis", "B - Ra", "C - Osiris"),
    ("A - Djoser", "B - Cleopatra", "C - Tutankhamun"))

for question in questions:
    print("-----------")
    print(question)