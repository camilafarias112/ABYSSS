from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.time import RandomActivationByType # Will be needed when other Agents are added
from mesa.datacollection import DataCollector


'''
Compartments
1) Bacteria (S. aureus) - in progress
2) Neutrophils - TBD
'''

class Bacteria(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.age = self.random.randint(0, 72) # The start age as random
        living = True # Indicate to be alive
   
    def step(self): # I cleaned up this part, and re-organized the nature of bacteria
        self.increment_age()
        self.move()
        self.die() 
#        self.reproduce()

    def move(self):
        ### bacteria can only move right with a random number of steps XX
        # Important: It is not moving right. It starts from left only.
        # See forest fire example for that.
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def increment_age(self):
        self.age += 1 # hour

    def die(self):  # Tried to set up reproduction, but I couldn't make it work!
        if self.age > 168: # 24h x 7 days = 168
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            living = False
 #       else:
 #           if self.random.random() < self.model.bacteria_reproduce:
 #           self.age = 100
 #           baby_bacteria = Bacteria(self.model.next.id(), self.model, self.age)
 #           self.model.grid.place_agent(baby_bacteria)
 #           self.model.schedule.add(baby_bacteria)

class Neutrophil(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.age = self.random.randint(0, 72) # The start age as random
        living = True # Indicate to be alive
   
    def step(self): # I cleaned up this part, and re-organized the nature of bacteria
        self.increment_age()
        self.move()
        self.die() 
#        self.reproduce()

    def move(self):
        ### Neutrophils can only move left with a random number of steps XX
        # Important: It is not moving right. It starts from left only.
        # See forest fire example for that.
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def increment_age(self):
        self.age += 1 # hour

    def die(self):  # Tried to set up reproduction, but I couldn't make it work!
        if self.age > 168: # 24h x 7 days = 168
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            living = False
 #       else:
 #           if self.random.random() < self.model.bacteria_reproduce:
 #           self.age = 100
 #           baby_bacteria = Bacteria(self.model.next.id(), self.model, self.age)
 #           self.model.grid.place_agent(baby_bacteria)
 #           self.model.schedule.add(baby_bacteria)

'''
Skin Model
'''

# Actual Model:
class Skin(Model):

#    bacteria_reproduce = 0.04
    verbose = False  # Print-monitoring

    def __init__(self, N_bacteria, width, height):
#    def __init__(self, N_bacteria, width, height, # Things that have to be provided
#                  bacteria_reproduce = 0.04): # Things that are automatic
        super().__init__()    
#        self.bacteria_reproduce = bacteria_reproduce
        self.num_bacteria = N_bacteria
        self.grid = MultiGrid(width, height, False)
        self.schedule = RandomActivationByType(self)
        self.datacollector = DataCollector(
            {"S.aureus": lambda m: m.schedule.get_type_count(Bacteria)}) # It is not collecting burden
        self.running=True
        self.datacollector.collect(self)

        # Create initial number of bacteria
        for i in range(self.num_bacteria):
            b = Bacteria(i, self)
            self.schedule.add(b)

            # add the bacteria to the leftmost location with random y
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (0, y))

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)
        if self.verbose:
            print([self.schedule.time,
                   self.schedule.get_type_count(Bacteria)])

    def run_model(self, step_count=168): # This is not running, supposed to be the initial and final burden track
        if self.verbose:
            print("Initial S. aureus burden: ", self.schedule.get_type_count(Bacteria))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print("")
            print("Final S. aureus burden: ", self.schedule.get_type_count(Bacteria))