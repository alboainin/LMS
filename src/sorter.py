from reader import *
import string

value = dict()

def sorter():
    
    for index,letter in enumerate(string.ascii_lowercase):
        value[letter]= index+1

        
sorter()

