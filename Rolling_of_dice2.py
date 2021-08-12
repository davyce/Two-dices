#This program roll 2 of dices.
import random

#Constant for the minimum and the maximum number
MIN = 1
MAX = 6

def main():
    #Create a function to controll the loop
    again = 'y'

    #Simulate rolling of the dice.
    while again == 'Y' or again == 'y':
        print('Rolling the dice...')
        print('Their value are:')
        x = random.randint(MIN, MAX)
        y = random.randint(MIN, MAX)
        print(x)
        print(y)

        #Do another roll of dice?
        again = input('Roll them again?: ')

#Call the main function
main()
