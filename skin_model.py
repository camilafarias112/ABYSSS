from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid


class Bacteria(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Neutrophil(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Chemokine(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

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
