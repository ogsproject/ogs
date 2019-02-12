from OpenGameServer import Server
from OpenGameServer import Downloader


class MinecraftServer(Server.Server):
    ServerVersionURL = {
                "1.13.2" : "https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"
            }

    
    def __init__(self, config):
        Server.Server.__init__(self, config)

    def create(self, config):
        downloadedFile = Downloader.getFileFromUrl(self.ServerVersionURL["1.13.2"])
        with open("server.ar", "wb") as f:
            f.write(downloadedFile.read())
        
