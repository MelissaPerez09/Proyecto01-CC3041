import json
from TuringSimulator import TMSimulator

# open and load the configuration from the input file
file = open("res/turing_machine.json")
turing_machine = json.load(file)

# create an instance of the TMSimulator using the loaded configuration
sim = TMSimulator(turing_machine)

# simulation input
input = "10"
accepted = sim.derivate(input, print_steps=True)

print("")
if accepted:
    print("The input '{}' has been accepted by the machine.".format(input))
else:
    print("The input '{}' has not been accepted by the machine.".format(input))