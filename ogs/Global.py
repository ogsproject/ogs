import os

from .Config import ConfigElement, ConfigDict, Config


class Global(object):
    def __init__(self):
        self.initialized = False
        self.ConfigPath = "run/etc/ogs"
        self.ConfigFileName = "global.json"

        self.config = ConfigDict({
            "DataPath" : "run/data",
            "ServersConfigPath" : "run/servers/config",
            "ServersDataPath" : "run/servers/data"
        })

    def init(self):
        self.initialized = True
        os.makedirs(self.DataPath, mode=0o777, exist_ok = True)
        os.makedirs(self.ServersConfigPath, mode=0o777, exist_ok = True)
        os.makedirs(self.ServersDataPath, mode=0o777, exist_ok = True)

        self.ConfigFilePath = os.path.join(self.ConfigPath, self.ConfigFileName)
        self.configFile = Config(self.ConfigFilePath, self.config)
        if not os.path.exists(self.configFile.filePath):
            self.configFile.save()
        else:
            self.configFile.load()

    @property
    def DataPath(self):
        if not self.initialized:
            raise Exception("Not initialized")
        return self.config["DataPath"].get()

    @DataPath.setter
    def DataPath(self, value):
        return self.config["DataPath"].set(value)

    @property
    def ServersConfigPath(self):
        if not self.initialized:
            raise Exception("Not initialized")
        return self.config["ServersConfigPath"].get()

    @ServersConfigPath.setter
    def ServersConfigPath(self, value):
        return self.config["ServersConfigPath"].set(value)

    @property
    def ServersDataPath(self):
        if not self.initialized:
            raise Exception("Not initialized")
        return self.config["ServersDataPath"].get()

    @ServersDataPath.setter
    def ServersDataPath(self, value):
        return self.config["ServersDataPath"].set(value)

GlobalConfig = Global()


