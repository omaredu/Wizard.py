from core import Game

ANSI_RESET = "\u001B[0m"
ANSI_BLACK = "\u001B[30m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
ANSI_CYAN = "\u001B[36m"
ANSI_WHITE = "\u001B[37m"

GAME_TITLE = r"""
 ___       __   ___  ________  ________  ________  ________      ________  ___    ___ 
|\  \     |\  \|\  \|\_____  \|\   __  \|\   __  \|\   ___ \    |\   __  \|\  \  /  /|
\ \  \    \ \  \ \  \\|___/  /\ \  \|\  \ \  \|\  \ \  \_|\ \   \ \  \|\  \ \  \/  / /
 \ \  \  __\ \  \ \  \   /  / /\ \   __  \ \   _  _\ \  \ \\ \   \ \   ____\ \    / / 
  \ \  \|\__\_\  \ \  \ /  /_/__\ \  \ \  \ \  \\  \\ \  \_\\ \ __\ \  \___|\/  /  /  
   \ \____________\ \__\\________\ \__\ \__\ \__\\ _\\ \_______\\__\ \__\ __/  / /    
    \|____________|\|__|\|_______|\|__|\|__|\|__|\|__|\|_______\|__|\|__||\___/ /     
                                                                         \|___|/      
                                                                        by Omaredu
"""

class Ui:
    def __init__(self, game: Game) -> None:
        self.__gameEnded: bool = False
        self.game: Game = game

    def init(self) -> None:
        self.__run()

    def __run(self) -> None:
        self.__show_main_menu()
        input: int = self.__ask_number()

        if input ==  1:
            while not self.__gameEnded:
                self.__play()
        else:
            self.__end_game()

    def __play(self) -> None:
        if self.game.player.is_dead():
            self.__show_error("The Wizard defeated you... Try again and defeat the Wizard!")
            self.__end_game()
        elif self.game.wizard.is_dead():
            self.__show_message("You defeated the Wizard, you won!")
            self.__end_game()

        self.__show_status()
        self.__show_options()

        input = self.__ask_number()

        if input == 1:
            self.__show_message("Building new house...")
            self.game.build_house()
        elif input == 2:
            if self.game.steal_fairy():
                self.__show_message("You stole one of the Wizard's fairies")
            else:
                self.__show_error("It looks like you don't have enough available houses to do that...")
        else:
            self.__end_game()

        if self.game.random_attack():
            self.__show_error("Oh no, the Ogre did just attacked you!")

    def __show_main_menu(self) -> None:
        print(ANSI_PURPLE + GAME_TITLE + ANSI_RESET)
        print(
            "1. Play" +
            "\n" +
            "2. Exit"
        )

    def __ask_number(self) -> int:
        res: int = 0
        try:
            res: int = int(input(ANSI_CYAN + "$ " + ANSI_RESET))
        except:
            pass
        return res

    def __show_status(self) -> None:
        print(
            ANSI_YELLOW +
            f"Player's HP: {self.game.player.health}" + "\n" +
            f"Available houses in the village: {self.game.village.available_houses()}" + "\n" +
            f"Unavailable houses in the village (saved fairies): {self.game.village.unavailable_houses()}" + "\n" +
            f"Wizard's PP: {self.game.wizard.power}" + "\n" +
            ANSI_RESET
        )

    def __show_options(self) -> None:
        print(
            "1. Build a new house" + "\n" +
            "2. Steal a fairy" + "\n" +
            "3. End game" + "\n"
        )

    def __show_error(self, message) -> None:
        print(
            ANSI_RED +
            "> " + message +
            ANSI_RESET
        )

    def __show_message(self, message) -> None:
        print(
            ANSI_GREEN +
            "> " + message +
            ANSI_RESET
        )

    def __end_game(self) -> None:
        print(
            ANSI_PURPLE +
            "Thanks for playing Wizard.py by Omaredu" +
            ANSI_RESET
        )
        exit()
