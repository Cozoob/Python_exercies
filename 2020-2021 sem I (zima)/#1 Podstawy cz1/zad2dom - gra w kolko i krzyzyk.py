# Created by Marcin "Cozoob" Kozub 18.07.2021
# Gra w kolko i krzyzyk.

def print_board(positions):
    i = 0
    print("-------")
    for _ in range(3):

        print("|", end='')
        for _ in range(3):
            if positions[i] == ' ':
                print(i + 1, end='')
            else:
                print(positions[i], end='')
            print("|", end='')
            i += 1

        print()
        print("-------")


def is_win(positions):

    if positions[0] == positions[1] == positions[2] and positions[0] != ' ':
        return True
    if positions[3] == positions[4] == positions[5] and positions[3] != ' ':
        return True
    if positions[6] == positions[7] == positions[8] and positions[6] != ' ':
        return True
    if positions[0] == positions[3] == positions[6] and positions[0] != ' ':
        return True
    if positions[1] == positions[4] == positions[7] and positions[1] != ' ':
        return True
    if positions[2] == positions[5] == positions[8] and positions[2] != ' ':
        return True
    if positions[0] == positions[4] == positions[8] and positions[0] != ' ':
        return True
    if positions[2] == positions[4] == positions[6] and positions[2] != ' ':
        return True

    return False

def is_full(positions):
    for elem in positions:
        if elem == ' ':
            return False
    return True


if __name__ == '__main__':
    print("Let's play noughts and crosses!")
    print("Made by Cozoob.")
    print()
    playing = True
    while playing:
        positions = [' ' for _ in range(9)]
        print("The board: ")
        print_board(positions)
        print("The first player uses crosses, the second one uses noughts. GL & HF")
        print()
        flag = True

        while flag:
            checker = is_full(positions)
            if checker:
                flag = True
                print("Oh no! The board is full! No one wins.")
                break

            print("The first player now: ")
            print("Where do you put the cross? (1/2/3/.../9/exit)")
            new_cross = input("> ")
            if new_cross == "exit":
                print("Thanks for playing! Bye!")
                exit()
            else:
                new_cross = int(new_cross) - 1

            while not checker:
                if positions[new_cross] == ' ':
                    checker = True
                    positions[new_cross] = 'X'
                else:
                    print("The position is already claimed. Choose another one.")
                    print("Where do you put the cross? (1/2/3/.../9/exit)")
                    new_cross = input("> ")
                    if new_cross == "exit":
                        print("Thanks for playing! Bye!")
                        exit()
                    else:
                        new_cross = int(new_cross) - 1

            if is_win(positions):
                print("Congratulations to the first player! You win!")
                print_board(positions)
                flag = True
                break

            print()
            print("The board: ")
            print_board(positions)

            checker = is_full(positions)
            if checker:
                flag = True
                print("Oh no! The board is full! No one wins.")
                break

            print("The second player now: ")
            print("Where do you put the nought? (1/2/3/.../9/exit)")
            new_cross = input("> ")
            if new_cross == "exit":
                print("Thanks for playing! Bye!")
                exit()
            else:
                new_cross = int(new_cross) - 1

            while not checker:
                if positions[new_cross] == ' ':
                    checker = True
                    positions[new_cross] = 'O'
                else:
                    print("The position is already claimed. Choose another one.")
                    print("Where do you put the nought? (1/2/3/.../9/exit)")
                    new_cross = input("> ")
                    if new_cross == "exit":
                        print("Thanks for playing! Bye!")
                        exit()
                    else:
                        new_cross = int(new_cross) - 1

            if is_win(positions):
                print("Congratulations to the second player! You win!")
                print_board(positions)
                flag = True
                break

            print()
            print("The board: ")
            print_board(positions)

        print()
        print("Do you wanna play one more time? (YES/NO)")
        answer = input("> ")
        if answer == 'NO':
            print("Thanks for playing! Bye!")
            playing = False
            break