from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
#from mesa.batchrunner import batch_run

class Bacteria(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.age = 0
    
    def move(self):
        ### bacteria can only move right with a random number of steps
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    
    def increment_age(self):
        self.age += 1

    def die(self):
        if self.age > 7:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)

    def generate_chemokines(self):
        return

    def reproduce(self):
        return

    def step(self):
        self.increment_age()
        self.move()
        ## generate x number of Neutrophils (may have to move this to another class)

        ## reproduce

        ## die if age = x
        self.die()


#class Chemokine(Agent):
#    def __init__(self, unique_id, model):
#        super().__init__(unique_id, model)
#    def step(self):
#        ## recruit neutrophils
#        ## they won't move
#        ## decay


class Neutrophil(Agent):
    def __init__(self, unique_id, model, age):
        super().__init__(unique_id, model, age)
        self.age = 0
    
    def step(self):
        return
        ## neutrophils will home to a bacteria

        ## eat a bacteria if it's in the neighboring cells
        

        ## die after age = x

class Skin(Model):
    def __init__(self, N_bacteria, width, height):
        self.num_bacteria = N_bacteria
        self.grid = MultiGrid(width, height, False)
        self.schedule = RandomActivation(self)
        self.running=True
        
        # Create initial number of bacteria
        for i in range(self.num_bacteria):
            b = Bacteria(i, self)
            self.schedule.add(b)

            # add the bacteria to the leftmost location with random y
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (0, y))

    def step(self):
        self.schedule.step()
