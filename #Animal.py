#Animal

from doctest import OutputChecker


class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    
    def__repr__(self):
        return f'{self.color}{self.species}, {self.number-of_legs} legs'
class Wolf(Animal):
    def __init__(self, color, number_of_legs):
        super().__init__(color, number_of_legs)

class Sheep(Animal):
    def __init__(self, color, number_of_legs):
        super().__init__(color, number_of_legs)

class Snake(Animal):
    def __init__(self, color, number_of_legs):
        super().__init__(color, number_of_legs)
class Cage():
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals= []
    def add_animals(self,*animals):
        for one_animal in animals:
            self.animals.append(one_animal)
    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output+= '\n'.join('\t' + str(animal)for animal in self.animals)
        return output 

    
