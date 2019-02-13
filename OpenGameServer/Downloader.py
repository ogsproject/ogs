import os, datetime, urllib
from urllib import request, parse

class DownloadingFile(object):
    def __init__(self, stream, filePath):
        self.stream = stream
        self.filePath = filePath
        self.outStream = open(filePath, "wb")

    def read(self):
        self.outStream.write(self.stream.read())
        self.outStream.flush()
        self.outStream.close()
        return open(self.filePath, "rb").read()

def getFileFromUrl(url):
    filePath = "test.download"
    #nosec
    parsedUrl = parse.urlparse(url)
    if parsedUrl.scheme != "https" and parsedUrl.scheme != "http":
        raise Exception("unsupported scheme")
    response = request.urlopen(url)
    urlDate = datetime.datetime.strptime(response.headers["Last-Modified"], '%a, %d %b %Y %H:%M:%S GMT')
    urlDate = urlDate.replace(tzinfo = datetime.timezone.utc).astimezone(tz=None)
    needToDownload = True

    if not os.path.exists(filePath):
        needToDownload = True
    else:
        fileDate = datetime.datetime.fromtimestamp(os.path.getmtime(filePath) )
        fileDate = fileDate.replace(tzinfo = None).astimezone(tz=None)
        needToDownload = urlDate > fileDate

    if needToDownload:
        return DownloadingFile(response, filePath)
    else:
        return open(filePath, "rb")

