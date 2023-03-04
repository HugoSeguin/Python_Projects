#Ice Cream

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor
def create_scoops():
    scoops = [Scoop('chcolate'), Scoop('Vanilla'), Scoop('Persimmon')]
    for scoop in scoops:
        print(scoop.flaovr)
create_scoops()

