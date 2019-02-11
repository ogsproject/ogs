from OpenGameServer import Server


class MinecraftServer(Server.Server):
    def __init__(self, config):
        Server.Server.__init__(self, config)

    def isConfigured(self):
        print(self.config)
