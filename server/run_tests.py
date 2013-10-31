#!/usr/bin/env python
#from test.test_auth import TestAuth
from test.test_board import TestBoard
from test.test_user import TestUser
from test.test_post import TestPost
from test.test_session import TestSession
from test.test_mail import TestMail
import unittest
"""
testloader = unittest.TestLoader()
suite = unittest.TestSuite([
    testloader.loadTestsFromTestCase(TestAuth),
    testloader.loadTestsFromTestCase(TestBoard),
    testloader.loadTestsFromTestCase(TestUser),
    testloader.loadTestsFromTestCase(TestPost),
    testloader.loadTestsFromTestCase(TestSession)
])
"""
unittest.main(verbosity=2)
