import unittest
from OpenGameServer import FileManager


class DownloaderTest(unittest.TestCase):

    def test_download(self):
        with FileManager.getFileFromUrl("https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game"):
            pass

