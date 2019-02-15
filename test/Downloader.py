#! /usr/bin/env python3

import unittest

if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import ogs


class DownloaderTest(unittest.TestCase):

    def test_download(self):
        with ogs.FileManager.getFileFromUrl("https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game"):
            pass

if __name__ == "__main__":
    ogs.Global.GlobalConfig.init()
    unittest.main()

