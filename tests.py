import unittest
from turing_machine import TuringMachine

class TestTuringMachine(unittest.TestCase):

    def setUp(self):
        # Define parameters for our example Turing machine instance
        # Based on 3-state busy beaver
        self.states = {'A', 'B', 'C', 'HALT'}
        self.symbols = {'0', '1'}
        self.blank_symbol = '0'
        self.initial_state = 'A'
        self.final_states = {'HALT'}
        self.transitions = {
            ('A', '0'): ('B', '1', 'R'),
            ('A', '1'): ('C', '1', 'L'),
            ('B', '0'): ('A','1','L'),
            ('B', '1'): ('B','1','R'),
            ('C', '0'): ('B','1','L'),
            ('C', '1'): ('HALT','1',None)
        }

    def test_initialization(self):
        tmachine = TuringMachine(
            states=self.states,
            symbols=self.symbols,
            blank_symbol=self.blank_symbol,
            initial_state=self.initial_state,
            final_states=self.final_states,
            transitions=self.transitions
        )

        # Assertions to ensure initialization is correct
        self.assertEqual(tmachine.states, self.states)
        self.assertEqual(tmachine.symbols, self.symbols)
        self.assertEqual(tmachine.blank_symbol, self.blank_symbol)
        self.assertEqual(tmachine.current_state, self.initial_state)

        # Check that all tape cells are initialized to blank symbol by default
        for i in range(-10, 11):
            self.assertEqual(tmachine.tape[i], tmachine.blank_symbol)

    def test_busy_beaver(self):
        # Busy Beaver (known to halt after producing six 1's on the tape).
        tmachine = TuringMachine(
            states=self.states,
            symbols=self.symbols,
            blank_symbol=self.blank_symbol,
            initial_state=self.initial_state,
            final_states=self.final_states,
            transitions=self.transitions
        )

        # Run the Busy Beaver until it halts.
        tmachine.run()

        tape_content=tmachine.get_tape()

        expected_output = ['1'] * 6
        self.assertEqual(tape_content, expected_output, "The tape content should be '{}'".format(''.join(expected_output)))

# Additional tests go here...
if __name__ == '__main__':
    unittest.main()
