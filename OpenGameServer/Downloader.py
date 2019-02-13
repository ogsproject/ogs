import os, datetime, base64
from urllib import request, parse
from OpenGameServer import Global

class DownloadingFile(object):
    def __init__(self, stream, filePath):
        self.stream = stream
        self.filePath = filePath
        self.outStream = open(filePath, "wb")

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        self.close()

    def read(self):
        self.outStream.write(self.stream.read())
        self.outStream.flush()
        self.outStream.close()
        self.outStream = open(self.filePath, "rb").read()
        return self.outStream

    def close(self):
        self.outStream.close()


def getFileFromUrl(url):
    downloadDir = os.path.join(Global.config.DataPath, "download")
    os.makedirs(downloadDir, mode = 0o777, exist_ok = True)

    filename = str(base64.b64encode(bytes(url, "utf8")).decode("utf8"))
    filePath = os.path.join(Global.config.DataPath, "download", filename)
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

