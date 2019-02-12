import os

from OpenGameServer import ConfigObject
from OpenGameServer.plugins.minecraft import MinecraftServer

game = "minecraft"


def init(manager):
    pass

def get(config):
    if not "maxMemory" in config.keys():
        config["maxMemory"] =  "512M"
    if not "startMemory" in config.keys():
        config["startMemory"] = "512M"
    if not "version" in config.keys():
        config["version"] = "1.13.2"
    if not "launchArgs"in config.keys():
        config["launchArgs"] = ["nogui"]

    server = MinecraftServer.MinecraftServer(config)
    return server

