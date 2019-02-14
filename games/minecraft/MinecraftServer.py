import os

from OpenGameServer import Server
from OpenGameServer import Downloader


class MinecraftServer(Server.Server):
    def __init__(self, game, config):
        self.game = game
        Server.Server.__init__(self, config)

    def create(self, manager):
        downloadedFile = Downloader.getFileFromUrl(self.game.ServerVersionURL["1.13.2"])
        jarFile = os.path.join(self.workingDirectory, "server.jar")
        with open(jarFile, "wb") as f:
            f.write(downloadedFile.read())
