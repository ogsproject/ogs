import json, os
from MinecraftServerManager import MinecraftServer
from MinecraftServerManager import ConfigObject

class MinecraftServerManagerConfig(ConfigObject.Config):
    def __init__(self, filePath):
        ConfigObject.Config.__init__(self, filePath, {
                "server" :
                {
                    "host" : "0.0.0.0",
                    "port" : 8080,
                    "working-directory" : "./data"
                },
                "server-list" : 
                [
                ]
        })

class MinecraftServerManager:
    def __init__(self, filePath):
        self.config = MinecraftServerManagerConfig(filePath)
        if not os.path.exists(filePath):
            self.config.save()
        else:
            self.config.load()

        self.serverList = []
        print (self.config.get("server-list"))
        for s in self.config.get("server-list"):
            directory = os.path.join(self.config.get("server", "working-directory"), s.get("name"))
            self.serverList.append(MinecraftServer.MinecraftServer(s["name"], directory = directory))

        if not os.path.isdir(self.config.get("server", "working-directory")):
            os.mkdir(self.config.get("server", "working-directory"))

    def createServer(self, name):
        directory = os.path.join(self.config.get("server", "working-directory"), name)
        server = MinecraftServer.MinecraftServer(name, directory = directory)
        if server.isConfigured():
            raise Exception("Server already exists")
        else:
            server.create()
            self.__appendServer(server)
            return server

    def __appendServer(self, server):
        self.config.get("server-list").append({"name" : server.name})
        self.config.save()

    def start(self, name):
        for s in self.serverList:
            if s.name == name:
                s.start()

