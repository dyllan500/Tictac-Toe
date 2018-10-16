import random

lista = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
r = [0]
def printboard():
    print("""_{}_|_{}_|_{}_ 
_{}_|_{}_|_{}_
 {} | {} | {}     
            """.format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8]))
def howto():
    print("""                   How To Play!!!
        The Player that goes first is X and the next Player is O.
        Youngest player goes first, unless playing again the previous winner goes first.
        Winner is who ever gets three in a row.
        To place your piece on the board enter the place you want to place it example...
        Enter 1 for for place 1 and 2 for 2 and so on...
                                    _1_|_2_|_3_
                                    _4_|_5_|_6_
                                     7 | 8 | 9
        If you need to restart game for any reason both players must enter R or Restart.
        To display how to play again enter H or Help.
        """)
def howto2():
    print("""                   How To Play!!!
            The Computer goes first is X and the you are second or O.
            Winner is who ever gets three in a row.
            To place your piece on the board enter the place you want to place it example...
            Enter 1 for for place 1 and 2 for 2 and so on...
                                        _1_|_2_|_3_
                                        _4_|_5_|_6_
                                         7 | 8 | 9
            If you need to restart game for any reason enter R or Restart.
            To display how to play again enter H or Help.
            """)
def restart():
    lista[0] = " "
    lista[1] = " "
    lista[2] = " "
    lista[3] = " "
    lista[4] = " "
    lista[5] = " "
    lista[6] = " "
    lista[7] = " "
    lista[8] = " "
    start()

def playerone():
    while True:
        if lista[0] == "O" and lista[1] == "O" and lista[2] == "O":
            break
        if lista[3] == "O" and lista[4] == "O" and lista[5] == "O":
            break
        if lista[6] == "O" and lista[7] == "O" and lista[8] == "O":
            break
        if lista[0] == "O" and lista[3] == "O" and lista[6] == "O":
            break
        if lista[1] == "O" and lista[4] == "O" and lista[7] == "O":
            break
        if lista[2] == "O" and lista[5] == "O" and lista[8] == "O":
            break
        if lista[0] == "O" and lista[4] == "O" and lista[8] == "O":
            break
        if lista[2] == "O" and lista[4] == "O" and lista[6] == "O":
            break
        playerone = input("Player One: ")
        playerone = playerone.lower()
        if playerone == "1":
            if lista[0] == "X" or lista[0] == "O":
                print("There is already an X or O placed there")
            else:
                lista[0] = "X"
                printboard()
                break
        if playerone == "2":
            if lista[1] == "X" or lista[1] == "O":
                print("There is already an X or O placed there")
            else:
                lista[1] = "X"
                printboard()
                break
        if playerone == "3":
            if lista[2] == "X" or lista[2] == "O":
                print("There is already an X or O placed there")
            else:
                lista[2] = "X"
                printboard()
                break
        if playerone == "4":
            if lista[3] == "X" or lista[3] == "O":
                print("There is already an X or O placed there")
            else:
                lista[3] = "X"
                printboard()
                break
        if playerone == "5":
            if lista[4] == "X" or lista[4] == "O":
                print("There is already an X or O placed there")
            else:
                lista[4] = "X"
                printboard()
                break
        if playerone == "6":
            if lista[5] == "X" or lista[5] == "O":
                print("There is already an X or O placed there")
            else:
                lista[5] = "X"
                printboard()
                break
        if playerone == "7":
            if lista[6] == "X" or lista[6] == "O":
                print("There is already an X or O placed there")
            else:
                lista[6] = "X"
                printboard()
                break
        if playerone == "8":
            if lista[7] == "X" or lista[7] == "O":
                print("There is already an X or O placed there")
            else:
                lista[7] = "X"
                printboard()
                break
        if playerone == "9":
            if lista[8] == "X" or lista[8] == "O":
                print("There is already an X or O placed there")
            else:
                lista[8] = "X"
                printboard()
                break
        if playerone == "h" or playerone == "help":
            howto()
        if playerone == "r" or playerone == "restart":
            r[0] = 1
            break
        else:
            print("You entered an invalid command try again")

def playertwo():
    while True:
        playertwo = input("Player Two: ")
        playertwo = playertwo.lower()
        if playertwo == "1":
            if lista[0] == "X" or lista[0] == "O":
                print("There is already an X or O placed there")
            else:
                lista[0] = "O"
                printboard()
                break
        if playertwo == "2":
            if lista[1] == "X" or lista[1] == "O":
                print("There is already an X or O placed there")
            else:
                lista[1] = "O"
                printboard()
                break
        if playertwo == "3":
            if lista[2] == "X" or lista[2] == "O":
                print("There is already an X or O placed there")
            else:
                lista[2] = "O"
                printboard()
                break
        if playertwo == "4":
            if lista[3] == "X" or lista[3] == "O":
                print("There is already an X or O placed there")
            else:
                lista[3] = "O"
                printboard()
                break
        if playertwo == "5":
            if lista[4] == "X" or lista[4] == "O":
                print("There is already an X or O placed there")
            else:
                lista[4] = "O"
                printboard()
                break
        if playertwo == "6":
            if lista[5] == "X" or lista[5] == "O":
                print("There is already an X or O placed there")
            else:
                lista[5] = "O"
                printboard()
                break
        if playertwo == "7":
            if lista[6] == "X" or lista[6] == "O":
                print("There is already an X or O placed there")
            else:
                lista[6] = "O"
                printboard()
                break
        if playertwo == "8":
            if lista[7] == "X" or lista[7] == "O":
                print("There is already an X or O placed there")
            else:
                lista[7] = "O"
                printboard()
                break
        if playertwo == "9":
            if lista[8] == "X" or lista[8] == "O":
                print("There is already an X or O placed there")
            else:
                lista[8] = "O"
                printboard()
                break
        if " " not in lista:
            break
        if playertwo == "h" or playertwo == "help":
            howto()
        if playertwo == "r" or playertwo == "restart":
            if r[0] == 1:
                restart()
            else:
                print("Player One didn't want to restart")
        else:
            print("You entered an invalid command try again")

def endgame():
    while True:
        endgame = input("Enter R or Restart to play again or Q or Quit to Quit: ")
        endgame.lower()
        if endgame == "r" or endgame == "restart":
            restart()
            break
        elif endgame == "q" or endgame == "quit":
            quit()
            break
        else:
            print("Invalid command try again")

def humangame():
    howto()
    printboard()
    while True:
        playerone()
        if " " not in lista:
            print("Game is a draw")
            endgame()
        if lista[0] == "X" and lista[1] == "X" and lista[2] == "X":
            print("Player One as won!")
            endgame()
            break
        if lista[3] == "X" and lista[4] == "X" and lista[5] == "X":
            print("Player One as won!")
            endgame()
            break
        if lista[6] == "X" and lista[7] == "X" and lista[8] == "X":
            print("Player One as won!")
            endgame()
            break
        if lista[0] == "X" and lista[3] == "X" and lista[6] == "X":
            print("Player One as won!")
            endgame()
            break
        if lista[1] == "X" and lista[4] == "X" and lista[7] == "X":
            print("Player One as won!")
            endgame()
            break
        if lista[2] == "X" and lista[5] == "X" and lista[8] == "X":
            print("Player One as won!")
            endgame()
            break
        if lista[0] == "X" and lista[4] == "X" and lista[8] == "X":
            print("Player One as won!")
            endgame()
            break
        if lista[2] == "X" and lista[4] == "X" and lista[6] == "X":
            print("Player One as won!")
            endgame()
            break

        if lista[0] == "O" and lista[1] == "O" and lista[2] == "O":
            print("Player Two as won!")
            endgame()
            break
        if lista[3] == "O" and lista[4] == "O" and lista[5] == "O":
            print("Player Two as won!")
            endgame()
            break
        if lista[6] == "O" and lista[7] == "O" and lista[8] == "O":
            print("Player Two as won!")
            endgame()
            break
        if lista[0] == "O" and lista[3] == "O" and lista[6] == "O":
            print("Player Two as won!")
            endgame()
            break
        if lista[1] == "O" and lista[4] == "O" and lista[7] == "O":
            print("Player Two as won!")
            endgame()
            break
        if lista[2] == "O" and lista[5] == "O" and lista[8] == "O":
            print("Player Two as won!")
            endgame()
            break
        if lista[0] == "O" and lista[4] == "O" and lista[8] == "O":
            print("Player Two as won!")
            endgame()
            break
        if lista[2] == "O" and lista[4] == "O" and lista[6] == "O":
            print("Player Two as won!")
            endgame()
            break
        else:
            playertwo()

def computereasy():
    howto2()
    printboard()
    while True:
        computere()
        if " " not in lista:
            print("Game is a draw")
            endgame()
        if lista[0] == "X" and lista[1] == "X" and lista[2] == "X":
            print("Computer as won!")
            endgame()
            break
        if lista[3] == "X" and lista[4] == "X" and lista[5] == "X":
            print("Computer as won!")
            endgame()
            break
        if lista[6] == "X" and lista[7] == "X" and lista[8] == "X":
            print("Computer as won!")
            endgame()
            break
        if lista[0] == "X" and lista[3] == "X" and lista[6] == "X":
            print("Computer as won!")
            endgame()
            break
        if lista[1] == "X" and lista[4] == "X" and lista[7] == "X":
            print("Computer as won!")
            endgame()
            break
        if lista[2] == "X" and lista[5] == "X" and lista[8] == "X":
            print("Computer as won!")
            endgame()
            break
        if lista[0] == "X" and lista[4] == "X" and lista[8] == "X":
            print("Computer as won!")
            endgame()
            break
        if lista[2] == "X" and lista[4] == "X" and lista[6] == "X":
            print("Computer as won!")
            endgame()
            break

        if lista[0] == "O" and lista[1] == "O" and lista[2] == "O":
            print("You have won!")
            endgame()
            break
        if lista[3] == "O" and lista[4] == "O" and lista[5] == "O":
            print("You have won!")
            endgame()
            break
        if lista[6] == "O" and lista[7] == "O" and lista[8] == "O":
            print("You have won!")
            endgame()
            break
        if lista[0] == "O" and lista[3] == "O" and lista[6] == "O":
            print("You have won!")
            endgame()
            break
        if lista[1] == "O" and lista[4] == "O" and lista[7] == "O":
            print("You have won!")
            endgame()
            break
        if lista[2] == "O" and lista[5] == "O" and lista[8] == "O":
            print("You have won!")
            endgame()
            break
        if lista[0] == "O" and lista[4] == "O" and lista[8] == "O":
            print("You have won!")
            endgame()
            break
        if lista[2] == "O" and lista[4] == "O" and lista[6] == "O":
            print("You have won!")
            endgame()
            break
        else:
            player()

def computerhard():
    howto2()
    lista[0] = "X"
    printboard()
    player()
    if lista[1] == "O" or lista[3] == "O" or lista[5] == "O" or lista[7] == "O":
        lista[8] = "X"
        printboard()
        player()
        if lista[1] == "O":
            lista[7] = "X"
            printboard()
            player()
            if lista[3] == "O":
                lista[5] = "X"
                printboard()
                player()
                if lista[2] == "O":
                    lista[6] = "X"
                    printboard()
                    print("Tie")
                    endgame()
                else:
                    lista[2] = "X"
                    printboard()
                    print("Tie")
                    endgame()
            else:
                if lista[2] == "O" or lista[6] == "O":
                    if lista[2] == "O":
                        lista[6] = "X"
                        printboard()
                        player()
                        if lista[3] == "O":
                            lista[5] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                        else:
                            lista[3] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                    else:
                        lista[2] = "X"
                        printboard()
                        player()
                        if lista[3] == "O":
                            lista[5] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                        else:
                            lista[3] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                else:
                    lista[3] = "X"
                    printboard()
                    player()
                    if lista[2] == "O":
                        lista[6] = "X"
                        printboard()
                        print("Tie")
                        endgame()
                    else:
                        lista[2] = "X"
                        printboard()
                        print("Tie")
                        endgame()
        elif lista[3] == "O":
            lista[5] = "X"
            printboard()
            player()
            if lista[1] == "O":
                lista[7] = "X"
                printboard()
                player()
                if lista[2] == "O":
                    lista[6] = "X"
                    printboard()
                    print("Tie")
                    endgame()
                else:
                    lista[2] = "X"
                    printboard()
                    print("Tie")
                    endgame()
            else:
                if lista[2] == "O" or lista[6] == "O":
                    if lista[2] == "O":
                        lista[6] = "X"
                        printboard()
                        player()
                        if lista[1] == "O":
                            lista[7] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                        else:
                            lista[1] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                    else:
                        lista[2] = "X"
                        printboard()
                        player()
                        if lista[1] == "O":
                            lista[7] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                        else:
                            lista[7] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                else:
                    lista[7] = "X"
                    printboard()
                    player()
                    if lista[2] == "O":
                        lista[6] = "X"
                        printboard()
                        print("Tie")
                        endgame()
                    else:
                        lista[2] = "X"
                        printboard()
                        print("Tie")
                        endgame()
        elif lista[7] == "O":
            lista[1] = "X"
            printboard()
            player()
            if lista[3] == "O":
                lista[5] = "X"
                printboard()
                player()
                if lista[2] == "O":
                    lista[6] = "X"
                    printboard()
                    print("Tie")
                    endgame()
                else:
                    lista[2] = "X"
                    printboard()
                    print("Tie")
                    endgame()
            else:
                if lista[2] == "O" or lista[6] == "O":
                    if lista[2] == "O":
                        lista[6] = "X"
                        printboard()
                        player()
                        if lista[3] == "O":
                            lista[5] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                        else:
                            lista[3] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                    else:
                        lista[2] = "X"
                        printboard()
                        player()
                        if lista[3] == "O":
                            lista[5] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                        else:
                            lista[3] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                else:
                    lista[3] = "X"
                    printboard()
                    player()
                    if lista[2] == "O":
                        lista[6] = "X"
                        printboard()
                        print("Tie")
                        endgame()
                    else:
                        lista[2] = "X"
                        printboard()
                        print("Tie")
                        endgame()
        elif lista[5] == "O":
            lista[3] = "X"
            printboard()
            player()
            if lista[1] == "O":
                lista[7] = "X"
                printboard()
                player()
                if lista[2] == "O":
                    lista[6] = "X"
                    printboard()
                    print("Tie")
                    endgame()
                else:
                    lista[2] = "X"
                    printboard()
                    print("Tie")
                    endgame()
            else:
                if lista[2] == "O" or lista[6] == "O":
                    if lista[2] == "O":
                        lista[6] = "X"
                        printboard()
                        player()
                        if lista[1] == "O":
                            lista[7] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                        else:
                            lista[1] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                    else:
                        lista[2] = "X"
                        printboard()
                        player()
                        if lista[1] == "O":
                            lista[7] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                        else:
                            lista[7] = "X"
                            printboard()
                            print("Tie")
                            endgame()
                else:
                    lista[7] = "X"
                    printboard()
                    player()
                    if lista[2] == "O":
                        lista[6] = "X"
                        printboard()
                        print("Tie")
                        endgame()
                    else:
                        lista[2] = "X"
                        printboard()
                        print("Tie")
                        endgame()
    elif lista[8] != "O":
        lista[8] = "X"
        printboard()
        player()
        if lista[6] != "O":
            lista[6] = "X"
            printboard()
            player()
            if lista[3] != "O":
                lista[3] = "X"
                printboard()
                print("Computer Has Won!")
                endgame()
            else:
                lista[7] = "X"
                printboard()
                print("Computer Has Won!")
                endgame()
        else:
            lista[2] = "X"
            printboard()
            player()
            if lista[1] != "O":
                lista[1] = "X"
                printboard()
                print("Computer Has Won!")
                endgame()
            else:
                lista[5] = "X"
                printboard()
                print("Computer Has Won!")
                endgame()

    else:
        lista[6] = "X"
        printboard()
        player()
        lista[2] = "X"
        printboard()
        player()
        if lista[1] != "O":
            lista[1] = "X"
            printboard()
            print("Computer Has Won!")
            endgame()
        else:
            lista[3] = "X"
            printboard()
            print("Computer Has Won!")
            endgame()
def player():
    while True:
        player = input("Player: ")
        player = player.lower()
        if player == "1":
            if lista[0] == "X" or lista[0] == "O":
                print("There is already an X or O placed there")
            else:
                lista[0] = "O"
                printboard()
                break
        if player == "2":
            if lista[1] == "X" or lista[1] == "O":
                print("There is already an X or O placed there")
            else:
                lista[1] = "O"
                printboard()
                break
        if player == "3":
            if lista[2] == "X" or lista[2] == "O":
                print("There is already an X or O placed there")
            else:
                lista[2] = "O"
                printboard()
                break
        if player == "4":
            if lista[3] == "X" or lista[3] == "O":
                print("There is already an X or O placed there")
            else:
                lista[3] = "O"
                printboard()
                break
        if player == "5":
            if lista[4] == "X" or lista[4] == "O":
                print("There is already an X or O placed there")
            else:
                lista[4] = "O"
                printboard()
                break
        if player == "6":
            if lista[5] == "X" or lista[5] == "O":
                print("There is already an X or O placed there")
            else:
                lista[5] = "O"
                printboard()
                break
        if player == "7":
            if lista[6] == "X" or lista[6] == "O":
                print("There is already an X or O placed there")
            else:
                lista[6] = "O"
                printboard()
                break
        if player == "8":
            if lista[7] == "X" or lista[7] == "O":
                print("There is already an X or O placed there")
            else:
                lista[7] = "O"
                printboard()
                break
        if player == "9":
            if lista[8] == "X" or lista[8] == "O":
                print("There is already an X or O placed there")
            else:
                lista[8] = "O"
                printboard()
                break
        if " " not in lista:
            break
        if player == "h" or player == "help":
            howto()
        if player == "r" or player == "restart":
            restart()
        else:
            print("You entered an invalid command try again")

def computere():
    while True:
        if lista[0] == "O" and lista[1] == "O" and lista[2] == "O":
            break
        if lista[3] == "O" and lista[4] == "O" and lista[5] == "O":
            break
        if lista[6] == "O" and lista[7] == "O" and lista[8] == "O":
            break
        if lista[0] == "O" and lista[3] == "O" and lista[6] == "O":
            break
        if lista[1] == "O" and lista[4] == "O" and lista[7] == "O":
            break
        if lista[2] == "O" and lista[5] == "O" and lista[8] == "O":
            break
        if lista[0] == "O" and lista[4] == "O" and lista[8] == "O":
            break
        if lista[2] == "O" and lista[4] == "O" and lista[6] == "O":
            break
        com = random.randint(1, 10)
        com = str(com)
        if com == "1":
            if lista[0] == "X" or lista[0] == "O":
                pass
            else:
                lista[0] = "X"
                printboard()
                break
        if com == "2":
            if lista[1] == "X" or lista[1] == "O":
                pass
            else:
                lista[1] = "X"
                printboard()
                break
        if com == "3":
            if lista[2] == "X" or lista[2] == "O":
                pass
            else:
                lista[2] = "X"
                printboard()
                break
        if com == "4":
            if lista[3] == "X" or lista[3] == "O":
                pass
            else:
                lista[3] = "X"
                printboard()
                break
        if com == "5":
            if lista[4] == "X" or lista[4] == "O":
                pass
            else:
                lista[4] = "X"
                printboard()
                break
        if com == "6":
            if lista[5] == "X" or lista[5] == "O":
                pass
            else:
                lista[5] = "X"
                printboard()
                break
        if com == "7":
            if lista[6] == "X" or lista[6] == "O":
                pass
            else:
                lista[6] = "X"
                printboard()
                break
        if com == "8":
            if lista[7] == "X" or lista[7] == "O":
                pass
            else:
                lista[7] = "X"
                printboard()
                break
        if com == "9":
            if lista[8] == "X" or lista[8] == "O":
                pass
            else:
                lista[8] = "X"
                printboard()
                break

def start():
    an = input("Play against human(h) or computer(c): ")
    an = an.lower()
    if an == "h" or an == "human":
        humangame()
    elif an == "c" or an == "computer":
        an2 = input("Easy(e) mode or Hard(h) mode: ")
        an2 = an2.lower()
        if an2 == "e" or an2 == "easy":
            computereasy()
        elif an2 == "h" or an2 == "hard":
            computerhard()
        else:
            print("You entered an invalid command try again")
    else:
        print("You entered an invalid command try again")
start()