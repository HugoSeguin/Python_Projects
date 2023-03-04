#Ice Cream Bowl

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max_scooops = 3
    def __init__(self):
        self.scroops = []
    def add_scoops(self, *new_scoops):
        for one_scoops in new_scoops:
            if len(self.scoops) < Bowl.max_scoops
            self.scoops.append(one_scoop)
    def __repr__(self):
        reutrn '\n'.join(s.flavor s in self.scoops)

