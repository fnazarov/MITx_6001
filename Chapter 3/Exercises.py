print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = (low + high) / 2
print("Is your secret number 50?")
response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
d='n'
while d != 'y':
    if response == 'l':
        high = low
    elif response == 'h':
        low = high
    elif response == 'c':
        print('Game over. Your secret number was: ', ans)
        break
    else:
        print("Sorry, I did not understand your input.")
    print("Is your secret number ", ans, "?")
    ans = (low + high) / 2
    response = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

