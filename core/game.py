from core.fairy import Fairy
from core.ogre import Ogre
from core.village import Village
from core.wizard import Wizard
from core.player import Player

import random

class Game:
    def __init__(self) -> None:
        self.player: Player = Player()
        self.wizard: Wizard = Wizard()
        self.village: Village = Village()
        self.ogre: Ogre = Ogre()

        self.__health_counter: int = 0

    def build_house(self) -> None:
        self.village.build()

    def random_attack(self) -> bool:
        attack: bool = random.randint(0, 100) < 50
        if (attack):
            self.player.health -= 1

        return attack

    def steal_fairy(self) -> bool:
        if self.village.available_houses() <= 0:
            return False

        fairy: Fairy = self.wizard.steal_fairy()

        if fairy == None:
            return False

        out = self.village.use_house(fairy)

        if out:
            self.__health_counter += 1
        
        if self.__health_counter >= 10:
            self.player.health += 1
            self.__health_counter = 0

        return out