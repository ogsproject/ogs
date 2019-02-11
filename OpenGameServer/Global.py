import os
from OpenGameServer import ConfigObject


class Global(object):
    def __init__(self):
        self.RootPath = "data"
        self.GlobalConfigPath = "data/etc/"
        self.GlobalConfigFilename = "global.json"
        self.config = ConfigObject.Config(os.path.join(self.GlobalConfigPath, self.GlobalConfigFilename), ConfigObject.ConfigDict({
            "MinecraftServerManagerConfigLocation" : self.GlobalConfigPath,
            "MinecraftServerManagerConfigFilename" : "server.json",
            "ServerRootLocation" : os.path.join(self.RootPath, "servers"),
            "ServerBinaryLocation" : os.path.join(self.RootPath, "binary"),
            "JavaBinPath" : "java"
        }))
        if not os.path.exists(self.config.filePath):
            self.config.save()
        else:
            self.config.load()


    @property
    def MinecraftServerManagerConfigLocation(self):
        return self.config.element["MinecraftServerManagerConfigLocation"].get()

    @property
    def MinecraftServerManagerConfigFilename(self):
        return self.config.element["MinecraftServerManagerConfigFilename"].get()

    @property
    def MinecraftServerManagerConfigFilePath(self):
        return os.path.join(self.MinecraftServerManagerConfigLocation, self.MinecraftServerManagerConfigFilename)

    @property
    def ServerRootLocation(self):
        return self.config.element["ServerRootLocation"].get()

    @property
    def ServerBinaryLocation(self):
        return self.config.element["ServerBinaryLocation"].get()

    @property
    def JavaBinPath(self):
        return self.config.element["JavaBinPath"].get()

config = Global()

#MinecraftServerManagerConfigPath = "config.json"

#JavaBinPath = "/usr/bin/java"
#MinecraftServerJarPath = "server.jar"
#SourceMinecraftServerJarPath = "data/server.jar"
#MinecraftServerArgs = ["nogui"]
#MinecraftServerName = "server1"

