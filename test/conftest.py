import unittest, shutil
import ogs


def pytest_sessionstart(session):
    ogs.GlobalConfig.ConfigPath = "run_test/etc/ogs"
    ogs.GlobalConfig.DataPath = "run_test/data"
    ogs.GlobalConfig.ServersConfigPath = "run_test/servers/config"
    ogs.GlobalConfig.ServersDataPath = "run_test/servers/data"
    ogs.GlobalConfig.init()

def pytest_sessionfinish(session, exitstatus):
    shutil.rmtree("run_test")
