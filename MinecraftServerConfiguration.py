
# use inotify to watch config file

class MinecraftServerConfiguration():
    def __init__(self, filePath):

        self.conf = {
                "max-tick-time":
                    [None, None, ""],
                "generator-settings": [None, None, ""],
                "force-gamemode": [None, None, ""],
                "allow-nether": [None, None, ""],
                "enforce-whitelist": [None, None, ""],
                "gamemode": [None, None, ""],
                "enable-query": [None, None, ""],
                "player-idle-timeout": [None, None, ""],
                "difficulty": [None, None, ""],
                "spawn-monsters": [None, None, ""],
                "op-permission-level": [None, None, ""],
                "pvp": [None, None, ""],
                "snooper-enabled": [None, None, ""],
                "level-type": [None, None, ""],
                "hardcore": [None, None, ""],
                "enable-command-block": [None, None, ""],
                "max-players": [None, None, ""],
                "network-compression-threshold": [None, None, ""],
                "resource-pack-sha1": [None, None, ""],
                "max-world-size": [None, None, ""],
                "server-port": [None, None, ""],
                "server-ip": [None, None, ""],
                "spawn-npcs": [None, None, ""],
                "allow-flight": [None, None, ""],
                "level-name": [None, None, ""],
                "view-distance": [None, None, ""],
                "resource-pack": [None, None, ""],
                "spawn-animals": [None, None, ""],
                "white-list": [None, None, ""],
                "generate-structures": [None, None, ""],
                "online-mode": [None, None, ""],
                "max-build-height": [None, None, ""],
                "level-seed": [None, None, ""],
                "prevent-proxy-connections": [None, None, ""],
                "use-native-transport": [None, None, ""],
                "motd": [None, None, ""],
                "enable-rcon": [None, None, ""]
                }

        self.filePath = filePath
        self.load()


    def load(self):
        with open(self.filePath, "r") as f:
            for l in f.readlines():
                line = l.strip()
                if not line.startswith("#"):
                    keyValue = line.split("=")
                    key = keyValue[0]
                    value = keyValue[1]
                    self.setConfig(key, value)

    def setConfig(self, key, value):
        if key not in self.conf:
            self.conf[key] = [None, None, ""]
        self.conf[key][1] = value

    def save(self):
        with open(self.filePath, "w") as f:
            for key in self.conf.keys():
                if self.conf[key][1] != None:
                    f.write("%s=%s" % (key, self.conf[key][1]))

