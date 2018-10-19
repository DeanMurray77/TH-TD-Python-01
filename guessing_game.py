import random

def start_game():

    print("Hello, and welcome to the number guessing game.")
    print("The way that this works is the system will choose a random number between 1 and 20 (inclusive).")
    print("Then you'll be prompted to guess a number.")
    print("If you guess the right number, then the round is over and you win.")
    print("If you guess the wrong number, then I'll tell you if the number is higher or lower than your guess.")
    print("Then, you can guess again.")
    print("The system will keep track of your fewest number of guesses to win during a particular session.")

    user_wants_to_continue = "yes"
    low_score = 999999
    while user_wants_to_continue != "no":

        if low_score == 999999:
            print("This is the first time through, so there currently isn't a high score.")
        else:
            print("Your current best score is {}.".format(low_score))
        count_of_guesses = 0
        random_number = random.randint(1,20)
        while True:
            try:
                user_guess = int(input("Please enter your guess (a number from 1-20 ) "))
            except ValueError:
                print("Please enter a valid number as a numeral ('1' rather than 'one')")
                print("Let's try again:")
            else:
                if user_guess < 1:
                    print("You've entered a number that is too small. Please enter a number between 1 and 20 inclusive")
                    print("Let's try again:")
                    continue
                if user_guess > 20:
                    print("You've entered a number that is too big. Please enter a number between 1 and 20 inclusive")
                    print("Let's try again:")
                    continue
                if user_guess < random_number:
                    print("It's higher")
                    count_of_guesses += 1
                    continue
                if user_guess > random_number:
                    print("It's lower")
                    count_of_guesses += 1
                    continue
                count_of_guesses += 1
                print("Congratulations, you got it! The number was {}, and it only took you {} guesses!".format(random_number, count_of_guesses))
                break
        
        if count_of_guesses < low_score:
            print("Your new best score is {}:".format(count_of_guesses))
            low_score = count_of_guesses
        else:
            print("Your current best score is {}:".format(low_score))
        
        user_wants_to_continue = "blah"
        while((user_wants_to_continue.lower() != 'yes') and (user_wants_to_continue.lower() != 'no')):
            user_wants_to_continue = input("This round is over. Would you like to play again? (yes/no)")
            if ((user_wants_to_continue.lower() != 'yes') and (user_wants_to_continue.lower() != 'no')):
                print("Please enter 'yes' or 'no' without the quotes")
        
    print("Thanks for playing. Your best score for this session was {} guesses.".format(low_score))
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()