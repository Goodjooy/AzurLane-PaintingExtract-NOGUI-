import tools.autoload
import os
import time


def test():
    name = input("name:")
    path = os.getcwd()
    unity = path + "\\UnityStudio\\UnityStudio.exe"
    os.system("start " + unity)
    time.sleep(3)
    tools.autoload.load_file(["%s\\painting\\%s" % (path, name)], path)
