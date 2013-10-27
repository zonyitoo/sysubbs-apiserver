from test.test_board import TestBoard
from test.test_auth import TestAuth
from test.test_user import TestUser
import unittest
testloader = unittest.TestLoader()
suite = unittest.TestSuite([
    testloader.loadTestsFromTestCase(TestAuth),
    testloader.loadTestsFromTestCase(TestBoard),
    testloader.loadTestsFromTestCase(TestUser),
])
unittest.main()
