class Player:
    def __init__(self, health: int = 5) -> None:
        self.health = health

    def is_dead(self) -> bool:
        return self.health <= 0