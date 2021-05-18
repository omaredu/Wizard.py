from core.fairy import Fairy
from typing import Union

class Wizard:
    def __init__(self, power: int = 2) -> None:
        self.__fairies: list[Fairy] = []

        for i in range(power*10):
            self.__fairies.append(Fairy())
        
        self.power = int(len(self.__fairies)/10)

    def steal_fairy(self) -> Union[Fairy, None]:
        fairy = None

        try:
            fairy = self.__fairies.pop()
        except:
            pass

        self.power = int(len(self.__fairies)/10)

        return fairy

    def is_dead(self) -> bool:
        return self.power <= 0