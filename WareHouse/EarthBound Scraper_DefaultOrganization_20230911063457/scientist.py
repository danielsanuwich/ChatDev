'''
This file contains the Scientist class, which represents a scientist from a Danish university.
'''
class Scientist:
    def __init__(self, name):
        '''
        Initializes a Scientist object.
        Parameters:
        - name: A string representing the name of the scientist.
        '''
        self.name = name
        self.commercial_potential = False
    def set_commercial_potential(self, commercial_potential):
        '''
        Sets the commercial potential of the scientist.
        Parameters:
        - commercial_potential: A boolean value indicating whether the research of the scientist has commercial potential.
        '''
        self.commercial_potential = commercial_potential