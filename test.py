#! /usr/bin/env python3

import unittest, shutil
from OpenGameServer import Global

def suite():
    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('test', pattern='*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    Global.config.ConfigPath = "run_test/etc/ogs"
    Global.config.DataPath = "run_test/data"
    Global.config.ServersConfigPath = "run_test/servers/config"
    Global.config.ServersDataPath = "run_test/servers/data"
    Global.config.init()

    runner = unittest.TextTestRunner()
    runner.run(suite())

    shutil.rmtree("run_test")
