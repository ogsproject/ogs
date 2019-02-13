
import unittest, json, os
from OpenGameServer import ConfigObject


class ConfigElementTest(unittest.TestCase):

    def test_scalar_2(self):
        config = ConfigObject.ConfigScalar("test")
        self.assertEqual(config.get(), "test")
        config.set("allo")
        self.assertEqual(config.get(), "allo")

    def test_scalar_3(self):
        config = ConfigObject.ConfigScalar(True)
        self.assertEqual(config.get(), True)
        config.set(False)
        self.assertEqual(config.get(), False)

    def test_scalar_4(self):
        config = ConfigObject.ConfigScalar(1)
        self.assertEqual(config.get(), 1)

    def test_scalar_5(self):
        config = ConfigObject.ConfigScalar(1)
        config.set(True)
        self.assertTrue(config.get())

    def test_scalar_6(self):
        config = ConfigObject.ConfigScalar(1)
        with self.assertRaises(ConfigObject.ConfigException):
            config.set([10,10])

    def test_scalar_7(self):
        config = ConfigObject.ConfigScalar(1)
        config.set(True)
        self.assertTrue(config.get())

    def test_list_1(self):
        with self.assertRaises(ConfigObject.ConfigException):
            config = ConfigObject.ConfigList(1)

    def test_list_2(self):
        config = ConfigObject.ConfigList([])
        config.set([
            ConfigObject.ConfigScalar(1)
        ])
        self.assertEqual(config[0].get(), 1)

    def test_list_3(self):
        config = ConfigObject.ConfigList([])
        config.set([0,1,2,3,4])
        a = []
        for i in config:
            a.append(i.get())

        self.assertEqual(a[0], 0)
        self.assertEqual(a[1], 1)
        self.assertEqual(a[2], 2)
        self.assertEqual(a[3], 3)
        self.assertEqual(a[4], 4)

    def test_list_4(self):
        config = ConfigObject.ConfigList([1,2,3,4])
        with self.assertRaises(TypeError):
            config[0] = 10

    def test_list_4(self):
        config = ConfigObject.ConfigList([])
        config.set([0,1])
        config[0].set(10)
        self.assertEqual(config[0].get(), 10)

    def test_list_5(self):
        config = ConfigObject.ConfigList([1,2,3,4])
        self.assertEqual(config.toJson(), [1,2,3,4])

    def test_dict_1(self):
        with self.assertRaises(ConfigObject.ConfigException):
            config = ConfigObject.ConfigDict(1)
    
    def test_dict_2(self):
        config = ConfigObject.ConfigDict({"test": 1})
        self.assertEqual(config["test"].get(), 1)

    def test_dict_3(self):
        config = ConfigObject.ConfigDict({"test": 1})
        config["test"].set(10)
        self.assertEqual(config["test"].get(), 10)

    def test_dict_4(self):
        config = ConfigObject.ConfigDict({"test": 1})
        self.assertEqual(config.toJson(), {"test":1})

    def test_toJson_1(self):
        config = ConfigObject.ConfigDict({"test": 1})
        strJson = json.dumps(config.toJson())
        loadJson = json.loads(strJson)
        configLoaded = ConfigObject.toConfigElement(loadJson)
        self.assertEqual(config["test"].get() , 1)


