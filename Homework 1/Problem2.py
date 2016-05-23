'''
Craps, a game of chance
'''
from random import randint
def roll_dice():
    '''
    Returns to random integers in the range of 1-6
    and adds them together.
    '''
    return str(randint(1, 6) + randint(1,6))
       
def play_one_game():
    '''
    Plays one game of python and rolls the die.  If the dice roll lands on a 2,3,12
    on the first roll then this means that they lost.  If they got a 7, or 11. Then
    it means that they won.  If it was something else it becomes the point value.
    Returns a 0 or a 1 depending on if the player won or lost the game.
    '''
    P = roll_dice()
    if P in ("2", "3", "12"):
        print("You rolled " + P + "\nApologies, you have lost. :C ")
        return 0
        exit
    elif P in ("7", "11"):
        print("\nYou rolled " + P + "\nCongrats! You won!! :D")
        return 1
        exit
    else:
        Point = P
        print("\nYou rolled " + str(P))
        print("Your point value is " + P + ". We are now going to roll until you win or lose!")
        k = 'a'
        while k != Point:
            k = roll_dice()
            if k == "7":
                print("You rolled " + k)
                print("You rolled a 7 before your making your point. You lose! Sorry! :C")
                return 0
            elif k == Point:
                print("You rolled " + k)
                print("You rolled the point! You won!")
                return 1
            else:
                continue
        return   
                
def craps():
    '''
    Plays multiple games of craps depending on the if the balance is > 0.
    It returns the balance after winning or loser.
    '''
    print("----------------------------")
    print("Welcome to the Craps program")
    print("----------------------------")
    print("Your initial bank balance is $1000.")

    print("Okay, let's play")
    Balance = 1000
    play_again = 'a'
    while play_again != 'y' or 'n':
        play_again = str(input("Do you want to roll again? [y/n] "))
        wager = int(input("Please enter in a wager >0 and <Balance. $"))
        while wager > Balance or wager <=0:
            wager = int(input("Please enter in a wager >0 and <Balance. $"))

        if Balance <= 0:
            print("\nYou're broke! Sorry better luck next time.")
            break    
        elif play_again == 'n':
            print("Thank you for playing!")
            break
        else:
            if play_one_game() == 0:
                Balance -=wager
                print("Your balance is $"+str(Balance))
            
            elif play_one_game() == 1:
                Balance +=wager
                print("Your balance is $"+str(Balance))
                
        
   
            
        
        
        
        
        
        
                

            
