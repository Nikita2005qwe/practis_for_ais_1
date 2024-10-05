from dataclasses import dataclass
from LinkedList import (LinkedListItem, LinkedList)


@dataclass
class Composition:
    name: str
    path: str


class PlayList(LinkedList):
    def __init__(self, first_item=None):
        super().__init__(first_item)
        self.current = self.first_item
        
    def play_all(self, item: LinkedListItem):
        """Метод проигрывает все треки начиная с item"""
        #сделать проигрывание композиций по их пути
        pass
    
    def next_track(self):
        """
        перейти к следующему треку
        """
        self.current = self.current.next_item
    
    def previous_track(self):
        """
        перейти к предыдущему трэку
        """
        self.current = self.current.previous_item
    
    @property
    def current(self):
        return self.current

    @current.setter
    def current(self, value):
        self.current = value
