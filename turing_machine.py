from collections import defaultdict

class TuringMachine:
    def __init__(self, states, symbols, blank_symbol,
                 initial_state, final_states, transitions):
        # Set of states for the Turing machine.
        self.states = states

        # Set of allowed symbols (alphabet) including the blank symbol.
        self.symbols = symbols

        # The symbol representing 'blank' in tape cells that have not been written.
        self.blank_symbol = blank_symbol

        # The tape is implemented as a defaultdict which returns the blank symbol for any non-initialized index.
        self.tape = defaultdict(lambda: blank_symbol)

        # The current position of the head over the tape (starts at 0).
        self.head_position = 0

        # The initial state in which the Turing machine starts.
        self.current_state = initial_state

        # A set containing all final (halting) states.
        self.final_states = final_states

        # Transition function represented as a dictionary with keys as tuples
        # in form (state, symbol) and values as tuples (new state, symbol to write, direction to move).
        self.transitions = transitions

    def step(self):
        """Performs one step of computation."""
        if self.current_state in self.final_states:
            return False

        symbol_under_head = self.tape[self.head_position]

        if (self.current_state, symbol_under_head) not in self.transitions:
            return False

        new_state, write_symbol, move_dir = \
            self.transitions[(self.current_state, symbol_under_head)]

        if write_symbol is not None:
            # Write new symbol under head only if it's not None
            self.tape[self.head_position] = write_symbol

        if move_dir == 'L':
            # Move head left
            self.head_position -= 1
        elif move_dir == 'R':
            # Move head right
            self.head_position += 1

        # Update current state to new state after transition
        self.current_state = new_state

        return True

    def run(self):
        """Runs the machine until it halts."""
        while True:
            tape_content = tmachine.get_tape()
            print("Tape Content:", ''.join(tape_content))

            if not self.step():
                break

    def get_tape(self):
        """Returns current content of tape."""
        min_used_index = min(self.tape.keys())
        max_used_index = max(self.tape.keys())

        return [self.tape[i] for i in range(min_used_index,
                                          max_used_index + 1)]

# Example usage:

# Define sets and parameters for our example Turing machine instance.
states = {'A', 'B', 'C', 'HALT'}
symbols = {'0', '1'}
blank_symbol = '0'
initial_state = 'A'
final_state = {'HALT'}
transition_function={
    ('A', '0'): ('B', '0', 'R'),
    ('A', '1'): ('B', '1', 'L'),
    ('B', '0'): ('A','1','L'),
    ('B', '1'): ('HALT','0','R'),
}

# Create an instance of our example Turing machine with provided parameters.
tmachine=TuringMachine(states,symbols,
                       blank_symbol,
                       initial_state,
                       final_state,
                       transition_function)

# Initialize tape content (for this example we'll start at position 0 with '0').
tmachine.tape[0] = '0'

# Run the Turing Machine until it halts.
tmachine.run()

# Output the contents of the tape after running.
tape_content = tmachine.get_tape()
print("Final Tape Content:", ''.join(tape_content))
