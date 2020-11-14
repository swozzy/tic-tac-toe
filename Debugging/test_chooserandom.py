import chooserandom
import unittest

class Test_TestChooseFirst(unittest.TestCase):

    # There's a ton of test cases
    # Give it like ~30 seconds to run

    def test_run_mult_times(self):
        self.assertAlmostEqual(chooserandom.run_mult_times(), 50, 1)

if __name__ == "__main__":
    unittest.main()