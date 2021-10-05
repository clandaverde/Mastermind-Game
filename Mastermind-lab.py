# Christian Landaverde
# Mastermind Lab
# 04/01/2020


import random


# assigns a specific number to an abbreviated letter of the specific color
def converts_number_to_color(i_number):
    s_color = ""
    if i_number == 1:
        s_color = "B"
    elif i_number == 2:
        s_color = "G"
    elif i_number == 3:
        s_color = "K"
    elif i_number == 4:
        s_color = "P"
    elif i_number == 5:
        s_color = "R"
    elif i_number == 6:
        s_color = "Y"

        
    return s_color



# Creates a random code for the user to figure out 
def create_game_code():
    i_random1 = random.randint(1,6)
    i_random2 = random.randint(1,6)
    i_random3 = random.randint(1,6)
    i_random4 = random.randint(1,6)


    s_code = ""
    s_code = s_code + converts_number_to_color(i_random1)
    s_code = s_code + converts_number_to_color(i_random2)
    s_code = s_code + converts_number_to_color(i_random3)
    s_code = s_code + converts_number_to_color(i_random4)

    return s_code

s_comp_code = create_game_code()
# print("The computers code: ", s_comp_code)



# Displays title
print("Welcome to Mastermind")



# Displays the instructions for the user
def display_instruction(s_instructions):
    if s_instructions == "Ready" or "ready":
        print("The objective of the game is to guess the pegs (color and order) that the computer picks.")
        print("You will be given 8 attempts to do so.")
        print("The 6 colors of the code pegs are blue, green, pink, purple, red & yellow")
        print("There are two additional pegs, a black and a white one.")
        print("A black peg indicates that the user has a code peg that is the CORRECT COLOR and in the CORRECT ORDER.")
        print("A white peg indicates that the user has a code peg that is the CORRECT COLOR but in the INCORRECT POSITION.")
        print("Enter the the first letter (IN ALL CAPS) of the 4 colors you pick i.e purple, blue, yellow and red.")
        print("Would be displayed as: 'PBYR'")
        print("KEEP IN MIND THAT TO INPUT PINK IT'S: 'K'")
        
    return ""

s_instructions = input("Type 'ready' to display the directions: ")
i_call_instructions = display_instruction(s_instructions)
print(i_call_instructions)



# Gets the players guess  
def players_guess(s_begin):
    
    
    if s_begin == "yes" or "Yes":
        s_players_guess = input("Enter a guess: ")

    

    return s_players_guess

s_begin = input("Ready? Type 'yes' to begin: ")
s_players_guess = players_guess(s_begin)
print(s_players_guess)



# calculates black pegs
def calculate_black_pegs(s_comp_code, s_players_guess):
    
    i_num_of_black_pegs = 0
    if s_comp_code[0] == s_players_guess[0]:
        i_num_of_black_pegs = i_num_of_black_pegs + 1
    if s_comp_code[1] == s_players_guess[1]:
        i_num_of_black_pegs = i_num_of_black_pegs + 1
    if s_comp_code[2] == s_players_guess[2]:
        i_num_of_black_pegs = i_num_of_black_pegs + 1
    if s_comp_code[3] == s_players_guess[3]:
        i_num_of_black_pegs = i_num_of_black_pegs + 1

    
    print("Black pegs: ", i_num_of_black_pegs)

    return i_num_of_black_pegs


i_total_black_pegs = calculate_black_pegs(s_comp_code, s_players_guess)



# Calculates the number of white pegs (might make into two seperate functions later on)
def calculate_white_pegs(s_comp_code, s_players_guess, i_total_black_pegs):
    
    i_num_of_white_pegs = 0

    i_actual_blue = 0
    i_actual_green = 0
    i_actual_pink = 0
    i_actual_purple = 0
    i_actual_red = 0
    i_actual_yellow = 0
    


    i_guessed_blue = 0
    i_guessed_green = 0
    i_guessed_pink = 0
    i_guessed_purple = 0
    i_guessed_red = 0
    i_guessed_yellow = 0


    for i in range(4):
        
        if s_comp_code[i] == "B":
            i_actual_blue = i_actual_blue + 1
            
        elif s_comp_code[i] == "G":
            i_actual_green = i_actual_green + 1
            
        elif s_comp_code[i] == "K":
            i_actual_pink = i_actual_pink + 1
            
        elif s_comp_code[i] == "P":
            i_actual_purple = i_actual_purple + 1
            
        elif s_comp_code[i] == "R":
            i_actual_red = i_actual_red + 1
            
        elif s_comp_code[i] == "Y":
            i_actual_yellow = i_actual_yellow + 1
            

    for i in range(4):
        
        if s_players_guess[i] == "B":
            i_guessed_blue = i_guessed_blue + 1
            
        elif s_players_guess[i] == "G":
            i_guessed_green = i_guessed_green + 1
            
        elif s_players_guess[i] == "K":
            i_guessed_pink = i_guessed_pink + 1
            
        elif s_players_guess[i] == "P":
            i_guessed_purple = i_guessed_purple + 1
            
        elif s_players_guess[i] == "R":
            i_guessed_red = i_guessed_red + 1
            
        elif s_players_guess[i] == "Y":
            i_guessed_yellow = i_guessed_yellow + 1



    i_num_of_white_pegs = i_num_of_white_pegs + min(i_guessed_blue, i_actual_blue)
    i_num_of_white_pegs = i_num_of_white_pegs + min(i_guessed_green, i_actual_green)
    i_num_of_white_pegs = i_num_of_white_pegs + min(i_guessed_pink, i_actual_pink)
    i_num_of_white_pegs = i_num_of_white_pegs + min(i_guessed_purple, i_actual_purple)
    i_num_of_white_pegs = i_num_of_white_pegs + min(i_guessed_red, i_actual_red)
    i_num_of_white_pegs = i_num_of_white_pegs + min(i_guessed_yellow, i_actual_yellow)

    i_num_of_white_pegs = i_num_of_white_pegs - i_total_black_pegs

    print("White pegs: ", i_num_of_white_pegs)

    return i_num_of_white_pegs

i_total_white_pegs = calculate_white_pegs(s_comp_code, s_players_guess, i_total_black_pegs)




# Updates the screen/serves as a main function
def update_screen(i_total_black_pegs, i_total_white_pegs):
    
    i_guesses = 0
    
    while i_total_black_pegs != 4 and i_guesses != 7:
        s_players_guess = players_guess(s_begin)
        i_total_black_pegs = calculate_black_pegs(s_comp_code, s_players_guess)
        i_total_white_pegs = calculate_white_pegs(s_comp_code, s_players_guess, i_total_black_pegs)
        i_guesses = i_guesses + 1

    if i_total_black_pegs == 4:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lose!")

    return

i_update = update_screen(i_total_black_pegs, i_total_white_pegs)
print("The computers code: ", s_comp_code)
