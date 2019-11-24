import os
from IPython.core.magic import *
from urllib.request import *
from sys import exit as exx, path as s_p
from IPython.display import HTML, clear_output

from lxml.etree import XML

def nameport(TOKEN, AUTO, PORT=10001):
  tokens = {}
  def selectApi(api):
    try:
        return tokens[api]
    except:
        return "Invalid Token"

  if AUTO:
    USR_Api = "mnc"
    tokens = {
        "ddn": "6qGnEsrCL4GqZ7hMfqpyz_7ejAThUCjVnU9gD5pbP5u",
        "tdn": "1Q4i7F6isO7zZRrrjBKZzZhwsMu_74yJqoEs1HrJh1zYyxNo1",
        "mnc": "1SCsbuawjv9d79jlhlfNljaFTaB_5heVkcR6C7Sk8UBaQ1U1C",
        "api001": "1Q3zMbZhIunjp92RvrZpnyuJxZL_3V3JUziX5Dp1sQbTMAPrr",
        "api002": "1Q45NXgsx6oyusN3GiNAYvkNJPS_AveYUDBcPHsvRvf21WZv",
        "api003": "1Q6smHt4Bzz9VEXTwj3a7p5Gdx2_5mp6ivT6N6nB3YmRHUEM3",
    }
  elif not TOKEN:
    print("Copy authtoken from https://dashboard.ngrok.com/auth")
    __temp = %sx read -p "Token :"
    tokens['your'] = __temp[0].split(':')[1]
    USR_Api = "your"
  else:
    USR_Api = "mind"
    tokens["mind"] = TOKEN


  return selectApi(USR_Api), PORT

def checkAvailable(path_="", userPath=False):
    from os import path as _p

    if path_ == "":
        return False
    else:
        return (
            _p.exists(path_)
            if not userPath
            else _p.exists(f"/usr/local/sessionSettings/{path_}")
        )

def accessSettingFile(file="", setting={}):
    from json import load, dump

    if not isinstance(setting, dict):
        print("Only accept Dictionary object.")
        exx()
    fullPath = f"/usr/local/sessionSettings/{file}"
    try:
        if not len(setting):
            if not checkAvailable(fullPath):
                print(f"File unavailable: {fullPath}.")
                exx()
            with open(fullPath) as jsonObj:
                return load(jsonObj)
        else:
            with open(fullPath, "w+") as outfile:
                dump(setting, outfile)
    except:
        print(f"Error accessing the file: {fullPath}.")


def createButton(name, *, func=None, style="", icon="check"):
    import ipywidgets as widgets

    button = widgets.Button(
        description=name, button_style=style, icon=icon, disabled=not bool(func)
    )
    button.style.font_weight = "900"
    button.on_click(func)
    output = widgets.Output()
    display(button, output)

def displayUrl(data, buRemote, reset):
    clear_output(wait=True)
    print(f'Web UI: {data["url"]} : {data["port"]}')
    if "surl" in data.keys():
        print(f'Web UI (S): {data["surl"]} : {data["port"]}')
    createButton("Backup Remote", func=buRemote)
    if "token" in data.keys():
        createButton("Reset", func=reset)


def findProcess(process, command="", isPid=False):
    from psutil import pids, Process

    if isinstance(process, int):
        if process in pids():
            return True
    else:
        for pid in pids():
            try:
                p = Process(pid)
                if process in p.name():
                    for arg in p.cmdline():
                        if command in str(arg):
                            return True if not isPid else str(pid)
                        else:
                            pass
                else:
                    pass
            except:
                continue

def installNgrok():
    if checkAvailable("/usr/local/bin/ngrok"):
        return
    else:
        runSh(
            "wget -qq -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"
        )
        runSh("unzip -qq -n ngrok-stable-linux-amd64.zip")
        runSh("mv ngrok /usr/local/bin/ngrok")
        runSh("rm -f /content/ngrok-stable-linux-amd64.zip")

def installAutoSSH():
    if checkAvailable("/usr/bin/autossh"):
        return
    else:
        runSh("apt-get install autossh -qq -y")



def runSh(args, *, output=False, shell=False, cd=None):
    import subprocess, shlex 

    if not shell:
        if output:
            proc = subprocess.Popen( 
                shlex.split(args), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cd
            )
            while True:
                output = proc.stdout.readline()
                if output == b"" and proc.poll() is not None:
                    return
                if output:
                    print(output.decode("utf-8").strip())
        return subprocess.run(shlex.split(args), cwd=cd).returncode
    else:
        if output:
            return (
                subprocess.run(
                    args,
                    shell=True, 
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    cwd=cd,
                )
                .stdout.decode("utf-8")
                .strip()
            )
        return subprocess.run(args, shell=True, cwd=cd).returncode 


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
        return True
    else:
        print("Script Update Checker: Your script is up to date")
        
