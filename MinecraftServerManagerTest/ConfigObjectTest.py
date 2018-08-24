
import unittest
from MinecraftServerManager import ConfigObject

class ConfigObjectTest(unittest.TestCase):

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
