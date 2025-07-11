import time
import random
import sys

# Variables
names = [
    "Khalid", "Yusuf", "Tariq", "Marwan", "Hakam",
    "Qasim", "Abdullah", "Ali", "Mohammed", "Muawiya"
]
name_of_the_cheerful_man = random.choice(names)  # Initialize this variable


class GameState:
    def __init__(self):
        self.score = 0  # Initialize player score
        self.money = 0  # Initialize player money
        self.cheerful_man_name = random.choice(names)
        # Stores the cheerful character's name


def print_pause(text, pause=1):
    print(text)
    time.sleep(pause)


def win_lose_functions(state: GameState):
    if state.score < 55:
        print_pause("GAME OVER!", 2)
        play_again(state)
    elif state.score >= 55:
        print_pause(
            "CONGRATULATIONS! you win and went back to your home.", 2 
        )
        play_again(state)


def play_again(state: GameState):
    while True:
        play_again = input("play again? (yes/no): ").lower()
        if play_again in ("yes", "y"):
            state = GameState()
            damascus_time_travel(state)
            break
        elif play_again in ("no", "n"):
            print("Thanks for playing!")
            sys.exit()
        else:
            print_pause("Enter a valid unit")


def first_scene(state: GameState):
    print_pause("You woke up at 1:00 pm feeling extremely bored.", 2)
    print_pause("The house is quiet. Too quiet.", 2)
    print_pause("You want to do something fun!", 2)
    print_pause(
        "Now you go to your PC and play an Islamic game that set in the "
        "Umayyad era.",
        2
    )
    print_pause("You hear someone calling you.", 2)
    print_pause("You went out to check.", 2)
    print_pause("WHAT IS THIS!", 4)
    where_am_i(state)


def where_am_i(state: GameState):
    state.cheerful_man_name
    print_pause(
        "You landed on the spice mart with a lot of trading camels "
        "roaming about.",
        2
    )
    print_pause("You are lost and don't understand anything.", 2)
    while True:
        choice = input("Enter 1 to ask anyone where you are: ").strip()
        if choice == "1":
            print_pause(
                "You start searching for someone to ask him where are you.",
                2
            )
            print_pause("That's him!", 1)
            print_pause(
                "A bearded, cheerful man in a white turban and crimson robe."
                " His silver ring glinted. A curved dagger hung at his waist.",
                2
            )
            print_pause("You ask what year it is.", 2)
            print_pause("He smiles to you and says 715!", 2)
            print_pause("You ask him: where we are?.", 2)
            print_pause("He says: You are in Damascus,the capital!", 2)
            print_pause("Now you understand everything.", 2)
            print_pause("This is the game that I was playing!", 2)
            name_of_the_cheerful_man = random.choice(names)
            a_great_offer(state)
            break
        else:
            print_pause("Sorry, enter a valid unit.")


def a_great_offer(state: GameState):
    print_pause("You ask him: What is your name?", 2)
    print_pause(f"He says: My name is: {name_of_the_cheerful_man}.", 2)
    print_pause("What do you do in this mess?", 2)
    print_pause(
        "He says,You can follow me to explore the city.", 2
    )
    print_pause("Will you accept?", 2)
    while True:
        print_pause("Enter 1 to accept (the best choice).", 2)
        print_pause("Enter 2 to decline (the worst and most dangerous).", 2)
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            state.score += 10
            print_pause(
                f"You accept and {name_of_the_cheerful_man} says: "
                "I have some things to do in the city. Come with me.",
                2
            )
            print_pause("+10pts", 2)
            print_pause(f"your score: {state.score}", 2)
            print_pause("You accept.", 2)
            print_pause(
                "The weather is very hot and you want something to drink!",
                2
            )
            print_pause("But you don't have money!", 2)
            print_pause(f"You tell {name_of_the_cheerful_man}.", 2)
            print_pause(
                "He says: I know a guy who challenges people to a game of "
                "darts for money if they win.",
                2
            )
            print_pause("you say: OK, take me to him.", 2)
            print_pause("You go to the man and start playing!", 2)
            print_pause("The seller says, It's only 5 throws, be focused!", 2)
            print_pause("You need to throw darts at the leather shield.", 2)
            print_pause("Each hit is worth 10 dirhams.", 2)
            print_pause("The first!", 3)
            print_pause("OPPS! You missed!", 2)
            print_pause("The second!", 3)
            print_pause("YOU GOT IT! 🎯", 2)
            print_pause("The third!", 3)
            print_pause("You got it! 🎯", 2)
            print_pause("Nice game!", 2)
            print_pause("The fourth!", 3)
            print_pause("You got it! 🎯", 2)
            print_pause("You are brilliant today!", 2)
            print_pause("The last!", 3)
            print_pause("You missed!", 2)
            print_pause("Now you have 30 dirhams.", 2)
            tour_in_damascus(state)
            break
        elif choice == "2":
            dangerous_choice(state, show_warning=True)
            break
        else:
            print("Sorry, enter a valid unit.")


def tour_in_damascus(state: GameState):
    state.money = 30
    print_pause(
        "While taking a tour in Damascus with you start searching for a "
        "drinks seller.",
        2
    )
    print_pause(
        "You found drinks seller near the Great Umayyad Mosque.", 2
    )
    print_pause("You buy Jallab juice by 7 dirhams", 2)
    state.money -= 7
    print_pause(f"You have: {state.money} dirhams", 2)
    print_pause(
        f"You and {name_of_the_cheerful_man} go to the Great Umayyad Mosque "
        "and take a tour in Damascus until the sun sets.",
        2
    )
    print_pause(
        f"{name_of_the_cheerful_man} offered you to stay the night with him",
        2
    )
    while True:
        print_pause("Enter 1 to accept.", 2)
        print_pause("Enter 2 to decline.", 2)
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            state.score += 15
            print_pause("+15pts", 2)
            print_pause(f"your score: {state.score}", 2)
            print_pause(
                "You got to his house and he give you dinner", 2
            )
            print_pause(
                "And he gave you a blanket and a place to sleep", 2
            )
            print_pause(
                "now you go to sleep in the place that he prepared for you",
                2
            )
            print_pause("...", 3)
            print_pause("You wake-up at 2:00 feeling thirsty", 2)
            print_pause(
                "you went out from the room to drink from the jar.", 4
            )
            print_pause("OH MY GOD!", 2)
            print_pause("What is happening now?!", 2)
            print_pause("What is this spacious garden?", 2)
            print_pause("And what is this three doors?", 2)
            print_pause(
                "You see an old man coming to you saying:"
                "Choose one of this doors to enter it, one of them is your end!",
                3
            )
            print_pause("What door will you choose?", 2)
            while True:
                door = input("Enter [1, 2, or 3]: ").strip()
                if door in ("1", "2", "3"):
                    if door == "1":
                        print_pause(
                            "You fall into a deep hole and die.", 1
                        )
                        state.score -= 20
                        print_pause("-20pts", 2)
                        print_pause(f"Final score: {state.score}", 2)
                        win_lose_functions(state)
                        break
                    elif door == "2":
                        print_pause("you found a long path", 2)
                        print_pause("you walking on it...", 2)
                        print_pause("you found a door, and open it", 2)
                        state.score += 50
                        print_pause("+50pts", 2)
                        print_pause(f"Final score: {state.score}", 2)
                        win_lose_functions(state)
                        break
                    elif door == "3":
                        print_pause("you found a long path", 2)
                        print_pause("you walking on it...", 2)
                        print_pause("you found a door, and open it", 2)
                        state.score += 40
                        print_pause("+40pts", 2)
                        print_pause(f"Final score: {state.score}", 2)
                        win_lose_functions(state)
                        break
                else:
                    print_pause("Please enter 1, 2, or 3.")
        elif choice == "2":
            dangerous_choice(state, show_warning=True)
            break
        else:
            print_pause("sorry, enter a valid unit", 2)


def dangerous_choice(state, show_warning=True):
    if show_warning:
        print_pause("Unexpected, honestly.", 2)
    state.score -= 5
    print_pause("-5pts", 2)
    print_pause(f"your score: {state.score}", 2)
    print_pause(
        "You start searching for a source of money...", 2
    )
    print_pause(
        "An old man leaning on a crutch with hunched back waves at you "
        "from across the street!",
        2
    )
    print_pause("Help me carry these bags for 100 dirhams!", 2)
    print_pause(
        "You accept the offer, despite feeling suspicious of him", 2
    )
    print_pause("You grab the heavy bags, noticing a strange smell...", 2)
    print_pause(
        "The old man leads you into a narrow, dimly lit alley.", 3
    )
    print_pause(
        "His walking speed suddenly improves... too much.", 2
    )
    print_pause(
        "He starts attacking you, pulling out his dagger while trying to harm you!"
    )
    print_pause("What will you do?")


def run_away(state: GameState):
    state.score += 25
    print_pause("+25pts", 1)
    print_pause(f"Your Score: {state.score}", 3)
    print_pause("You try to run forward but fail!", 2)
    print_pause(
        f"You found {name_of_the_cheerful_man} extending his hands to you!", 3
    )
    print_pause(
        "You take his hands and he takes you to the spice mart while both of "
        "you are running from the old man and his gang",
        3
    )
    print_pause(
        "running and running, you find a big wall and the gang is behind you!",
        2
    )
    print_pause(
        f"Suddenly! {name_of_the_cheerful_man} opens a slot in the wall and "
        "enters inside it!",
        2
    )
    print_pause("He takes your hands to enter it.", 2)
    print_pause(f"You enter with {name_of_the_cheerful_man} inside.", 2)
    print_pause("Beautiful, spacious garden and three doors in front of you", 2)
    print_pause("What door will you choose?", 2)
    while True:
        door = input("Enter [1, 2, or 3]: ").strip()
        if door in ("1", "2", "3"):
            if door == "1":
                print_pause("You fall into a deep hole and die.", 1)
                win_lose_functions(state)
                break
            elif door == "2":
                print_pause("you found a long path", 2)
                print_pause("you walking on it...", 2)
                print_pause("you found a door, and open it", 2)
                state.score += 50
                print_pause("+50pts", 2)
                print_pause(f"Final score: {state.score}", 2)
                win_lose_functions(state)
                break
            elif door == "3":
                print_pause(
                    "The door takes you back in time to the old man", 2
                )
                dangerous_choice(state, show_warning=False)
                win_lose_functions(state)
                break
        else:
            print_pause("Please enter 1, 2, or 3.")


def defend_yourself(state: GameState):
    print_pause("You try to punch him", 2)
    print_pause("But before you can react—", 2)
    print_pause("Something hard hits your skull!", 3)
    print_pause("...", 3)
    print_pause("Your vision blurs.", 2)
    print_pause("...", 4)
    print_pause("You wake up with a pounding headache.", 3)
    print_pause("The room reeks of mold and blood.", 2)
    print_pause("Your pockets are empty. Your phone is gone.", 2)
    print_pause("A rusty door creaks open...", 3)
    print_pause(
        "The 'old man' stands there—no crutch, no hunched back!", 3
    )
    print_pause("He tosses your ID card into a pile of others.", 3)
    print_pause("-10pts", 2)
    state.score -= 10
    print_pause(f"Final Score: {state.score}", 3)
    win_lose_functions(state)


def print_slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


title = """
╔══════════════════════════════╗
║     DAMASCUS TIME TRAVEL     ║
╚══════════════════════════════╝
"""


def damascus_time_travel(state: GameState):
    print_slow(title)
    first_scene(state)


if __name__ == "__main__":
    state = GameState()
    damascus_time_travel(state)
