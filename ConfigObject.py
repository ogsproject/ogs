import json


class ConfigElement:
    def __init__(self, data):
        self.__data = data
        for k in self.__data.keys():
            if type(self.__data[k]) is dict:
                self.__data[k] = ConfigElement(self.__data[k])

    def get(self, args):
        current = self.__data
        for k in args:
            current = current[k]
        return current

    def update(self, source):
        self.__update(source, self)

    def __update(self, source, dest):
        for k in dest.__data.keys():
            if type(dest.__data[k]) is ConfigElement:
                dest.__data[k].update(source[k])
        source.update(dest.__data)

class Config:
    def __init__(self, filePath, baseDict):
        self.filePath = filePath
        self.__baseDict = baseDict
        self.__element = ConfigElement(baseDict)

    def load(self):
        with open(self.filePath, "r") as f:
            jsondict = json.load(f)
            self.__validateLoadedDict(jsondict, self.__baseDict)
            self.__element.update(jsondict)

    def get(self, *args):
        return self.__element.get(args)

    def save(self):
        with open(self.filePath, "w") as f:
            json.dump(self.__dict, f, sort_keys=True, indent=4)
    
    def __validateLoadedDict(self, loadedDict, baseDict, currentTree = ""):
        pass
#        for k in loadedDict:
#            if not k in baseDict.keys():
#                raise Exception("Invalid key \"%s\" in config file \"%s\"" % (currentTree + "." + k, self.filePath))
#            if type(loadedDict[k]) is dict:
#                self.__validateLoadedDict(loadedDict[k], baseDict[k], currentTree + "." + k)

