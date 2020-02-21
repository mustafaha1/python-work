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
        print("You have rolled: '{}', Your attack kills the monster!\n".format(result))
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

    print("The creature steps aside, letting you past.")

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


# Continuation if survival is achieved | Part #2
input11 = str(input("1. Take the shortcut\n2. Take the long way\n"'What will you do? : '))
if input11 == "1":
    short_cut("\nYou have decided to take the shortcut.\n","Suddenly a monster jumps out from behind a tree!\n\n# You will now roll a number from 1-100, if you roll below 20 your chances of survival vanish. Good luck.#") # end of function
if input11 == "2":
    mark_parkt()
    castle()