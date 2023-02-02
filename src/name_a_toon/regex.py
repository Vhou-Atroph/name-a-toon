import re

title = re.compile('^[0-9]{1,4}[*]0[*]')

first = re.compile('^[0-9]{1,4}[*]1[*]')

last1 = re.compile('^[0-9]{1,4}[*][2-3][*]')

last2 = re.compile('^[0-9]{1,4}[*]4[*]')

class NameList():
    """Class that holds a list of all possible Toon Name entries."""
    def __init__(self,titles=list,firsts=list,last1s=list,last2s=list):
        self.title = titles
        self.first = firsts
        self.last1 = last1s
        self.last2 = last2s
    def from_file(self,path:str):
        file = open(path,'r')
        text = file.readlines()
        file.close()
        for line in text:
            txt = line.split("*", 2)
            match True:
                case re.search('^[0-9]{1,4}[*]0[*]',line):
                    self.title.append(txt[1])
                case re.search('^[0-9]{1,4}[*]1[*]',line):
                    self.first.append(txt[1])
                case re.search('^[0-9]{1,4}[*][2-3][*]',line):
                    self.last1.append(txt[1])
                case re.search('^[0-9]{1,4}[*]4[*]',line):
                    self.last2.append(txt[1])
                case _:
                    continue