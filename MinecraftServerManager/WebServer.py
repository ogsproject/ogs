from flask import Flask
import MinecraftServerManager
import Global

app = Flask(__name__)
minecraftServerManager = MinecraftServerManager.MinecraftServerManager(Global.MinecraftServerManagerConfigPath)

@app.route('/')
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host=minecraftServerManager.config.dict["server"]["host"],
            port=minecraftServerManager.config.dict["server"]["port"])
