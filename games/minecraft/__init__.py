import os, sys
import ogs

__version__ = "1.0.0"
__title__ = "minecraft"


from . import MinecraftServer


class Minecraft(ogs.Game):
    name = "minecraft"

    def __init__(self):
        self.ServerVersionURL = {
            "1.13.2" : "https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"
        }

    def getServer(self, config):
        if not "maxMemory" in config.keys():
            config["maxMemory"] =  "512M"
        if not "startMemory" in config.keys():
            config["startMemory"] = "512M"
        if not "version" in config.keys():
            config["version"] = "1.13.2"
        if not "launchArgs"in config.keys():
            config["launchArgs"] = ["nogui"]
        server = MinecraftServer.MinecraftServer(self, config)
        return server

def getGame():
    return Minecraft()


