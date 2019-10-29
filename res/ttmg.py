from urllib.request import *
import os
from lxml.etree import XML

def updateCheck(self, Version):
    class UpdateChecker(object):
      
      def __init__(self):
          getMessage = self.getMessage
          getVersion = self.getVersion

      def getVersion(self, currentTag):
          url = self.URL
          update = urlopen(url).read()
          root = XML(update)
          cur_version = root.find(".//"+currentTag)
          current = cur_version.text
          return current

      def getMessage(self, messageTag):
          url = self.URL
          update = urlopen(url).read()
          root = XML(update)
          mess = root.find(".//"+messageTag)
          message = mess.text
          return message

    check = UpdateChecker()
    check.URL = "https://raw.githubusercontent.com/biplobsd/Google-Colab-CloudTorrent/master/update.xml"
    currentVersion = check.getVersion("currentVersion")
    message = check.getMessage("message")

    if Version != currentVersion:
        print("Script Update Checker: Version "+currentVersion+" "+message+" Your version: "+Version+"")
        display(HTML('<div style="background-color: #4caf50!important;text-align: center;padding-top:-1px;padding-bottom: 9px;boder:1px"><h4 style="padding-top:5px"><a target="_blank" href="http://bit.ly/updateCscript" style="color: #fff!important;text-decoration: none;color: inherit;background-color:transparent;font-family: Segoe UI,Arial,sans-serif;font-weight: 400;font-size: 20px;">Open Latest Version</a></h4></div>'))
        os.system('kill -9 -1')
    else:
        print("Script Update Checker: Your script is up to date")
