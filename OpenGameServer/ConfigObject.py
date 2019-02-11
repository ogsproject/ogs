import json, os

def toConfigElement(data):
    if issubclass(type(data), ConfigElement):
        return data

    if type(data) == int or\
            type(data) == bool or\
            type(data) == str or\
            type(data) == float:
                return ConfigScalar(data)

    if type(data) == list:
        return ConfigList(data)

    if type(data) == dict:
        return ConfigDict(data)

    raise ConfigException("Unsuported type")


class ConfigException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

class ConfigElement(object):
    def __init__(self):
        self.default = True
        self.parent = None
        self.config = None
        pass

    def toJson(self):
        raise NotImplementedError

    def set(self, data, default = False):
        raise NotImplementedError

    def postSet(self):
        if self.config != None:
            self.config.autoSave()

    def get(self):
        raise NotImplementedError

    def __str__(self):
        return json.dumps(self.toJson(), sort_keys=True, indent=4)

"""
"""
class ConfigScalar(ConfigElement):
    def __init__(self, data, description = None):
        ConfigElement.__init__(self)
        self.__description = description
        self.set(data, True)

    def set(self, data, default = False):
        if type(data) != int and\
            type(data) != bool and\
            type(data) != str and\
            type(data) != float:
                raise ConfigException("")
        self.__data = data
        self.default = default
        if not default:
            ConfigElement.postSet(self)

    def get(self):
        return self.__data

    def toJson(self):
        return self.__data

"""
"""
class ConfigDict(ConfigElement):
    def __init__(self, data, description = None):
        ConfigElement.__init__(self)
        self.set(data, True)

    def set(self, data, default = False):
        if not type(data) == dict:
            raise ConfigException("Not a dict")
        self.__data = {}
        for k in data.keys():
            element = toConfigElement(data[k])
            element.default = default
            element.parent = self
            element.config = self.config
            self.__data[k] = element
        if not default:
            ConfigElement.postSet(self)

    def toJson(self):
        result = {}
        for k in self.__data:
            result[k] = self.__data[k].toJson()
        return result

    def keys(self):
        return self.__data.keys()

    def get(self):
        returnValue = {}
        for k in self.__data.keys():
            returnValue[k] = self.__data[k].get()
        return returnValue

    def __getitem__(self, key):
        return self.__data[key]

    def __setitem__(self, k, v):
        element = toConfigElement(v)
        self.__data[k] = element
        element.default = False
        element.parent = self
        element.config = self.config
        ConfigElement.postSet(self)


"""
"""
class ConfigList(ConfigElement):
    def __init__(self, data = [], description = None):
        ConfigElement.__init__(self)
        self.set(data, True)

    def append(self, data):
        self.__data.append(toConfigElement(data))
        ConfigElement.postSet(self)

    def set(self, data, default = False):
        if not type(data) == list:
            raise ConfigException("Not a list")
        self.__data = []
        for e in data:
            element = toConfigElement(e)
            element.default = default
            element.parent = self
            element.config = self.config
            self.append(element)
        if not default:
            ConfigElement.postSet(self)

    def get(self):
        returnValue = []
        for k in self.__data:
            returnValue.append(k.get())
        return returnValue

    def toJson(self):
        result = []
        for a in self.__data:
            result.append(a.toJson())
        return result

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__data):
            result = self.__data[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.__data[key]


"""
"""
class Config(object):
    def __init__(self, filePath, configElement = None):
        self.filePath = filePath
        self.element = configElement
        self.element.config = self
        self.autoSaveEnabled = True
        self.preSaveCallback = []

    def load(self):
        with open(self.filePath, "r") as f:
            jsondict = json.load(f)
            self.element.set(jsondict, False)

    def save(self):
        for f in self.preSaveCallback:
            f()
        os.makedirs(os.path.dirname(self.filePath), exist_ok=True)
        with open(self.filePath, "w") as f:
            json.dump(self.element.toJson(), f, sort_keys=True, indent=4)
    
    def autoSave(self):
        if self.autoSaveEnabled:
            self.save()
