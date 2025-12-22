
import random
def wins():
    computerWin=0
    playerWin=0
    game=0
    def play_game():
        nonlocal playerWin
        nonlocal computerWin
        nonlocal game
        your_input = input("\n\nplease enter a number:\n1 : stone\n2 : paper\n3 : scissors\n\n")

        if your_input.lower() == 'quit' :
            return
        if your_input not in ["1","2","3"]:
            print("enter a valid input")

            return play_game()
        
        your_choice = int(your_input)

        computer_value = random.choice("123")
        computer_choice=int(computer_value)

        
        def decide_winner(player,computer):
            nonlocal playerWin
            nonlocal computerWin
            nonlocal game
            print(f"your choice is   {player}  \ncomputer choice is  {computer}")
           
            if your_choice == 1 and computer_value ==3 :
                playerWin=+1
                return "you win!"
            
            elif your_choice == 2 and computer_value == 3 :
                playerWin=+1
                return"you win!"
            
            elif your_choice == 3 and computer_value == 2 :
                playerWin+=1
                return "you win!"
                
            elif your_choice == computer_value :
                return "tie game"
            else :
                computerWin=+1
                return "computer win!"
                
        last=decide_winner(your_choice,computer_choice)
        print(last)
        game+=1
        print(f"the game count is{game}")
        print(f"your win {playerWin} and computer win {computerWin}")
        return play_game()

    return play_game
play= wins()
play()