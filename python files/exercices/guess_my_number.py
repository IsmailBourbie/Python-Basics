print('Please think of a number between 0 and 100!')
low_val = 0
heigh_val = 100

while True:
    guess = (heigh_val + low_val) // 2
    print("Is your secret number " + str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if(response == 'l'):
        low_val = guess
    elif (response == "h"):
        heigh_val = guess
    elif (response == "c"):
        print("Game over. Your secret number was:", str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
        
