# The Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(number *3 + 1)
        return number *3 + 1

def startSequence():
    print('Enter number:')
    userInput = input()
    try:
        userInput = int(userInput)
        while userInput != 1 :
            userInput = collatz(userInput)
    except ValueError:
        print('Error: Invalid argument')
        startSequence()
    
        

startSequence()    
