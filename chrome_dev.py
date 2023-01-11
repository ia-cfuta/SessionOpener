#!venv/bin/python3

#from .manager import Manager

from framework.util.manager import Manager
from time import sleep

manager = Manager()

manager.startBrowser(deviceIP='localhost', devicePort='8188')
manager.clickNewTabButton()
#manager.addSession()
#manager.removeSession()
#manager.addSession()

sleep(8)
manager.terminate()