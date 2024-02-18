import json
from TuringSimulator import TMSimulator

# open and load the configuration from the input file
file = open("res/turing_machine.json")
turing_machine = json.load(file)

# create an instance of the TMSimulator using the loaded configuration
sim = TMSimulator(turing_machine)

# simulation input
input = "111"
accepted = sim.derivate(input, print_steps=True)

print("")
if accepted:
    print("The input '{}' has been accepted by the machine.".format(input))
else:
    print("The input '{}' has not been accepted by the machine.".format(input))

print("")
print(f"Input: '{input}'")
print(f"Input in decimal notation: '{input.count('1')}'")
print("")
print(f"Result: '{sim.get_tape_string()}'")
print(f"Result in decimal notation: '{sim.get_tape_string().count('1')}'")
    