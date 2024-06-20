
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''





import random
def game_win(com,you):
    if(com == you):
        return None
    elif(com == 'r'):
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif com == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif com == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("Welcome to the game!!!\n")
print("You have 5 chance to play this game\n")
u=input(("If you want to stop the game press 't' otherwise press 'r'.\n"))

i=1
mr = 0
cr = 0
sm= 0
while(i<6):   
    if(u == 't'):
        break
    
    print("Player1 Turn: rock(r), paper(p) and scissor(s)?") 
    lis = ["rock","paper","scissor"]
    ranName =random.choice(lis)

    if(ranName == "rock"):
        com = 'r'
    elif(ranName == "paper"):
        com = 'p'
    elif(ranName == "scissor"):
        com = 's'


    you = input("Your Turn: rock(r), paper(p) and scissor(s)? ")

    print(f"Player1 chose::{com}")
    if(com == 'r'):
        print("ROCK::")
        print(rock)
        print("\n")
    elif(com == 'p'):
        print("PAPER::")
        print(paper)
        print("\n")
    elif(com == 's'):
        print("SCISSORS::")
        print(scissor)
        print("\n")

        
    print(f"You chose::{you}")
    if(you == 'r'):
        print("ROCK::")
        print(rock)
        print("\n")
    elif(you == 'p'):
        print("PAPER::")
        print(paper)
        print("\n")
    elif(you == 's'):
        print("SCISSORS::")
        print(scissor)
        print("\n")


    a = game_win(com,you)

    print("_________________________________________")
    if a == None:
        sm=sm+0
        print("The game is tie!\n you got '0' point.")
    elif a:
        sm=sm+1
        mr += 1 
        print("You Win!\n and you got '1' point.")
    else:
        sm=sm-1
        cr +=1
        print("You lose!\n and you got '-1' point.")
    print("_________________________________________")
    
    i+=1


print(f"Total point you got {sm} out of 5." )
if(mr > cr):
    print("Congratulation\t __You Win!__")
elif(mr == cr):
    print("OOOOOhhh\t Game is Tie!!")
else:
    print("OOOHHHHh\t Player1 is win!")
print("_________________________________________")












