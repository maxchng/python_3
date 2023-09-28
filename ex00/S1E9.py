from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class, mean you cannot create an instance of this class,
    You can only create its subclass
    """
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character class"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """every subclass must have its abstract method"""
        pass


class Stark(Character):
    """I Have No CLUE!, Stark is a character. :]"""
    def die(self):
        """Change is_alive status to False"""
        self.is_alive = False
