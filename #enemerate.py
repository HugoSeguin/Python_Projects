#enemerate

from dataclasses import dataclass


class myEnumerate():
    def __init__(self, data):
        self.data = data
        self.index= 0
    def __inter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (slef.index, self.data[self.index])
        self.index += 1
        return value
for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')