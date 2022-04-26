from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivationByType
from mesa.datacollection import DataCollector
import numpy as np

'''
Compartments
1) Bacteria (S. aureus)
2) Neutrophils
'''

class Bacteria(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        #self.age = self.random.randint(0, 72) # The start age as random
                
    def get_id(self):
        return "B_ID: " + str(self.unique_id)
        
    def step(self):
        #self.increment_age()
        self.move()
        self.reproduce()

    def move(self):
        # Get the position of the neighboring cells and
        # select a random position to move to
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    #def increment_age(self):
    #    self.age += 1 # hour

    def reproduce(self):
        #if self.age > 168: # 24h x 7 days = 168
        #    self.model.grid._remove_agent(self.pos, self)
        #    self.model.schedule.remove(self)
        #else:

        # Bacteria has a random change of reproducing
        if self.random.random() < self.model.bacteria_reproduce:
            baby_bacteria = Bacteria(self.model.next_id(), self.model)
            self.model.grid.place_agent(baby_bacteria, self.pos)
            self.model.schedule.add(baby_bacteria)
            
class Neutrophil(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        #self.age = self.random.randint(0, 72) # The start age as random

    def get_id(self):
        return "N_ID: " + str(self.unique_id)

    def step(self):
        #self.increment_age()
        self.move()
        self.eat_bacteria()
        #self.die() 

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def eat_bacteria(self):
        ## If there is a bacteria in the same cell, eat it
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        bacteria = [obj for obj in this_cell if isinstance(obj, Bacteria)]
        if len(bacteria) > 0:
            bacteria_to_eat = self.random.choice(bacteria)
            # Kill the bacteria
            self.model.grid.remove_agent(bacteria_to_eat)
            self.model.schedule.remove(bacteria_to_eat)

            # After a neutrophil eats a bacteria, it has a chance of reproduction
            if self.random.random() < self.model.neutrophil_reproduce:
                baby_neutrophil = Neutrophil(self.model.next_id(), self.model)
                self.model.grid.place_agent(baby_neutrophil, self.pos)
                self.model.schedule.add(baby_neutrophil)
        
    #def increment_age(self):
    #    self.age += 1 # hour

    #def die(self):
    #    if self.age > 168: # 24h x 7 days = 168
    #        self.model.grid.remove_agent(self)
    #        self.model.schedule.remove(self)

'''
Skin Model
'''

# Actual Model:
class Skin(Model):

    def __init__(self, N_bacteria, N_neutrophil, bacteria_reproduce, neutrophil_reproduce, width, height):
        super().__init__()    
        self.num_bacteria = N_bacteria
        self.num_neutrophil = N_neutrophil
        self.bacteria_reproduce = bacteria_reproduce
        self.neutrophil_reproduce = neutrophil_reproduce

        self.grid = MultiGrid(width, height, False)
        self.schedule = RandomActivationByType(self)
        self.running=True
        
        # Create initial number of bacteria
        for i in range(self.num_bacteria):
            b = Bacteria(self.next_id(), self)
            self.schedule.add(b)

            # add the bacteria to the left-most location with random y
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (0, y))

        # Create initial number of neutrophils
        for i in range(self.num_neutrophil):
            b = Neutrophil(self.next_id(), self)
            self.schedule.add(b)

            # add the neutrophil to the right-most location with random y
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (self.grid.width-1, y))

        # Data collection plots for the graphs
        self.datacollector = DataCollector({
            'S. aureus burden': 'bacteria',
            'Neutrophils': 'neutrophil'
        })

    @property
    def bacteria(self):
        return self.schedule.get_type_count(Bacteria)

    @property
    def neutrophil(self):
        return self.schedule.get_type_count(Neutrophil)
    
    def step(self):
        #print([obj.get_id() for obj in self.schedule.agents if isinstance(obj, Bacteria)])
        #print([obj.get_id() for obj in self.schedule.agents if isinstance(obj, Neutrophil)])
        self.datacollector.collect(self)
        self.schedule.step()
