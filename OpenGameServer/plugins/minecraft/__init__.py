import os

from OpenGameServer import ConfigObject
from OpenGameServer.plugins.minecraft import MinecraftServer

game = "minecraft"

def init(manager):
    config = ConfigObject.ConfigDict({
        "ServerVersionURL" : {
                "1.13.2" : "https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"
            }
        })

    manager.config["Minecraft"] = config

def get(config):
    if not "maxMemory" in config.keys():
        config["maxMemory"] =  "512M"
    if not "startMemory" in config.keys():
        config["startMemory"] = "512M"
    if not "version" in config.keys():
        config["version"] = "1.13.2"
    if not "launchArgs"in config.keys():
        config["launchArgs"] = ["nogui"]

    return MinecraftServer.MinecraftServer(config)

