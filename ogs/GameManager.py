import os
import importlib.util

from . import Game
from . import Log

class GameManager(object):
    def __init__(self):
        self.plugins = {}

    def load(self, path):
        Log.info("Loading games from directory %s", path)
        for d in os.listdir(path):
            try:
                spec = importlib.util.spec_from_file_location(d, os.path.join(path, d, "__init__.py"))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                game = module.getGame()
                self.addGame(game)
            except Exception as e:
                Log.error(e, exc_info=True)

    def addGame(self, game):
        if not issubclass(type(game), Game.Game):
            raise Exception("Not a sub class of Game.Game")

        if self.getGame(game.name) != None:
            raise Exception("Game already exists %s" % game.name)

        self.plugins[game.name] = game
        Log.info("Loaded games %s", game.name)

    def getGame(self, name):
        if not name in self.plugins.keys():
            return None
        return self.plugins[name]


