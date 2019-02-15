import os

import ogs


class MinecraftServer(ogs.Server):
    def __init__(self, game, config):
        self.game = game
        ogs.Server.__init__(self, config)

    def create(self, manager):
        downloadedFile = ogs.FileManager.getFileFromUrl(self.game.ServerVersionURL["1.13.2"])
        jarFile = os.path.join(self.workingDirectory, "server.jar")
        with open(jarFile, "wb") as f:
            f.write(downloadedFile.read())
