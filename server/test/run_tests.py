import unittest

from test_board import TestBoard
from test_user import TestUser
from test_auth import TestAuth

if __name__ == '__main__':
    testloader = unittest.TestLoader()
    suite = unittest.TestSuite([
            testloader.loadTestsFromTestCase(TestAuth),
            testloader.loadTestsFromTestCase(TestUser),
            testloader.loadTestsFromTestCase(TestBoard),
        ])


    unittest.main(verbosity=2)
    
