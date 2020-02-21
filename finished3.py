import time # used for short delay 
from random import randrange # used for random number generator
import random # used for hangman 


# Beginning of the game
print("\033[30;47m")
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
time.sleep(3)
print("As you keep riding you come upon two paths, '1' is a shortcut which is guaranteed to be dangerous. '2' is the long way which seems to be much safer.\n")


# Matt short part | Part #1
num = randrange(100)
result = num
def short_cut(text, monster): # function for the player chosen shortcut option
    time.sleep(1)
    print(text)
    time.sleep(2)
    print(monster)

    short_cut_monster = """\
                                |     |
                                \\_V_//
                                \/=|=\/
                                 [=v=]
                               __\___/_____
                              /..[  _____  ]
                             /_  [ [  M /] ]
                            /../.[ [ M /@] ]
                           <-->[_[ [M /@/] ]
                          /../ [.[ [ /@/ ] ]
     _________________]\ /__/  [_[ [/@/ C] ]
    <_________________>>0---]  [=\ \@/ C / /
       ___      ___   ]/000o   /__\ \ C / /
          \    /              /....\ \_/ /
       ....\||/....           [___/=\___/
      .    .  .    .          [...] [...]
     .      ..      .         [___/ \___]
     .    0 .. 0    .         <---> <--->
  /\/\.    .  .    ./\/\      [..]   [..]
 / / / .../|  |\... \ \ \    _[__]   [__]_
/ / /       \/       \ \ \  [____>   <____]
    """
    print(short_cut_monster)

# Choices and input if statements
    choice1 = str(input("1. Attack\n2. Defend\nWhat will you do? : "))
    if choice1 == "1" and result > 20:
        time.sleep(1)
        print("You have rolled: '{}', Your attack kills the monster! The monsters last words were information that 'the princess is locked in a roop upstairs in the castle.'\n".format(result))
        time.sleep(1)
        castle()
        time.sleep(2)
    elif choice1 == "1" and result < 20:
        time.sleep(1)
        print("You have rolled: '{}', The monster blocks your attack and kills you in 1 hit.\n".format(result))
        exit("You have died.")
        death_symbol()
    if choice1 == "2" and result > 20:
        time.sleep(1)
        print("You have rolled: '{}', You deflect the monsters powerful attack and manage to run away.\n".format(result))
        castle()
        time.sleep(2)
    elif choice1 == "2" and result < 20:
        time.sleep()
        print("You have rolled: '{}', The monster paralyses you with fear. he charges you and kills you with a powerful hit.\n".format(result))
        exit("You have died.")


 # End of Matt's function | Part #1
time.sleep(1)


# Mark's function | Part #1
def mark_parkt():

    def yes_or_no(question):
        time.sleep(1)
        response1 = "A masked creature jumps out from behind a tree and quickly draws a sword."
        reply = str(input(question+' (yes/no): ')).lower().strip()
        if reply == 'yes':
            return True
        elif reply == "no":
            print("Before you can react you hear an arrow being shot from behind a tree.\nYou have died.")
            exit()

    print("You have decided to take the long way.\n")
    time.sleep(2)
    print("you begin your ascent up a large hill, the forest seems to become more dense")
    time.sleep(2)
    print("before you know it, hours have passed and it is almost dark.")
    time.sleep(2)
    print("You hear a rustling from some nearby shrubs")
    time.sleep(2)
    print("...")
    time.sleep(2)
    yes_or_no("Do you investigate?")

    if yes_or_no == "yes":
        print(response1)
        time.sleep(2)
    if yes_or_no == "no":
        print()
    response1 = "A masked creature jumps out from behind a tree and quickly draws a sword."
    time.sleep(1)
    creature_str = """
        /       '\'
    __ /   .-.  .'\'      
    /  `\  /   \/  \''
    |  _ \/   .==.==.
    | (   \  /____\__'\'
    \ \      (_()(_()
        \ \            '---._
        \                   \_
    /\ |`       (__)________/
    /  \|     /\___/
    |    \     \||VV
    |     \     \|"",
    |      \     ______
    \       \  /`
            '\'
    """
    print(creature_str)
    print(response1)
    print("He tells you he can't let you proceed unless you answer his question correctly.")
    time.sleep(2)


    # Mark's Quiz | Part #1
    def quiz():
        question1 = str(input("What is the 6th letter of the 'alphabet'?: \nAnswer : "))
        
        if question1 == "b":
            print("You have solved the riddle.\n")
            time.sleep(2)
        elif question1 != "b":
            print("The creature raises his sword and strikes you down.. You have failed.. Please try again.")
            exit()
            quiz()
    quiz()

    print("The creature steps aside, letting you past, and he tells you that the princess you are looking for is 'locked upstairs inside the castle you are heading to'.")
    time.sleep(2)
    print("You turn around to notice he has disappeared into the night")
    time.sleep(2)
    print("You press on until you reach an opening in the trees")
    time.sleep(2)
    print("You spot a castle in the distance and begin to head in its direction\n")


# Matt's trap door function | Part #2
def trapdoor():
    
    sign = "WARNING: DANGER UP AHEAD, CONTINUE AT YOUR OWN RISK!"
    time.sleep(2)
    print("\nAs you walk downstairs you see a sign on the wall which reads, {}".format(sign))
    time.sleep(2)
    con_tinue = str(input("1. Go back upstairs.\n2. Continue downstairs.\nWhat will you do? : "))
    if con_tinue == "2":
        time.sleep(2)
        print("\nAs you walk forward the light gets thinner, you are surrounded by complete darkness with no end in sight. Suddenly you lose your footing. It's all over before you know it, you have fallen to your death.\nYou have died.")
        exit()
    elif con_tinue == "1":
        castle()


# Mustafas end game | Part #1
def find_p(option):
    option = str(input('1. Open the door\n2. Reconsider\nWhat will you do? : '))
    if option == '1':
        print('\nCongratulations! you have freed the princess and beat the game!\nThere is a hores waiting for you and the princess behind the castle.\n')
        time.sleep(1)
        horse_ascii = """
            {)                     /()\              
        c==//\                  c==//\         
   _-~~/-._|_|             _-~~/-._|_|          
  /'_,/,   //'~~~\;;,     /'_,/,   //'~~~\;;,  
  `~  _( _||_..\ | ';;     `~  _( _||_..\ | ';; 
    /'~|/ ~' `\<\>  ;           /'~|/ ~' `\<\>  ;  
    "  |      /  |              "  |      /  |   
       "      "  "                 "      "  " 
        """
        print(horse_ascii)
        print("\nThank you for playing!")
    elif option == '2':
        print('\nWhy would you pick this?.')
        find_p("")


# Hang man | Part #1
def get_guess():
  
  dashes = "-" * len(secret_word)
  guesses_left = 10
  while guesses_left > -1 and not dashes == secret_word:
    print(dashes)
    guess = input("Guess:")
    if len(guess) != 1:
      print ("Your guess must have exactly one character!")
    elif guess in secret_word:
      print ("That letter is in the secret word!")
      dashes = update_dashes(secret_word, dashes, guess)
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
  if guesses_left < 0:
    print ("You lose. The word was: " + str(secret_word))
  else:
    print ("\nYou win. The word was: " + str(secret_word))
    

# Hang man | Part #2
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess # Adds guess to string if guess is correctly
    else:
      result = result + cur_dash[i]
  return result
    
words = ["painting"] # Wordlist for the hangman, probably going to use just 1.

secret_word = random.choice(words)


# Mustafas and Matts key | Part #2
def key():
    time.sleep(2)
    option1 = str(input("You are now upstairs, you see two metals doors that resemble metal bars, through them you can see there is a locked chest and the other room is the princess, she seems passed out and tied up, this must the place that the monster was talking about.\n\n1. Approach the chest\n2. Approach the princess\nWhat will you do? : "))
    if option1 == '1':
        time.sleep(1)
        chest_ascii = """
         __________
        /\____;;___
       | /         /
       `. ())oo() .
        |\(%()*^^()^
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
      """
        print(chest_ascii)
        print('\nYou have approached the left door with the chest, you must now play a hang-man game, to unlock the chest. The hint is hanging on the wall in the form of a  P _ _ _ _ _ _ _.\n')
        get_guess()
        time.sleep(1)
        print("The chest has opened! you claim the key and make your way back.\n\nYou now have the key and you can unlock the door to the princess!")
        time.sleep(1)
        key_ascii = """
     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o___oP'
        """
        print(key_ascii)
        find_p("")
    elif option1 == "2":
        print("\n# There is nothing you can do at the moment.... maybe the room with the chest can help...#\n\n")
        key()


# Mustafa's function | Part #2
def castle():
    time.sleep(2)
    continued = "You have arrived at the castle and you make your way inside through giant wooden doors that are unguarded, you must now decide which way you want to go.\n1.Go downstairs\n2.Go upstairs\n"
    print(continued)
    choice1 = str(input("What will you do? : "))
    if choice1 == "1":
        print("You are now heading downstairs")
        trapdoor()
        time.sleep(1)
    elif choice1 == "2":
        princessascii = """
                 __
                /__`.
               / \ `\\
              /   \  `\'
             /     \   \'
            /_______\  /\'
            (((( ))))
           (((' . ')))
           (((\_-_/)))
           (((_) (_)))
          /((( \ / )))\'
         / (((  ^  ))) \'
        / / ((  ^  )) \ \'
       ( (   \  ^  /   ) )
        \ \   )www(   / /
         `\\ /     \ //'
           /'       `\'
          /           \'
         /             \'
         """
        print(princessascii)
        time.sleep(2)
        key()

# Continuation if survival is achieved | Part #2
input11 = str(input("1. Take the shortcut\n2. Take the long way\n"'What will you do? : '))
if input11 == "1":
    time.sleep(2)
    short_cut("\nYou have decided to take the shortcut.\n","Suddenly a monster jumps out from behind a tree!\n\n# You will now roll a number from 1-100, if you roll below 20 your chances of survival vanish. Good luck.# ") # end of function
if input11 == "2":
    time.sleep(2)
    mark_parkt()
    castle()