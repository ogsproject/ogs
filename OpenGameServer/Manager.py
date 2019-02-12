import json, os
import urllib.request
import importlib.util
import traceback
import random
import string
import traceback

from OpenGameServer import ConfigObject
from OpenGameServer import Global
from OpenGameServer import Server

class PluginManager(object): 
    def __init__(self):
        self.plugins = {}
        pass

    def load(self, path):
        for d in os.listdir(path):
            try:
                spec = importlib.util.spec_from_file_location(d, os.path.join(path, d, "__init__.py"))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                game = module.getGame()
                self.plugins[game.name] = game
            except Exception as e:
                print ("error loading module %s : %s" % (d, str(e)))

    def getGame(self, name):
        if not name in self.plugins.keys():
            return None
        return self.plugins[name]


class Manager(object):
    def __init__(self, filePath):
        self.pluginManager = PluginManager()
        self.config = ConfigObject.ConfigDict({
            "ServerRootLocation" : Global.config.ServerRootLocation,
            "ServerBinaryLocation" : Global.config.ServerBinaryLocation,
            "ServerList" :
            [
            ]
        })

        self.configFile = ConfigObject.Config(filePath, self.config)
        self.configFile.preSaveCallback.append(self.preSaveConfig)

        if not os.path.exists(self.configFile.filePath):
            self.configFile.save()
        else:
            self.configFile.load()

        if not os.path.isdir(self.config["ServerRootLocation"].get()):
            os.mkdir(self.config["ServerRootLocation"].get())

        if not os.path.isdir(self.config["ServerBinaryLocation"].get()):
            os.mkdir(self.config["ServerBinaryLocation"].get())

        self.pluginManager.load(os.path.join(os.path.dirname(__file__), "plugins"))


    def getFileFromUrl(self , version):
        filePath = os.path.join(self.config["ServerBinaryLocation"].get(), version)
        if not os.path.exists(filePath):
            url = self.config["ServerDownloadLink"][version].get()
            with urllib.request.urlopen(url) as response:
                print (response.headers)
                with open(filePath, "wb") as fileDownloaded:
                    fileDownloaded.write(response.read())
        return filePath

    def preSaveConfig(self):
        pass

    def getServer(self, config):
        game = self.pluginManager.getGame(config["game"].get())
        if game == None:
            raise Exception("No plugin for %s" %(config["game"].get()))

        server = game.getServer(config)
        if not issubclass(type(server), Server.Server):
            raise Exception("Not a sub class of Server.Server")

        return server


    def createServer(self, game):
        config = self.getTempServerConfig(game)
        server = self.getServer(config)
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


    def getTempServerConfig(self, game):
        name = None
        while True:
            name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if self.getServerFromName(name) == None:
                break

        return ConfigObject.ConfigDict({
            "name" : name,
            "workingDirectory" : os.path.join(self.config["ServerRootLocation"].get(), name),
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

