import re
from typing import List, Tuple 

class CardNumber:
    number :int
    marked : bool
    def __init__(self, number: int) -> None:
        self.number = number
        self.marked = False
    
    def __str__(self) -> str:
        pass

    def hasBeenSinged (self, singedNumber: int):
        if not self.marked and self.number == singedNumber:
            self.marked = True

BingoArray = List[List[CardNumber]]
