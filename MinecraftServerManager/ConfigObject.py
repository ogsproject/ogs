import json


class ConfigElement:
    def __init__(self, sourceDict):
        self.__data = {}
        self.update(sourceDict)

    def update(self, sourceDict):
        self.__data.update(sourceDict)
        for k in sourceDict.keys():
            if type(sourceDict[k]) is dict:
                self.__data[k] = ConfigElement(sourceDict[k])

    def toDict(self):
        returnValue = {}
        returnValue.update(self.__data)
        for k in self.__data.keys():
            if type(self.__data[k]) is ConfigElement:
                returnValue[k] = self.__data[k].toDict()
        return returnValue

    def get(self, *args):
        current = None
        nb = 0
        for k in args:
            nb = nb + 1
            if current == None:
                current = self.__data[k]
                continue

            if type(current) is ConfigElement:
                current = current.__data[k]
            else:
                break

        if nb < len(args):
            raise Exception("Object not a ConfigElement")

        return current



class Config:
    def __init__(self, filePath, baseDict):
        self.filePath = filePath
        self.__element = ConfigElement(baseDict)

    def load(self):
        pass
#        with open(self.filePath, "r") as f:
#            jsondict = json.load(f)
#            self.__validateLoadedDict(jsondict, self.__baseDict)
#            self.__element.update(jsondict)

    def get(self, *args):
        return self.__element.get(*args)

    def save(self):
        with open(self.filePath, "w") as f:
            json.dump(self.__element.toDict(), f, sort_keys=True, indent=4)
    
    def __validateLoadedDict(self, loadedDict, baseDict, currentTree = ""):
        pass
#        for k in loadedDict:
#            if not k in baseDict.keys():
#                raise Exception("Invalid key \"%s\" in config file \"%s\"" % (currentTree + "." + k, self.filePath))
#            if type(loadedDict[k]) is dict:
#                self.__validateLoadedDict(loadedDict[k], baseDict[k], currentTree + "." + k)

