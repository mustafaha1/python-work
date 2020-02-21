import time # used for short delay 
from random import randrange # used for random number generator



# Beginning of the game
print('   _____                   _   _                       _                         _ ')
print('  / ____|                 | | | |                     (_)                       | |')
print(' | (___   __ ___   _____  | |_| |__   ___   _ __  _ __ _ _ __   ___ ___  ___ ___| |')
print('  \___ \ / _` \ \ / / _ \ | __|  _ \ / _ \ |  _ \|  __| |  _ \ / __/ _ \/ __/ __| |')
print('  ____) | (_| |\ V /  __/ | |_| | | |  __/ | |_) | |  | | | | | (_|  __/\__ \__ \_|')
print(' |_____/ \__,_| \_/ \___|  \__|_| |_|\___| | .__/|_|  |_|_| |_|\___\___||___/___(_)')
print('                                           | |                                     ')
print('                                           |_|                                     ')
name = input('enter your name: ')
print("\n")
print('{} you are riding through the forest on your horse tasked with locating a princess, rumours are she is trapped in a nearyby castle, you are on your way there right now.'.format(name.capitalize()))
# time.sleep(5)
print("As you keep riding you come upon two paths, '1' is a shortcut which is guaranteed to be dangerous. '2' is the long way which seems to be much safer.\n")


# Matt short part | Part #1
num = randrange(100)
result = num
def short_cut(text, monster): # function for the player chosen shortcut option
    # time.sleep(1)
    print(text)
    # time.sleep(1)
    print(monster)


# Choices and input if statements
    choice1 = str(input("1. Attack\n2. Defend\nWhat will you do? : "))
    if choice1 == "1" and result > 20:
        print("You have rolled: '{}', Your attack kills the monster! The monsters last words were information that the princess is locked upstairs in the castle.".format(result))
        castle()
        # time.sleep(2)
    elif choice1 == "1" and result < 20:
        print("You have rolled: '{}', The monster blocks your attack and kills you in 1 hit.\n".format(result))
        exit("You have died.")
    if choice1 == "2" and result > 20:
        print("You have rolled: '{}', You deflect the monsters powerful attack and manage to run away.\n".format(result))
        castle()
        # time.sleep(2)
    elif choice1 == "2" and result < 20:
        print("You have rolled: '{}', The monster paralyses you with fear. he charges you and kills you with a powerful hit.\n".format(result))
        exit("You have died.")


 # End of Matt's function | Part #1
# time.sleep(1)


# Mark's function | Part #1
def mark_parkt():

    def yes_or_no(question):
        response1 = "A masked creature jumps out from behind a tree and quickly draws a sword."
        reply = str(input(question+' (yes/no): ')).lower().strip()
        if reply == 'yes':
            return True
        elif reply == "no":
            print("Before you can react you hear an arrow being shot from behind a tree.\nYou have died.")
            exit()

    print("You have decided to take the long way.\n")
    # time.sleep(2.5)
    print("you begin your ascent up a large hill, the forest seems to become more dense")
    # time.sleep(3)
    print("before you know it, hours have passed and it is almost dark.")
    # time.sleep(3)
    print("You hear a rustling from some nearby shrubs")
    # time.sleep(3)
    print("...")
    # time.sleep(2)
    yes_or_no("Do you investigate?")

    if yes_or_no == "yes":
        print(response1)
        # time.sleep(2)
    if yes_or_no == "no":
        print()
    response1 = "A masked creature jumps out from behind a tree and quickly draws a sword."
    print(response1)
    print("He tells you he can't let you proceed unless you answer his question correctly.")
    # time.sleep(2)


    # Mark's Quiz | Part #1
    def quiz():
        question1 = str(input("What is the 6th letter of the 'alphabet'?: \nAnswer : "))
        
        if question1 == "b":
            print("You have solved the riddle.\n")
        elif question1 != "b":
            print("The creature raises his sword and strikes you down.. You have failed.. Please try again.")
            exit()
            quiz()
    quiz()

    print("The creature steps aside, letting you past, and he tells you that the princess is locked upstairs inside the castle you are heading to.")

    # time.sleep(2)
    print("You turn around to notice he has disappeared into the night")
    # time.sleep(2)
    print("You press on until you reach an opening in the trees")
    # time.sleep(2)
    print("You spot a castle in the distance and begin to head in its direction\n")


# Matt's trap door function | Part #2
def trapdoor():
    
    sign = "WARNING: DANGER UP AHEAD, CONTINUE AT YOUR OWN RISK!"
    print("\nAs you walk downstairs you see a sign on the wall which reads, {}".format(sign))
    con_tinue = str(input("1. Go back upstairs.\n2. Continue downstairs.\nWhat will you do? : "))
    if con_tinue == "2":
        print("\nAs you walk forward the light gets thinner, you are surrounded by complete darkness with no end in sight. Suddenly you lose your footing. It's all over before you know it, you have fallen to your death.\nYou have died.")
        exit()
    elif con_tinue == "1":
        castle()


import random

def get_guess():
  
  # Set the dashes to the length of the secret word and set the amount of guesses 
  # the user has to 10
  dashes = "-" * len(secret_word)
  guesses_left = 10
  
  # This will loop as long as BOTH conditions are true:
  # 1. The number of guesses of left is greater than -1
  # 2. The dash string does NOT equal the secret word
  while guesses_left > -1 and not dashes == secret_word:
    
    # Print the amount of dashes and guesses left
    print(dashes)
    print (str(guesses_left))
    
    # Ask the user for input
    guess = input("Guess:")
    
    # Conditions that will print out a message according to
    # invalid inputs
    if len(guess) != 1:
      print ("Your guess must have exactly one character!")
      
    # If the guess is in the secret word then we updtae dashes to replace the
    # corresponding dash with the correct index the guess belongs to in the 
    # secret word
    elif guess in secret_word:
      print ("That letter is in the secret word!")
      dashes = update_dashes(secret_word, dashes, guess)
      
    # If the guess is wrong then we display a message and subtract
    # the amount of guesses the user has by 1
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
    
  if guesses_left < 0:
    print ("You lose. The word was: " + str(secret_word))
  
  # If the dash string equals the secret word in the end then the
  # user wins
  else:
    print ("Congrats! You win. The word was: " + str(secret_word))
    
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     # Adds guess to string if guess is correctly
      
    else:
      # Add the dash at index i to result if it doesn't match the guess
      result = result + cur_dash[i]
      
  return result
    
words = ["painting"]

secret_word = random.choice(words)

# Mustafas key | Part #2
def key():
    option1 = str(
        input("You are now upstairs, you must locate a key to open the door to the princesses room that the monster was talking about.\n"))
    if option1 == '1':
        print('You must now play a hangman game, to locate the key the hint is hanging on the wall. If you fail you will die.\n')
        get_guess()
    elif option1 == '2':
        print('hey you desided to quie shamefull ')


# Mustafa's function | Part #2
def castle():
    continued = "You have arrived at the castle and you make your way inside through giant wooden doors that are unguarded, you must now decide which way you want to go.\n1.Go downstairs\n2.Go upstairs"
    print(continued)
    choice1 = str(input("What will you do? : "))
    if choice1 == "1":
        print("You are now heading downstairs")
        trapdoor()
    elif choice1 == "2":
        print("You are now heading Upstairs")
        key()


# Continuation if survival is achieved | Part #2
input11 = str(input("1. Take the shortcut\n2. Take the long way\n"'What will you do? : '))
if input11 == "1":
    short_cut("\nYou have decided to take the shortcut.\n","Suddenly a monster jumps out from behind a tree!\n\n# You will now roll a number from 1-100, if you roll below 20 your chances of survival vanish. Good luck.#") # end of function
if input11 == "2":
    mark_parkt()
    castle()