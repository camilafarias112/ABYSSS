from skin_model import *
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer

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

grid = CanvasGrid(agent_portrayal, 15, 15, 500, 500) # Size of the grid

chart = ChartModule([{"Label": "S. aureus burden",
                      "Color": "Purple"}],
                    data_collector_name='datacollector')

server = ModularServer(Skin,
                       [grid, chart],
                       "Skin Infection Model",
                       {"N_bacteria":15, "N_neutrophil":15, "bacteria_reproduce":0.5, "width":15, "height":15}) # Area that the bacteria are allowed to start

server.port = 8521 # The default
server.launch()


