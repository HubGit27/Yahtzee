"""
File:    Pytzee.py
Author:  Brandon Ta
Date:    3/29/2022
Section: 23
E-mail:  bta1@umbc.edu
Description:
  This program allows a user to play pytzee
"""

import random

TOTAL_DICE = 5
DICE_FACES = 6
USED_COUNTS = list()
PLAYER_SCORE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
PYTZEE_COUNT = 0


def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    roll_list = []
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))
    return roll_list


def add_score(list_to_add):
    """
    Adds up all the values in a list
    :param list_to_add: The list that needs to be added together into a int
    :returns: An intger of the score
    """
    score = 0
    for i in list_to_add:
        score += i
    return score


def three_of_a_kind(rolled_dice):
    '''
    Checks to see if the roll was a valid three_of_a_kind
    :param rolled_dice: The list of values from the dice rolled
    :returns: boolean
    '''
    match = False
    #Makes sure that there are three in a row in the rolled dice
    for i in rolled_dice:
        count = 0
        for j in rolled_dice:
            if i == j:
                count += 1
            if count >= 3:
                match = True
    
    return match


def four_of_a_kind(rolled_dice):
    '''
    Checks to see if the roll was a valid four_of_a_kind
    :param rolled_dice: The list of values from the dice rolled
    :returns: boolean
    '''
    match = False
    #Makes sure that there are four in a row in the rolled dice
    for i in rolled_dice:
        count = 0
        for j in rolled_dice:
            if i == j:
                count += 1
            if count >= 4:
                match = True
    
    return match


def pytzee(rolled_dice):
    """
    Checks  to see if the roll was a valid pytzee
    :param rolled_dice: The list of values from the dice rolled
    :returns: boolean
    """
    match = False
    #Checks if there are 5 in a row
    for i in rolled_dice:
        count = 0
        for j in rolled_dice:
            if i == j:
                count += 1
            if count >= 5:
                match = True

    return match


def small_straight(rolled_dice):
    """
    Checks  to see if the roll was a valid small straight
    :param rolled_dice: The list of values from the dice rolled
    :returns: boolean
    """
    match = False
    #Checks if there are 4 consecutive numbers rolled
    for i  in rolled_dice:
        straight = 0
        for j  in rolled_dice:
            if i + 1 == j:
                straight += 1
            elif i + 2 == j:
                straight += 2
            elif i + 3 == j:
                straight += 3
            if straight == 6:
                    match = True  
    
    return match


def large_straight(rolled_dice):
    """
    Checks  to see if the roll was a valid 5 straight
    :param rolled_dice: The list of values from the dice rolled
    :returns: boolean
    """
    match = False
    #Checks if there are 5 consecutive numbers rolled
    for i  in rolled_dice:
        straight = 0
        for j  in rolled_dice:
            if i + 1 == j:
                straight += 1
            elif i + 2 == j:
                straight += 2
            elif i + 3 == j:
                straight += 3
            elif i + 3 == j:
                straight += 4
            if straight == 10:
                    match = True 

    return match 


def full_house(rolled_dice):
    """
    Checks  to see if the roll was a valid full house straight
    :param rolled_dice: The list of values from the dice rolled
    :returns: boolean
    """
    match1 = False
    match2 = False
    three_match = None

    #Checks that there are three numbers matching
    for i in rolled_dice:
        count = 0
        for j in rolled_dice:
            if i == j:
                count += 1
            if count >= 3:
                three_match = i
                match1 = True

    #Checks that there are two numbers matching
    for i in rolled_dice:
        count = 0
        for j in rolled_dice:
            if i == j and j != three_match:
                count += 1
            if count >= 2:
                match2 = True

    if match1 and match2:
        return True
    else:
        return False


def number_count(rolled_dice, number):
    """
    Adds points to the scorecard if the user chose to count with a number
    :param rolled_dice: The list of values from the dice rolled
    :param number: The number that was chosen as the count
    :returns: nothing
    """
    count = 0
    number = int(number[-1:])
    for i in rolled_dice:
        if i == number:
            count += 1

    PLAYER_SCORE[number - 1] = count * number

    return None


def count():
    """
    Ask the user how they would like to count
    """
    #Makes sure that the user input is valid and the count hasn't already been used
    temp_count = input("How would you like to count this dice roll? ").lower()
    valid_count = False
    while valid_count == False:

        if temp_count == "count 1" or \
        temp_count == "count 2" or \
        temp_count == "count 3" or \
        temp_count == "count 4" or \
        temp_count == "count 5" or \
        temp_count == "count 6" or \
        temp_count == "three of a kind" or temp_count == "3 of a kind" or \
        temp_count == "4 of a kind" or temp_count == "four of a kind" or \
        temp_count == "full house" or \
        temp_count == "chance" or \
        temp_count == "pytzee" or \
        temp_count == "small straight" or \
        temp_count == "large straight" or\
        temp_count == "skip":
            valid_count = True

            #Makes sure that the method of count hasn't already been used
            for i in USED_COUNTS:
                if temp_count == i:
                    valid_count = False
                    print("There was already a score in that slot.")
                    temp_count = input("How would you like to count this dice roll? ").lower()
            
        else:  
            print("That is not a valid count.")
            temp_count = input("How would you like to count this dice roll? ").lower()
    
    #adds how the user counted to a list so that it can't be used again
    if temp_count == "pytzee" or temp_count == "skip":
        pass
    elif temp_count == "three of a kind" or temp_count == "3 of a kind":
        USED_COUNTS.append("three of a kind")
        USED_COUNTS.append("3 of a kind")
    elif temp_count == "four of a kind" or temp_count == "4 of a kind":
        USED_COUNTS.append("four of a kind")
        USED_COUNTS.append("4 of a kind")
    else:
        USED_COUNTS.append(temp_count)

    return temp_count
    

def scorecard():
    """
    Displays the scorecard
    :returns: nothing
    """
    score_types = ["Three of a Kind", "Four of a Kind", "Full House",\
     "Small straight", "Large Straight", "Yahtzee", "Chance"]

    print("\t Scorecard: \n 1's \t 2's \t 3's \t 4's \t 5's \t 6's")

    for i in range(6):
        print(PLAYER_SCORE[i], end="\t ")

    print("")

    for i in score_types:
        print(i, end=" ")

    print("")

    j = 0
    for i in range(6,13):
        print(str(PLAYER_SCORE[i]).rjust(len(score_types[j])), end = " ")
        j += 1

    return None


def final_score():
    """
    Calculates the final score of the game and adds bonus points
    for dice counts
    """
    final = add_score(PLAYER_SCORE)
    count = 0
    for i in range(6):
        count += PLAYER_SCORE[i]
    
    if count >= 63:
        final += 35

    return final




def play_game(num_rounds):
    """
    Function that runs the game
    :param num_rounds: integer to dertermine how many rounds will be played
    :returns: nothing
    """
    rounds_played = 1
    score = 0 

    while rounds_played < (num_rounds + 1):
        rolled_dice = roll_dice()
        print(f"***** Beginning Round {rounds_played} *****")
        
        #Displays the score
        print(f"Your score is: {add_score(PLAYER_SCORE)}")

        #Displays the dice rolled
        for i in rolled_dice:
            print(i, end="    ")
        print("")

        #Loop to keep asking for the users count until valid
        valid_count = False
        while valid_count == False:

            #Ask how the user wants to count
            temp_count = count()

            #Checks what the count was to add it to their score
            if temp_count == "three of a kind" or temp_count == "3 of a kind":

                #Checks if the count is valid
                if three_of_a_kind(rolled_dice) == True:
                    print("Three of a kind!")
                    valid_count = True
                    PLAYER_SCORE[6] = add_score(rolled_dice)
                else:
                    print("You do not have three of a kind")
                    USED_COUNTS.remove("three of a kind")
                    USED_COUNTS.remove("3 of a kind")
            
            elif temp_count == "4 of a kind" or temp_count == "four of a kind":
                
                #Checks if the count is valid
                if four_of_a_kind(rolled_dice) == True:
                    print("Three of a kind!")
                    valid_count = True
                    PLAYER_SCORE[7] = add_score(rolled_dice)
                else:
                    print("You do not have four of a kind.")
                    USED_COUNTS.remove("four of a kind")
                    USED_COUNTS.remove("4 of a kind")
            
            elif temp_count == "full house":
                #Checks if the count is valid
                if full_house(rolled_dice) == True:
                    print("Full house!")
                    valid_count = True
                    PLAYER_SCORE[8] = add_score(rolled_dice)
                else:
                    print("You do not have full house.")
                    USED_COUNTS.remove("full house")
                    USED_COUNTS.remove("full house")

            elif temp_count == "chance":
                PLAYER_SCORE[12] = add_score(rolled_dice)
                valid_count = True

            elif temp_count == "pytzee":
                
                #Checks if the count is valid
                if pytzee(rolled_dice) == True:
                    print("You have a pytzee and get 50 points.")
                    valid_count = True
                    PLAYER_SCORE[11] += 50
                    PYTZEE_COUNT += 1

                    #Adds bonus pytzee points
                    if PYTZEE_COUNT > 1:
                            PLAYER_SCORE[11] += 50
                else:
                    print("You do not have pytzee.") 
                
            elif temp_count == "small straight":

                #Checks if the count is valid
                if small_straight(rolled_dice) == True:
                    print("You have a small straight and get 30 points.")
                    valid_count = True
                    PLAYER_SCORE[9] += 30
                else:
                    print("You do not have a small straight.")
                    USED_COUNTS.remove("small straight")

            elif temp_count == "large straight":

                #Checks if the count is valid
                if full_house(rolled_dice) == True:
                    print("You have a small straight and get 40 points.")
                    valid_count = True
                    PLAYER_SCORE[10] += 30
                else:
                    print("You do not have a large straight.")
                    USED_COUNTS.remove("large straight")

            elif temp_count == "skip":
                valid_count = True

            else:
                number_count(rolled_dice, temp_count)
                print(f"Accepted the {temp_count[-1:]}")
                valid_count = True
        
        scorecard()
        print("")

        rounds_played += 1


if __name__ == '__main__':
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)
    print(f"Your final score was {final_score()}")
