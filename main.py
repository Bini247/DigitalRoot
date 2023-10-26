import unittest
from test_digital_root import TestDigitalRoot

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDigitalRoot)
    unittest.TextTestRunner(verbosity=2).run(suite)
