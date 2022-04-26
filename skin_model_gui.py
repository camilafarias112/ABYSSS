from skin_model import *
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

'''
Compartment vizualization
'''

def agent_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Bacteria:
        portrayal["Shape"] = "Viz/Microbe_Staphylococcus.png"
        portrayal["scale"] = 0.8
        portrayal["Layer"] = 1

    elif type(agent) is Neutrophil:
        portrayal["Shape"] = "Viz/Neutrophil.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1   

    return portrayal

'''
The canvas and information input
'''

grid = CanvasGrid(agent_portrayal, 15, 15, 500, 500)

chart = ChartModule([{"Label": "S. aureus burden", "Color": "purple"},
                     {"Label": "Neutrophils","Color": "red"}
])


model_params = {
    'width': 15,
    'height': 15,
    'N_bacteria': UserSettableParameter(
        'slider', 'Number of bacteria', 10, 0, 100, 1),
    'N_neutrophil': UserSettableParameter(
        'slider', 'Number of neutrophils', 30, 0, 100, 1),
    'bacteria_reproduce': UserSettableParameter(
        'slider', 'Probability of bacteria multiplying', 0.01, 0, 1, 0.05),
    'neutrophil_reproduce': UserSettableParameter(
        'slider', 'Probability of neutrophil multiplying', 0.01, 0, 1, 0.05)
}



server = ModularServer(Skin,
                       [grid, chart],
                       "Skin Infection Model",
                       model_params)

server.port = 8521 # The default
server.launch()


