from OpenGameServer import Server
from OpenGameServer import Game
from OpenGameServer import Downloader


class GameTest1(Game.Game):
    name = "GameTest1"
    def __init__(self):
        pass

def getGame():
    return GameTest1()

