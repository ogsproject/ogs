import unittest
from OpenGameServer import Downloader


class DownloaderTest(unittest.TestCase):

    def test_download(self):
        Downloader.getFileFromUrl("https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game")

