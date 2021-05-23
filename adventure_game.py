import time
import random

enemies = ["Dragon", "Giant", "Alien"]

enemy = random.choice(enemies)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(x, y, z):
    while True:
        choice = input(x).lower()
        if choice == y:
            break
        elif choice == z:
            break
        else:
            print_pause("i do not understand")
    return choice


def intro():

    print_pause("you find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers,")
    print_pause(f"Rumor has it the {enemy} is somewhere around here")
    print_pause("and has been terrifying the nearby village.")
    print_pause("in front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty")
    print_pause("(but not very effective) dagger.")


def option1(x, y, z):
    print_pause("Enter 1 to knock on the door of the house")
    print_pause("Enter 2 to peer into the cave")
    answer = valid_input("what would you like to do.\n", "1", "2")
    if answer == 1:
        print_pause("you approach the door of the house")
        print_pause("you are about to knock when the door opens..")
        print_pause(f"and out steps a {enemy}")
        print_pause(f"EEp! This is the {enemy}'s house!")
        print_pause(f"The {enemy} attacks you!")
        option3()
    elif answer == 2:
        print_pause("you peer cautiously into the cave.")
        print_pause("it turns out to be only a very small cave")
        print_pause("your eyes catch a glint of metal behind a rock")
        print_pause("you have found the magical sword of ogoroth!")
        print_pause("you discard your silly old dagger")
        print_pause("and take the sword with you")
        print_pause("you walk back out to the field")
        option4()

    else:
        print("please enter 1 or 2")
        return answer


def option3():
    print_pause("you feel a bit under-prepared for this..")
    print_pause("what with only having a tiny dagger.")
    answer = valid_input("would you like to (1) fight or "
                         " (2)run away?\n", "1", "2")
    if answer == 1:
        print_pause("you do your best...")
        print_pause(f"but your dagger is no match for the {enemy}")
        print_pause("you have been defeated!")
        answer = valid_input("would you like to play again?\n", "yes", "no")
        if answer == yes:
            print_pause("here we go!")
            game()
        elif answer == no:
            print_pause("thank you for playing!")
        else:
            print_pause("i do not understand")
            return answer
    elif answer == 2:
        print_pause("you run back into the field.")
        print_pause("luckily, you dont seem to have been followed.")
        option1()
    else:
        print_pause("i do not understand")
        return answer


def option2():
    answer = valid_input("would you like to (1) fight or "
                         " (2) run away?\n", "1", "2")
    if answer == 1:
        print_pause(f"as the {enemy} moves to attack you,")
        print_pause("you unsheath your new sword")
        print_pause(f"But the {enemy} takes one look")
        print_pause("at your shiny new toy and runs away!")
        print_pause(f"you have rid the town of the {enemy}!")
        print_pause("you are victoriious!")
        answer = valid_input("would you like to play again?\n", "yes", "no")
        if answer == yes:
            print_pause("here we go!")
            game()
        elif answer == no:
            print_pause("thank you for playing")
        else:
            print_pause("i do not understand")
            return valid_input
    elif answer == 2:
        print_pause("you run back into the field.")
        print_pause("luckily, you dont seem to have been followed.")
        option4()
    else:
        print_pause("i do not understand")
        return answer


def option4():
    print_pause("Enter 1 to knock on the door of the house")
    print_pause("Enter 2 to peer into the cave")
    answer = valid_input("what would you like to do.\n", "1", "2")
    if answer == 1:
        print_pause("you approach the door of the house")
        print_pause(f"you are about to knock when the door opens..")
        print_pause(f"and out stepts a {enemy}")
        print_pause(f"EEp! This is the {enemy} house!")
        print_pause(f"The {enemy} attacks you!")
        option2()
    elif answer == 2:
        print_pause("you peer cautiously into the cave")
        print_pause("youve been here before, and gotten all the good stuff.")
        print_pause("its just an empty cave now.")
        print_pause("you walk back out to the field")
        option4()
    else:
        print_pause("please enter 1 or 2")
        return answer


def game():

    global enemy

    enemies = ["dragon", "pirate", "alien"]

    enemy = random.choice(enemies)

    intro()
    option1()


game()
