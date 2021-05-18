from typing import Union
from core import fairy
from core.fairy import Fairy


class House:
    def __init__(self) -> None:
        self.fairy: Union[Fairy, None] = None
    
    def use(self, fairy: Fairy) -> None:
        if self.__in_use():
            return
        
        self.fairy = fairy

    def __in_use(self) -> bool:
        return self.fairy != None