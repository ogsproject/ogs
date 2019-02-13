import unittest, json, os
from OpenGameServer import Downloader


class DownloaderTest(unittest.TestCase):

    def test_download(self):
        Downloader.getFileFromUrl("https://www.google.com")

