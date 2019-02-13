import os
from OpenGameServer import ConfigObject

# directory 

class Global(object):
    def __init__(self):
        self.ConfigPath = "run/etc/ogs"
        self.ConfigFileName = "global.json"
        self.ConfigFilePath = os.path.join(self.ConfigPath, self.ConfigFileName)

        self.config =ConfigObject.ConfigDict({
            "DataPath" : "run/data",
            "ServersConfigPath" : "run/servers/config",
            "ServersDataPath" : "run/servers/data"
        })

        self.configFile = ConfigObject.Config(self.ConfigFilePath, self.config)
        if not os.path.exists(self.configFile.filePath):
            self.configFile.save()
        else:
            self.configFile.load()

        os.makedirs(self.DataPath, mode=0o777, exist_ok = True)
        os.makedirs(self.ServersConfigPath, mode=0o777, exist_ok = True)
        os.makedirs(self.ServersDataPath, mode=0o777, exist_ok = True)



    @property
    def DataPath(self):
        return self.config["DataPath"].get()

    @property
    def ServersConfigPath(self):
        return self.config["ServersConfigPath"].get()

    @property
    def ServersDataPath(self):
        return self.config["ServersDataPath"].get()

config = Global()


