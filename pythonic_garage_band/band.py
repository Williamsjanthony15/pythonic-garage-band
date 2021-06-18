class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos = []
        for player in self.members:
            solos.append(player.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:

    def __init__ (self, name, type, solo):
        self.name = name
        self.type = type
        self.solo = solo 



class Guitarist(Band):
    def __str__ (self):
        return f'My name is {self.name} and I play guitar'
    def __repr__ (self):
        return f'Guitarist instance. Name = {self.name}'
    def play_solo(self):
        return f'{self.solo}'
    
    @staticmethod
    def get_instrument():
        return "guitar"


class Bassist(Band):

    def __str__ (self):
        return f'My name is {self.name} and I play bass'
    def __repr__ (self):
        return f'Bassist instance. Name = {self.name}'
    def play_solo(self):
        return f'{self.solo}'
    
    @staticmethod
    def get_instrument():
        return "bass"

class Drummer(Band):

    def __str__ (self):
        return f'My name is {self.name} and I play drums'
    def __repr__ (self):
        return f'Drummer instance. Name = {self.name}'
    def play_solo(self):
        return f'{self.solo}'

    @staticmethod
    def get_instrument():
        return "drums"

