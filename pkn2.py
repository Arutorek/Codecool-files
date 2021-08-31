import random




# print ekranu startowego

def print_start_screen():
    print("Witaj w grze kpn \n \n wybierz kamien papier lub nozyce")

# wybór zmiennej użytkownika

def user_choise():
    user_input = input()

    return user_input

# wybór zmiennej kompa

def bot_choise():
    choices = ["kamien", "papier", "nozyce"]
    computer = random.choice(choices)
    print(computer)
    return computer

# wynik pojedynku i nowa gra

def result(user_input, bot_points, turns_number, user_points, computer):
    if user_input == "kamien" and computer == "nozyce" or user_input =="nozyce" and computer == "papier" or user_input == "papier" and computer == "kamien":
        print("wygrałes runde")
        user_points += 1
        turns_number += 1
    elif user_input == "nozyce" and computer == "kamien" or user_input =="papier" and computer == "nozyce" or user_input == "kamien" and computer == "papier":
        print("przegrales runde")
        bot_points += 1
        turns_number += 1
    else: 
        print("remis")
        turns_number += 1
    return user_points, bot_points, turns_number

def main1():
    user_points = 0
    bot_points = 0
    turns_number = 0
    print_start_screen()
    while turns_number < 3:
        user_input = user_choise()
        computer = bot_choise()
        user_points, bot_points, turns_number = result(user_input, bot_points, turns_number, user_points, computer)
        print(user_points, bot_points)
    print("koniec gry")
def main():
    next_game = True
    while next_game:
        main1()
        next_time_input = input("Do You want to play next time? y/n")
        if next_time_input == 'n':
            next_game = False
main()