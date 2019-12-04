import os
import time
import json
import urllib.request
from sys import exit as exx, path as s_p
from IPython.display import HTML, clear_output
from lxml.etree import XML

tokens = {
      "api1":"6qGnEsrCL4GqZ7hMfqpyz_7ejAThUCjVnU9gD5pbP5u",
      "api2":"1Q4i7F6isO7zZRrrjBKZzZhwsMu_74yJqoEs1HrJh1zYyxNo1",
      "api3":"1SCsbuawjv9d79jlhlfNljaFTaB_5heVkcR6C7Sk8UBaQ1U1C",
      "api5":"1Q45NXgsx6oyusN3GiNAYvkNJPS_AveYUDBcPHsvRvf21WZv",
      "api6":"1Q6smHt4Bzz9VEXTwj3a7p5Gdx2_5mp6ivT6N6nB3YmRHUEM3",
      "api7":"7VJwGkCTTUubiGhgz6Gv6_5fMLganRSKj9ntdefnF5o",
      "api9":"5S28rBKgc22ZW7evyedNT_YvEm15RZSHdXgS4QwYbk",
      "api11":"7pWLVhS1gxiMAQdaFeYJy_31krnw9drNLLJftaNSFnm",
      "api12":"3VnrrXDQVHoNp9HvHFhqX_3X4JExwm6L9n6w4ppL1qy",
      "api13":"1ShshNwfhQcyOqlMjnBDVE5X5jC_3WAmzomMHAgkunka4dSck",
      "api14":"772yFAui6ynH9AYx29HHS_5Xcr88pHtPTQLwewv7Ctk",
      "api16":"5HmAWwzDdkYp8CdzDQMDS_4BGwsK7AdMssLnSttZEeh",
      "api17":"1T750atJi3xccndeUqJ4ewiS62o_2s6f8GUccL1qDUXTGSftN",
      "api18":"1QUysRUo97w5mdB6sCZvTTMM0aK_3unoMs6nYd7grgCkuhbj3",
      "api19":"3CqeFZQht43cG5Z2YKfyv_6aKTrgrbo1HtyRi78hRKK",
      "api20":"5eMywZLisJNdybqpFLVgs_4XQDeF3YCMHu1Ybf7mVE6",
      "api21":"4Cg1cEwCT7Ek89zT4VcdB_4GPAjMFgu6nhwY7SxQm94",
      "api22":"1SGs4s9NrhxP9FRURszjL1nITSv_otcpfpb6aMVEL13u3dv1",
      "api23":"1StL3sIccfR624Uc3BGV36XA0qG_6cAMMYFdKtPjtWax3AHSK",
      "api24":"1SuK2ukM9Z4NohoJbU9224uMzXr_6h1ABdCrJU2EviZv4RN4r",
      "api26":"7ecmt2Kux5uYsTUHrrqGU_3W9CJnaSeSyxiwkjxNhHc",
      "api27":"3CqeFZQht43cG5Z2YKfyv_6aKTrgrbo1HtyRi78hRKK",
      "api28":"2DXURjrUhAZZNMhqN5m1F_6HHzejcfRecP8upwJnNBd",
}

def nameport(TOKEN, AUTO, PORT=10001):
  def selectApi(api):
    try:
        return tokens[api]
    except:
        return tkns
      
  if AUTO:
    try:
      USR_Api, tkns = tokens.popitem()
    except KeyError:
      return "Invalid Token", PORT
  elif not TOKEN:
    if not 'your' in tokens.keys():
      from IPython import get_ipython
      ipython = get_ipython()

      print("Copy authtoken from https://dashboard.ngrok.com/auth")
      __temp = ipython.magic('%sx read -p "Token :"')
      tokens['your'] = __temp[0].split(':')[1]
      USR_Api = "your"
      clear_output()
    else:
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


def displayUrl(data,btc='b'):
    clear_output(wait=True)
    showTxT = f'Public URL: {data["url"]}'
    showUrL = data["url"]
    if btc == 'b':
          # blue
          bttxt = 'hsla(210, 50%, 85%, 1)'
          btcolor = 'hsl(210, 80%, 42%)'
          btshado = 'hsla(210, 40%, 52%, .4)'
    elif btc == 'g':
          # green
          bttxt = 'hsla(110, 50%, 85%, 1)'
          btcolor = 'hsla(110, 86%, 56%, 1)'
          btshado = 'hsla(110, 40%, 52%, .4)'
    elif btc == 'r':
          # red
          bttxt = 'hsla(10, 50%, 85%, 1)'
          btcolor = 'hsla(10, 86%, 56%, 1)'
          btshado = 'hsla(10, 40%, 52%, .4)'

    return display(HTML('''<style>@import url('https://fonts.googleapis.com/css?family=Source+Code+Pro:200,900');  :root {   --text-color: '''+bttxt+''';   --shadow-color: '''+btshado+''';   --btn-color: '''+btcolor+''';   --bg-color: #141218; }  * {   box-sizing: border-box; } button { position:relative; padding: 10px 20px;     border: none;   background: none;   cursor: pointer;      font-family: "Source Code Pro";   font-weight: 900;   text-transform: uppercase;   font-size: 20px;     color: var(--text-color);      background-color: var(--btn-color);   box-shadow: var(--shadow-color) 2px 2px 22px;   border-radius: 4px;    z-index: 0;     overflow: hidden;    }  button:focus {   outline-color: transparent;   box-shadow: var(--btn-color) 2px 2px 22px; }  .right::after, button::after {   content: var(--content);   display: block;   position: absolute;   white-space: nowrap;   padding: 40px 40px;   pointer-events:none; }  button::after{   font-weight: 200;   top: -30px;   left: -20px; }   .right, .left {   position: absolute;   width: 100%;   height: 100%;   top: 0; } .right {   left: 66%; } .left {   right: 66%; } .right::after {   top: -30px;   left: calc(-66% - 20px);      background-color: var(--bg-color);   color:transparent;   transition: transform .4s ease-out;   transform: translate(0, -90%) rotate(0deg) }  button:hover .right::after {   transform: translate(0, -47%) rotate(0deg) }  button .right:hover::after {   transform: translate(0, -50%) rotate(-7deg) }  button .left:hover ~ .right::after {   transform: translate(0, -50%) rotate(7deg) }  /* bubbles */ button::before {   content: '';   pointer-events: none;   opacity: .6;   background:     radial-gradient(circle at 20% 35%,  transparent 0,  transparent 2px, var(--text-color) 3px, var(--text-color) 4px, transparent 4px),     radial-gradient(circle at 75% 44%, transparent 0,  transparent 2px, var(--text-color) 3px, var(--text-color) 4px, transparent 4px),     radial-gradient(circle at 46% 52%, transparent 0, transparent 4px, var(--text-color) 5px, var(--text-color) 6px, transparent 6px);    width: 100%;   height: 300%;   top: 0;   left: 0;   position: absolute;   animation: bubbles 5s linear infinite both; }  @keyframes bubbles {   from {     transform: translate();   }   to {     transform: translate(0, -66.666%);   } }    Resources</style><center><a href="'''+showUrL+'''" target="_blank"><div style="width: 570px;   height: 80px; padding-top:15px"><button style='--content: "'''+showTxT+'''";'">   <div class="left"></div>'''+showTxT+'''<div class="right"></div> </div></button></a></center>'''))
    

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

def loadingAn(name="cal"):
      if name == "cal":
          return display(HTML('<style>.lds-ring {   display: inline-block;   position: relative;   width: 34px;   height: 34px; } .lds-ring div {   box-sizing: border-box;   display: block;   position: absolute;   width: 34px;   height: 34px;   margin: 4px;   border: 5px solid #cef;   border-radius: 50%;   animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;   border-color: #cef transparent transparent transparent; } .lds-ring div:nth-child(1) {   animation-delay: -0.45s; } .lds-ring div:nth-child(2) {   animation-delay: -0.3s; } .lds-ring div:nth-child(3) {   animation-delay: -0.15s; } @keyframes lds-ring {   0% {     transform: rotate(0deg);   }   100% {     transform: rotate(360deg);   } }</style><div class="lds-ring"><div></div><div></div><div></div><div></div></div>'))
      elif name == "lds":
          return display(HTML('''<style>.lds-hourglass {  display: inline-block;  position: relative;  width: 34px;  height: 34px;}.lds-hourglass:after {  content: " ";  display: block;  border-radius: 50%;  width: 34px;  height: 34px;  margin: 0px;  box-sizing: border-box;  border: 20px solid #dfc;  border-color: #dfc transparent #dfc transparent;  animation: lds-hourglass 1.2s infinite;}@keyframes lds-hourglass {  0% {    transform: rotate(0);    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);  }  50% {    transform: rotate(900deg);    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);  }  100% {    transform: rotate(1800deg);  }}</style><div class="lds-hourglass"></div>'''))

def updateCheck(self, Version):
    class UpdateChecker(object):
      
      def __init__(self):
          getMessage = self.getMessage
          getVersion = self.getVersion

      def getVersion(self, currentTag):
          url = self.URL
          update = urllib.request.urlopen(url).read()
          root = XML(update)
          cur_version = root.find(".//"+currentTag)
          current = cur_version.text
          return current

      def getMessage(self, messageTag):
          url = self.URL
          update = urllib.request.urlopen(url).read()
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
        
