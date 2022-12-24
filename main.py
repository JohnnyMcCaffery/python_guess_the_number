import random as r

# min and max number to generate between
MIN    = 0
MAX    = 100

def you_have_won_message(attempts):
    data   = f" | You have guessed the correct number in {attempts} attempts |"
    border = (len(data)+1)*"-" 
    print(f"\n{border}\n{data}\n{border}\n")

def play_again(): return True if input("Would you like to play again? (Y | N) ").lower() == "y" else False

def regenerate_number(): return r.randint(MIN,MAX)

def main():
    attempts = 0
    number = regenerate_number()

    while True:
        guess = input(f"Try and guess a number from ({MIN} - {MAX})? ")
        if guess.isdigit():
            attempts += 1
            guess = int(guess)
            if guess == number:
                you_have_won_message(attempts)
                if play_again() == False:
                    break
                else:
                    number = regenerate_number()
                    attempts = 0
                    print()
                    continue
            if guess < number:
                print("You need to guess higher!")
            if guess > number:
                print("You need to guess lower!")
        else:
            print("Please enter a number!")
            
            
main()