"""
projekt2_bulls_and_cows.py: druhý projekt do Engeto Online Akademie - Datový analytik s Pythonem, varinta 1 Bulls & Cows
author: Tomáš Pakosta
email: tpakosta@gmail.com
discord: Tom P. (tom.pa.costa) Tom#2303
"""

import random # provides functions for generating random numbers
import time
import csv
import os


# ----- FUNCTIONS ---------------------------------------------------------------------------------------------------------


def generate_number():
    """
    Generate a 4-digit random number where each digit is unique and the number cannot start with 0.
    :return: A list of 4 unique digits forming the random number.
    """
    items= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(items)
    #print(items)
    
    random_number = digits[:4] if digits[0] != 0 else digits[1:5]

    return random_number


def valid_number_input():
    """
    Prompt the user to input a valid 4-digit number.
    This function ensures that the input has no duplicates, is exactly 4 digits long, 
    and does not start with 0.
    :return: A list of digits of the valid number entered by the user.
    """

    while True:
        try:
                # Prompt the user for input
            user_input = input(">>> ")
                # Try to convert the input to an integer
            number = int(user_input)
                # Transform to the list of digits
            number = [int(digit) for digit in str(number)]
                # check if the input number has 4 digits
            if len(number) == 4:
                    # Check for duplicates
                has_duplicates = len(number) != len(set(number))
                if has_duplicates:
                    print("The number has duplicated digits.")
                else:
                    #print("Valid number! ", len(number))
                    return number
            else:
                print("Invalid number! Please enter a 4 digits number.")    

        except ValueError:
            # Handle the case where the input is not a number
            print("Input is not a valid number. Please try again.")


def guess_number(user_number, random_number):
    """
    Compares the user's guess to the random number and returns a dictionary with bulls and cows count.
    :param user_number: List of digits representing the user's guess.
    :param random_number: List of digits representing the secret random number.
    :return: A dictionary with the count of bulls and cows.
    """
    result = {'bulls':0, 'cows':0}
        
    i = 0
    for num in user_number:
        if num in random_number:
            if i == random_number.index(num):
                result['bulls'] += 1
            else:
                result['cows'] += 1
        i += 1
    return result   


def save_result(guesses, e_time):
    """
    Saves the result of the game to a CSV file, updating the rounds and times.
    If the file already exists, the result is added, and the player's rank is displayed.
    :param guesses: The number of guesses the player took.
    :param e_time: The elapsed time in seconds for the game.
    """
    results = {}
    
    if os.path.isfile("project2_game_results.csv"):
        rounds = {}
        times = {}
        turn = 0
        
        with open("project2_game_results.csv",
            mode="r+",
            encoding="UTF-8",
            newline=""  # None
        ) as file: 
            reader = csv.reader(file)
            for row in reader:
                
                if row[0] != "Turns": # Skip header
                    
                    key = int(row[0])  # First column as key
                    value_1 = int(row[1])  # Second column as value
                    value_2 = float(row[2])
                    rounds[key] = value_1
                    times[key] = value_2
                   
                else:
                    continue

            turn = max(rounds.keys()) + 1 # the new turn number

            # Write the new result to the file
            result = [turn, guesses, e_time]
            rounds[result[0]] = result[1]
            times[result[0]] = result[2]     
            writer = csv.writer(file, delimiter=",")
            writer.writerow(result)  # Write all numbers in one row

        print(f"Your result have been written to {file.name}.")
        # Sort the values in descending order and remove duplicates
        sorted_rounds = sorted(set(rounds.values()))
        sorted_times= sorted(set(times.values()))
        
        # Find the rank of the value
        rank_rounds = sorted_rounds.index(result[1]) + 1  # Add 1 for 1-based rank
        print(f"The rank of your rounds is: {rank_rounds}")
        rank_times = sorted_times.index(result[2]) + 1
        print(f"The rank of your time is: {rank_times}")
    
    else:
        # If file doesn't exist, create it and add the first record
        with open("project2_game_results.csv",
            mode="w+",
            encoding="UTF-8",
            newline=""  # None
        ) as file:
            writer = csv.DictWriter(file, fieldnames=["Turns", "Rounds", "Time"])
            writer.writeheader()
            writer = csv.writer(file, delimiter=",")
            result = [1, guesses, e_time]
            writer.writerow(result)  # Write all numbers in one row
        print(f"Your result have been written to {file.name} and it is the first play.")

        


# ----- MAIN --------------------------------------------------------------------------------------------------------------

print(f"Hi there!")
print(f"-----------------------------------------------")
random_number = generate_number()
print(f"I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(f"-----------------------------------------------")
print(random_number)
print(f"Enter a number:")
print(f"-----------------------------------------------")
user_number = valid_number_input() # Get the player's first guess
start_time = time.time() # Record the start time
end_game = False
num_guess = 0

while end_game == False:
    
    guess_result = guess_number(user_number, random_number)
    num_guess += 1
    bulls = guess_result['bulls']
    cows = guess_result['cows']
    
    print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
    print(f"-----------------------------------------------")
    
    if bulls == 4:
        end_time = time.time() 
        elapsed_time = end_time - start_time
        print(f"Correct, you've guessed the right number\nin {num_guess} guesses and {elapsed_time:.2f} seconds!")
        save_result(num_guess, elapsed_time)
        end_game = True
    else: user_number = valid_number_input()



"""

possible extensions: user menu for calling up results (e.g. top 10), deleting results, etc.


"""