#! /usr/bin/env python3

import unittest

if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import os
import ogs

class TestGame1(object):
    def __init__(self):
        pass

class TestGame2(object):
    name = "TestGame2"
    def __init__(self):
        pass

class TestGame3(ogs.Game):
    name = "TestGame3"
    def __init__(self):
        pass

class GameManagerTest(unittest.TestCase):

    def test_init(self):
        ogs.GameManager()

    def test_loadPlugint1(self):
        gameManager = ogs.GameManager()
        with self.assertRaises(Exception):
            gameManager.addGame(TestGame1())

    def test_loadPlugint2(self):
        gameManager = ogs.GameManager()
        with self.assertRaises(Exception):
            gameManager.addGame(TestGame2())

    def test_loadPlugint3(self):
        gameManager = ogs.GameManager()
        gameManager.addGame(TestGame3())

    def test_loadPlugintPath1(self):
        gameManager = ogs.GameManager()
        gameManager.load(os.path.join(os.path.dirname(__file__), "games"))

if __name__ == "__main__":
    unittest.main()

