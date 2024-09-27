from dataclasses import dataclass
from LinkedList import LinkedListItem


@dataclass
class Composition:
    composition: str


class PlayList(LinkedList):
    def play_all(self, item: LinkedListItem):
        """Метод проигрывает все треки начиная с item"""
        pass
    
