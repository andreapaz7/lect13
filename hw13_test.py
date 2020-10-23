# TODO get 100% test coverage for hw13.py

import hw13
import unittest 

INPUT = "input"
NUM_ITERS = "num_iters"
INITIAL = "initial"
SECOND = "second"
EXPECTED = "expected"

class HW13TestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                INPUT: {
                    NUM_ITERS: 0,
                    INITIAL: 1,
                    SECOND: 2,
                },
                EXPECTED: "Don't iterate"
            },
            {
                INPUT: {
                    NUM_ITERS: 3,
                    INITIAL: 5,
                    SECOND: 1
                },
                EXPECTED: "counter is 10"
            },
            {
              INPUT: {
                    NUM_ITERS: 7,
                    INITIAL: -5,
                    SECOND: 2
                },
                EXPECTED: "initial is -5"
            }
        ]
        
    def test_function_success(self):
        for test in self.success_test_params:
            response = hw13.my_func(test[INPUT][NUM_ITERS], test[INPUT][INITIAL], test[INPUT][SECOND])
            expected = test[EXPECTED]
            self.assertEqual(response, expected)
    
if __name__ == '__main__':
    unittest.main()
