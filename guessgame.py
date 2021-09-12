# Guess Game, like 2D
import random

win_num = random.randint(1, 100)
guess_limit = 10
guess_count = 0
print('''
  "Welcome to My 2D Game"  
"You have 5 chance to guess."
''')
while guess_count < guess_limit:
    guess = input("CHOOSE A NUMBER: ")
    try:
        guess = int(guess)
        if guess == win_num:
            print('''
"YOU ARE SO LUCKY"
"YOU WIN THE GAME"
            ''')
            break
        elif guess >= 100 or guess <= 0:
            print("PlEASE CHOOSE 1 to 99!")
        else:
            print('"NOT A LUCK"')
            guess_count += 1
    except ValueError:
        print("PLEASE TYPE ONLY NUMBER!")
else:
    print('''
"YOU DON"T HAVE CHANCE ANYMORE"
      "MAY BE NEXT TIME"
    ''')