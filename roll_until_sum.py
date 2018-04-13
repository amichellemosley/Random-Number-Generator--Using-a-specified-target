from random1 import randrange

def WelcomeMessage():
    print( "This program rolls two 6-sided die until their sum is a given target value. " )
    return WelcomeMessage

def getTargetValue():
    targetValue = int(input('Enter the target sum to roll for:  '))
    return targetValue

def oneRoll():
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    sumOfRoll = dice1 + dice2 
    targetValue = getTargetValue()
    numberOfRolls = 0
    while True:
        if sumOfRoll == targetValue:
            print ( 'Got it in {0} Rolls!'.format(numberOfRolls))
            break
        elif sumOfRoll != targetValue:
            dice1 = randrange(1,7)
            dice2 = randrange(1,7)
            sumOfRoll = dice1 + dice2
            numberOfRolls += 1
            print("Roll: {0} and {1}, sum is {2}".format(dice1, dice2, sumOfRoll))
             
    return oneRoll

def main():
    WelcomeMessage()
    #getTargetValue()
    oneRoll()
##    GameRoll()
    
main()
