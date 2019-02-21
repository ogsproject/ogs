#! /usr/bin/env python3

import unittest, shutil
import ogs
import test.conftest

def suite():
    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('test', pattern='*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    ogs.GlobalConfig.ConfigPath = "run_test/etc/ogs"
    ogs.GlobalConfig.DataPath = "run_test/data"
    ogs.GlobalConfig.ServersConfigPath = "run_test/servers/config"
    ogs.GlobalConfig.ServersDataPath = "run_test/servers/data"
    ogs.GlobalConfig.init()

    runner = unittest.TextTestRunner()
    runner.run(suite())

    shutil.rmtree("run_test")
