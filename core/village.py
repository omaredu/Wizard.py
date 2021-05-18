from core.fairy import Fairy
from core.house import House

class Village:
    def __init__(self) -> None:
        self.__used_buildings: list[House] = []
        self.__unused_buildings: list[House] = []

    def build(self) -> None:
        self.__unused_buildings.append(House())

    def use_house(self, fairy: Fairy) -> bool:
        if len(self.__unused_buildings) <= 0:
            return False

        house = self.__unused_buildings.pop()
        house.use(fairy)

        self.__used_buildings.append(house)
        return True

    def available_houses(self) -> int:
        return len(self.__unused_buildings)

    def unavailable_houses(self) -> int:
        return len(self.__used_buildings)