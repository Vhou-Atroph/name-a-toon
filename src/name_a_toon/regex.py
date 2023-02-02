import re

title = re.compile('^[0-9]{1,4}[*]0[*]')

first = re.compile('^[0-9]{1,4}[*]1[*]')

last1 = re.compile('^[0-9]{1,4}[*][2-3][*]')

last2 = re.compile('^[0-9]{1,4}[*]4[*]')

class NameList():
    """Class that holds a list of all possible Toon Name entries."""
    def __init__(self):
        self.title = []
        self.first = []
        self.last1 = []
        self.last2 = []
    def fromfile(file:str):
        #TODO: this
        print("unimplemented")