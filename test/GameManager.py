import unittest, os
from OpenGameServer import GameManager, Server, Game

class TestGame1(object):
    def __init__(self):
        pass

class TestGame2(object):
    name = "TestGame2"
    def __init__(self):
        pass

class TestGame3(Game.Game):
    name = "TestGame3"
    def __init__(self):
        pass

class GameManagerTest(unittest.TestCase):

    def test_init(self):
        GameManager.GameManager()

    def test_loadPlugint1(self):
        gameManager = GameManager.GameManager()
        with self.assertRaises(Exception):
            gameManager.addGame(TestGame1())

    def test_loadPlugint2(self):
        gameManager = GameManager.GameManager()
        with self.assertRaises(Exception):
            gameManager.addGame(TestGame2())

    def test_loadPlugint3(self):
        gameManager = GameManager.GameManager()
        gameManager.addGame(TestGame3())

    def test_loadPlugintPath1(self):
        gameManager = GameManager.GameManager()
        gameManager.load(os.path.join(os.path.dirname(__file__), "games"))