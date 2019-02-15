import os
import random
import string
import sys

from . import GameManager
from . import Config
from . import Global
from . import Server

class ServerManager(object):
    def __init__(self):
        self.gameManager = GameManager.GameManager()
        self.config = Config.ConfigDict({
            "ServerList" :
            [
            ]
        })

        self.configFile = Global.Config(os.path.join(Global.GlobalConfig.ConfigPath, "servers.json"), self.config)
        self.configFile.preSaveCallback.append(self.preSaveConfig)

        if not os.path.exists(self.configFile.filePath):
            self.configFile.save()
        else:
            self.configFile.load()

        self.ServersDataPath = Global.GlobalConfig.ServersDataPath

    def loadGames(self, path):
        sys.path.append(path)
        self.gameManager.load(path)

    def preSaveConfig(self):
        pass

    def getServer(self, config):
        game = self.gameManager.getGame(config["game"].get())
        if game == None:
            raise Exception("No game for %s" %(config["game"].get()))

        server = game.getServer(config)
        if not issubclass(type(server), Server.Server):
            raise Exception("Not a sub class of Server.Server")

        return server

    def createServer(self, game):
        config = self.getInitialServerConfig(game)
        server = self.getServer(config)
        os.makedirs(server.workingDirectory)
        server.create(self)
        self.__appendServer(server)

    def setServer(self, name, prop, val):
        server = self.getServerFromName(name)
        if server == None:
            raise Exception("Not existing server %s" % name)
        server[prop] = val
        self.configFile.save()

    def getServerFromName(self, name):
        for s in self.ServerList:
            if s["name"].get() == name:
                return s
        return None

    def getInitialServerConfig(self, game):
        name = None
        while True:
            name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if self.getServerFromName(name) == None:
                break

        return Config.ConfigDict({
            "name" : name,
            "workingDirectory" : os.path.join(self.ServersDataPath, name),
            "game" : game
        })

    def __appendServer(self, server):
        self.ServerList.append(server.config)

    def start(self, name):
        serverConfig = self.getServerFromName(name)
        server = self.getServer(serverConfig)
        if server == None:
            raise Exception("Server %s not existing" % name)
        server.start()

    @property
    def ServerList(self):
        return self.config["ServerList"]

