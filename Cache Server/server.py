from flask import Flask, send_file
import threading
import time as time2
from urllib.request import urlopen
from werkzeug.routing import BaseConverter
import os

cacheDir = '/tmp/cache/'
originServer = '52.177.9.49'
originPort = 80
PORT = 80
MAX_TIME_ON_CACHE = 60

if not os.path.isdir(cacheDir):
    os.mkdir(cacheDir)

cachedItems = {}


def aging_fn():
    while True:
        list_to_remove = []
        for item in cachedItems:
            cachedItems[item] -= 1
            if cachedItems[item] == 0:
                list_to_remove.append(item)
        for i in list_to_remove:
            print("removed item " + i)
            cachedItems.pop(i)
        time2.sleep(1)


app = Flask(__name__)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route('/<regex(".*"):path>')
def receiver(path):
    path = str(path)
    path2 = path.replace("/", "+")

    if not path2:
        path2 = "index.html"

    if path2 in cachedItems:
        print("sending cached file " + path)
        return send_file(cacheDir + path2)

    r = urlopen('http://' + originServer + ":" + str(originPort) + "/" + path).read()
    f = open(cacheDir + path2, 'wb')
    f.write(r)
    f.close()
    cachedItems[path2] = MAX_TIME_ON_CACHE
    print("cached file " + path)
    return send_file(cacheDir + path2)


if __name__ == '__main__':
    aging = threading.Thread(target=aging_fn, args=(), daemon=True)
    aging.start()
    app.run(host='0.0.0.0', port=PORT)
