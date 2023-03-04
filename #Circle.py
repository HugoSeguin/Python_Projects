#Circle

from dataclasses import dataclass


class CircleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0
    def __next__(self):
        if slef.index>= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(slef.data)]
        self.index += 1
        return value
class Circle():
    def __init__(self):
        self.data = data 
        self.max_times = max_times
    def __inter__(self):
        return CircleIterator(self.data, self.max_times)

