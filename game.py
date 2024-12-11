import logic as lg

#start game

def greeting():
    print("Welcome to the '2048' game. I guess you already know the rules :)")
    print("To swipe to the left/up/right/down enter a/w/d/s from the keyboard")
    print("Let the game begins!")
    lg.field_setting(int(input("Please, enter the size of the matrix: ")))
    print("The game begins!")
    lg.random_spawn()
    lg.field_print()


def start_game():
    greeting()
    
    while True:
        if not lg.can_move():
            print("You lost :(")
            break
                

        cmd = input("Enter the command: ")
        if cmd == 'a':
            if lg.move_l():
                lg.random_spawn()
                lg.field_print()
            else:
                print("You cant use this command! Try another!")
                continue

        elif cmd == 'w':
            if lg.move_u():
                lg.random_spawn()
                lg.field_print()
            else:
                print("You cant use this command! Try another!")
                continue

        elif cmd == 'd':
            if lg.move_r():
                lg.random_spawn()
                lg.field_print()
            else:
                print("You cant use this command! Try another!")
                continue

        elif cmd == 's':
            if lg.move_d():
                lg.random_spawn()
                lg.field_print()
            else:
                print("You cant use this command! Try another!")
                continue

        else:
            print("I dont know this key. To swipe to the left/up/right/down enter a/w/d/s from the keyboard. Try again.")
            continue