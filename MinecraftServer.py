
import subprocess, threading, time, os, shutil
import MinecraftServerConfiguration

JavaBinPath = "/usr/bin/java"
MinecraftServerJarPath = "server.jar"
SourceMinecraftServerJarPath = "server.jar"
MinecraftServerArgs = ["nogui"] 
MinecraftServerName = "server1"

class MinecraftServerWatcher(threading.Thread):
    def __init__(self, server):
        threading.Thread.__init__(self)
        self.server = server

    def run(self):
        pass

class MinecraftServerListener(threading.Thread):
    def __init__(self, server):
        threading.Thread.__init__(self)
        self.server = server

    def run(self):
        while True:
            line = self.server.process.stdout.readline().strip()

class MinecraftServer():
    def __init__(self, name, directory = None, startMemory = "1024M", maxMemory = "1024M"):
        self.name = name
        self.maxMemory = maxMemory
        self.startMemory = startMemory
        self.process = None
        self.watcher = None
        self.listener = None

        if directory == None:
            self.workingDirectory = self.name
        else:
            self.workingDirectory = directory

        self.configFilePath = os.path.join(self.workingDirectory, "server.properties")
        self.eulaPath = os.path.join(self.workingDirectory, "eula.txt")

    def loadConfig(self):
        self.config = MinecraftServerConfiguration.MinecraftServerConfiguration(self.configFilePath)

    def isConfigured(self):
        return os.path.exists(self.configFilePath)

    def create(self):
        if self.isConfigured():
            raise Exception("Server already exists")

        os.mkdir(self.workingDirectory)
        shutil.copy2(SourceMinecraftServerJarPath, self.workingDirectory)

        args = []
        args.append(JavaBinPath)
        args.append("-jar")
        args.append(MinecraftServerJarPath)
        for a in MinecraftServerArgs:
          args.append(a)

        process = subprocess.Popen(args,
                executable = None,
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                cwd = self.workingDirectory,
                env = None,
                universal_newlines = True)

        process.wait()
        self.acceptEula()

    def run(self):
        args = []
        args.append(JavaBinPath)
        args.append("-Xmx" + self.maxMemory)
        args.append("-Xms" + self.startMemory)
        args.append("-jar")
        args.append(MinecraftServerJarPath)
        for a in MinecraftServerArgs:
          args.append(a)

        self.process = subprocess.Popen(args,
                executable = None,
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                cwd = self.workingDirectory,
                env = None,
                universal_newlines = True)

        self.watcher = MinecraftServerWatcher(self)
        self.listener = MinecraftServerListener(self)
        self.watcher.start()
        self.listener.start()

    def sendCommand(self, command):
        self.process.stdin.write(command + "\n")
        self.process.stdin.flush()

    def acceptEula(self):
        text = None
        with open(self.eulaPath, "r") as f:
            text = f.read()

        if not "eula" in text:
            raise Exception("eula file is not valid")

        text = text.replace("eula=false", "eula=true")
        with open(self.eulaPath, "w") as fw:
            fw.write(text)
            fw.flush()

