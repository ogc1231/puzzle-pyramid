# print("""
#   _____               _        _____                           _     _ 
#  |  __ \             | |      |  __ \                         (_)   | |
#  | |__) |   _ _______| | ___  | |__) |   _ _ __ __ _ _ __ ___  _  __| |
#  |  ___/ | | |_  /_  / |/ _ \ |  ___/ | | | '__/ _` | '_ ` _ \| |/ _` |
#  | |   | |_| |/ / / /| |  __/ | |   | |_| | | | (_| | | | | | | | (_| |
#  |_|    \__,_/___/___|_|\___| |_|    \__, |_|  \__,_|_| |_| |_|_|\__,_|
#                                       __/ |                            
#                                      |___/                             
# """)

while True:
    play = input("Do wish to enter the Pyramid? ").upper()
    if play.lower() not in ("yes", "no"):
        print("Invalid: enter 'yes or no' ")
        continue
    elif play == "yes":
        print("let's go")
        break
    else:
        print("Thanks for playing, goodbye! ")
        exit()