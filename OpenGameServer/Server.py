import os

class Server():
    def __init__(self, config):
        self.config = config

    def isConfigured(self):
        raise NotImplementedError()

    def create(self, manager):
        if self.isConfigured():
            raise Exception("Server already exists")

        if not os.path.exists(self.workingDirectory):
            os.mkdir(self.workingDirectory)

    def start(self):
        if not self.isConfigured():
            raise Exception("Server not configured")

    def stop(self):
        if not self.isConfigured():
            raise Exception("Server not configured")
    
    def sendCommand(self, command):
        if not self.isConfigured():
            raise Exception("Server not configured")

    def getSupportedCommand(self):
        return []

    @property
    def workingDirectory(self):
        return self.config["workingDirectory"].get()
