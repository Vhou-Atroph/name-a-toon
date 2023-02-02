import random

from .regex import NameList

class Name:
    """A Name that can be given to a Toon."""
    def __init__(self,title:str,first:str,last1:str,last2:str):
        self.title = title
        self.first = first
        self.last1 = last1
        if self.last1.endswith("'"):
            self.last2 = last2.title()
        else:
            self.last2 = last2
    
    def fromrand(list:NameList):
        """Generate a completely random name from a given list."""
        return Name(title=random.choice(list.title),
        first=random.choice(list.first),
        last1=random.choice(list.last1),
        last2=random.choice(list.last2))
