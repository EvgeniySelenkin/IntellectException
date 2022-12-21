import traceback
import re
import json


class IntellectException:
    def __init__(self, file_config_name):
        config = []
        with open(file_config_name, 'r') as f:
            config = json.load(f)
        self.tree = {}
        for elem in config:
            self.tree[elem[0]] = {}

        for elem in config:
            self.tree[elem[0]][elem[1]] = {}

        for elem in config:
            self.tree[elem[0]][elem[1]][hash(elem[2])] = elem[3]
    def printException(self, trace):
        file_name = re.search('".+"', trace.split("\n")[1]).group(0)[1:-1]
        line = re.search("line \d+", trace.split("\n")[1]).group(0)[5:]
        exception = trace.split("\n")[-2].strip()
        print(self.tree[file_name + ' ' + line][exception][hash(trace)])
  
e = IntellectException('config.json')

try:
    raise TypeError()
except:
    e.printException(traceback.format_exc())

try:
    raise NameError()
except:
    e.printException(traceback.format_exc())

try:
    raise ZeroDivisionError()
except:
    e.printException(traceback.format_exc())

try:
    raise Exception("Custom")
except:
    e.printException(traceback.format_exc())
