
N = 1_000

class TMSimulator:
    def __init__(self, turing_machine_data: dict) -> None:

        # extracting data from the Turing machine configuration
        states, input_symbols, tape_symbols, blank, start, accept, transitions = turing_machine_data
        self.states = turing_machine_data[states]
        self.input_symbols = turing_machine_data[input_symbols]
        self.tape_symbols = turing_machine_data[tape_symbols]
        self.blank = turing_machine_data[blank]
        self.start = turing_machine_data[start]
        self.accept = turing_machine_data[accept]

        # initialize tape, head position, current state, and transition function
        self.tape = "".join([self.blank]*N)    # Fill the tape with blanks
        self.head = N // 2              # Initialize head in the middle of the tape
        self.current_state = self.start
        self.transition_function = {}
        self.start_index = self.head
        self.end_index = 0

        # build the transition function from the configuration
        for transition in turing_machine_data[transitions]:
            # q: current state, r: read symbol, w: write symbol, d: direction, q1: next state
            q, r, w, d, q1 = transition.split(" ")
            self.transition_function[q, r] = (w, d, q1)
            
    def get_tape_string(self) -> str:
        return self.tape[self.start_index:self.end_index]
    
    # returns a string representation of the tape with the head position indicated by 'v
    def get_head_string(self) -> str:
        head_string = ""
        tape_start_index = self.tape.index(self.get_tape_string())
        if self.head - tape_start_index < 0:
            head_string = "v" + "".join([" "]*abs(self.head - tape_start_index))
        else:
            head_string = "".join([" "]*(self.head - tape_start_index)) + "v"
        return head_string

    # returns a formatted string of the tape with the head position
    def get_tape_fstring(self) -> str:
        tape_fstring = ""
        tape_start_index = self.tape.index(self.get_tape_string())
        tape_lenght = len(self.get_tape_string())
        if self.head - tape_start_index < 0:
            tape_fstring =  "".join([self.blank]*abs(self.head - tape_start_index)) + self.get_tape_string()
        elif self.head - tape_start_index > tape_lenght - 1:
            tape_fstring = self.get_tape_string() + "".join([self.blank]*(self.head - tape_start_index - tape_lenght + 1))
        else:
            tape_fstring = self.get_tape_string()
        return tape_fstring

    # prints the current step of the derivation
    def print_derivation_step(self) -> None:
        print(self.get_head_string())
        print(self.get_tape_fstring(), self.current_state)
    
    # executes one step of the Turing machine
    def step(self) -> bool:
        if self.current_state != self.accept:
            # assert self.head >= 0 and self.head < len(self.tape) here
            a = self.tape[self.head]
            action = self.transition_function.get((self.current_state, a))
            if action:
                w, d, q1 = action
                self.tape = self.tape[:self.head] + w + self.tape[self.head+1:] # Write the symbol to the tape
                if d != 'N':
                    self.head = self.head + (1 if d == 'R' else -1) # Move the head right or left
                self.current_state = q1 # Move to the next state
                return True     # Return true for valid transition
            else:
                return False    # Return false if theres no transition found (Halt)
        return True
    
    # initiates the derivation process with the given input
    def derivate(self, input: str, max_iter=9999, print_steps=False) -> bool: # iterations limit for when the string is not accepted
        self.tape = self.tape[:self.head] + input + self.tape[self.head:]   # Insert input in the middle of the tape
        self.end_index = self.head + len(input) - 1
        iter = 0
        if print_steps: 
            print("Derivation of '{}':\n".format(input))
            self.print_derivation_step()
        while self.current_state != self.accept and iter < max_iter: # Prevent infinite loop
            step_result = self.step()
            if not step_result: break
            if print_steps: self.print_derivation_step()
            iter += 1
        return self.current_state == self.accept
