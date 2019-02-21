import os

class Server():
    def __init__(self, config):
        self.config = config
        self.supportedCommand = []
        self.supportedProperties = []

    def pre_create(self):
        if not os.path.exists(self.workingDirectory):
            os.mkdir(self.workingDirectory)

    def create(self, manager):
        raise NotImplementedError()

    def post_create(self):
        pass

    def pre_start(self):
        pass

    def start(self):
        raise NotImplementedError()

    def post_start(self):
        pass

    def pre_stop(self):
        pass

    def stop(self):
        raise NotImplementedError()

    def post_stop(self):
        pass

    def getSupportedCommand(self):
        return self.supportedCommand

    def sendCommand(self, command):
        raise NotImplementedError()

    def getSupportedProperties(self):
        return self.supportedProperties

    def setProperty(self, name, value):
        raise NotImplementedError()

    @property
    def workingDirectory(self):
        return self.config["workingDirectory"].get()
