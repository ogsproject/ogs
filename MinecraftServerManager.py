import json, os
import MinecraftServer

class MinecraftServerManagerConfig:
    def __init__(self, filePath):
        self.filePath = filePath
        self.dict = {
                "server" :
                {
                    "host" : "0.0.0.0",
                    "port" : 8080,
                    "working-directory" : "./data"
                },
                "server-list" : 
                [
                ]
        }


    def load(self): 
        with open(self.filePath, "r") as f:
            jsondict = json.load(f)
            jsondict.update(self.dict)

    def save(self): 
        with open(self.filePath, "w") as f:
            self.dict = json.dump(self.dict, f, sort_keys=True, indent=4)

class MinecraftServerManager:
    def __init__(self, filePath):
        self.config = MinecraftServerManagerConfig(filePath)
        if not os.path.exists(filePath):
            self.config.save()
        else:
            self.config.load()

        self.serverList = []
        for s in self.config.dict["server-list"]:
            self.serverList.append(MinecraftServer.MinecraftServer(s["name"]))

        if not os.path.isdir(self.config.dict["server"]["working-directory"]):
            os.mkdir(self.config.dict["server"]["working-directory"])

    def createServer(self, name):
        directory = os.path.join(self.config.dict["server"]["working-directory"], name)
        server = MinecraftServer.MinecraftServer(name, directory = directory)
        if server.isConfigured():
            raise Exception("Server already exists")
        else:
            server.create()
            return server
