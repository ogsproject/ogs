
import unittest, json, os
from MinecraftServerManager import ConfigObject

class ConfigTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not os.path.isdir("data_test"):
            os.mkdir("data_test")

    def test_load_0(self):
        filePath = "data_test/test.json"
        with open(filePath, "w") as f:
            json.dump({
                }, f)
        config = ConfigObject.Config(filePath)
        config.load()

    def test_load_0(self):
        filePath = "data_test/test.json"
        with open(filePath, "w") as f:
            json.dump({
                "test0" : 0,
                "test1" : 1
                }, f)
        config = ConfigObject.Config(filePath)
        config.load()
        self.assertEqual(config.get("test0"), 0)
        self.assertEqual(config.get("test1"), 1)



class ConfigElementTest(unittest.TestCase):

    def test_init_1(self):
        config = ConfigObject.ConfigElement({})
        self.assertEqual(len(config.toDict().keys()), 0)

    def test_init_2(self):
        config = ConfigObject.ConfigElement({"test":0})
        self.assertEqual(len(config.toDict().keys()), 1)

    def test_init_3(self):
        config = ConfigObject.ConfigElement({
            "test" : 0,
            "test1" : 1
                })
        self.assertEqual(len(config.toDict().keys()), 2)

    def test_init_4(self):
        config = ConfigObject.ConfigElement({
            "test" : 0,
            "test1" : {
                "test" : 0
                }})
        self.assertEqual(len(config.toDict().keys()), 2)
        self.assertEqual(len(config.get("test1").toDict().keys()), 1)

    def test_get_0(self):
        config = ConfigObject.ConfigElement({"test":0})
        self.assertEqual(config.get("test"), 0)

    def test_get_1(self):
        config = ConfigObject.ConfigElement({
            "test" : 0,
            "test1" : {
                "test2": {
                    "test3" : 3
                    }}})
        self.assertEqual(config.get("test1", "test2", "test3"), 3)

    def test_get_2(self):
        config = ConfigObject.ConfigElement({
            "test" : 0,
            "test1" : {
                "test2": {
                    "test3" : 3
                    }}})
        self.assertEqual(config.get("test"), 0)


    def test_get_3(self):
        config = ConfigObject.ConfigElement({
            "test" : 0,
            "test1" : {
                "test2": {
                    "test3" : 3
                    }}})
        self.assertRaises(Exception, config.get, "test", "test1", "test2")

    def test_get_4(self):
        config = ConfigObject.ConfigElement({
            "test" : 0,
            "test1" : [
                0,
                1,
                2
                ]})
        self.assertEqual(config.get("test1")[0], 0)

    def test_get_5(self):
        config = ConfigObject.ConfigElement({
            "test" : 0,
            "test1" : [
                {"test0" : 0},
                {"test1" : 1}
                ]})
        self.assertEqual(type(config.get("test1")[0]), ConfigObject.ConfigElement)

    def test_get_5(self):
        config = ConfigObject.ConfigElement({
            "test" : 0,
            "test1" : [
                {"test0" : 0},
                {"test1" : 1}
                ]})
        self.assertEqual(config.get("test"), 0)
        config.set("test", value = 1)
        self.assertEqual(config.get("test"), 1)
