from ogs import Game


class GameTest1(Game):
    name = "GameTest1"
    def __init__(self):
        pass

def getGame():
    return GameTest1()

