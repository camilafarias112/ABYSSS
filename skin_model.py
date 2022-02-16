from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid


class Bacteria(Agent):
    def __init__(self, unique_id, age, model):
        super().__init__(unique_id, age, model)
        
    def move(self):
        ### bacteria can only move right with a random number of steps
        return

    def generate_chemokines(self):
        return

    def reproduce(self):
        return

    def step(self):
        return
        ## bacteria will move

        ## generate x number of Neutrophils (may have to move this to another class)

        ## reproduce

        ## die if age = x



#class Chemokine(Agent):
#    def __init__(self, unique_id, model):
#        super().__init__(unique_id, model)
#    def step(self):
#        ## recruit neutrophils
#        ## they won't move
#        ## decay


class Neutrophil(Agent):
    def __init__(self, unique_id, age, model):
        super().__init__(unique_id, age, model)



    def step(self):
        return
        ## neutrophils will home to a bacteria

        ## eat a bacteria if it's in the neighboring cells
        

        ## die after age = x

class Skin(Model):
    def __init__(self, N_bacteria, width, height):
        self.num_bacteria = N_bacteria
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        
        # Create initial number of bacteria
        for i in range(self.num_bacteria):
            b = Bacteria(i, self)
            self.schedule.add(b)

            # add the bacteria to the leftmost location with random y
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (0, y))
