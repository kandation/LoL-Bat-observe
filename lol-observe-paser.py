data = {
    "game_path" : "C:/Program Files (x86)/Garena/32786/Game",
    "game_client" : "League of Legends.exe",
}


from tkinter import *
from tkinter.filedialog import askopenfilename

import os


root = Tk()
root.withdraw()
root.update()
filename = askopenfilename()
root.destroy()

def openconfig():
    try:
        fo = open('config.txt', mode='r')
        f = fo.read()
        f = str(f).strip()
        fo.close()
        f = f[0:-2] if f[-1] == '/' else f
        return f

    except:
        print("Cannot find 'config.txt' ")

def newGamepath(game, data):
    data['game_path'] = game


def paser(content):
    k = content.find("spectator")
    k = content[k:-1]
    g = k.split(" ")

    return g[1:5]

def getLeagueCommand(oString):
    servreName = oString[3].strip().replace('"', '')
    obs = '"./' + data["game_client"] + '" '
    obs += '"spectator ' + oString[0] +' ' + oString[1] + ' ' + oString[2] +' ' + servreName + '" '
    obs += '-UseRads '
    return obs

def getBash(leagueCommand):
    command = data['game_path'][0:2]
    command += '\ncd '+data['game_path']
    command += '\n'+leagueCommand
    return command

def createBash(bashCommand):
    with open("TEMP_leaguegraph_spectator.bat", mode='w') as file:
        file.write(bashCommand)

if len(filename) > 0:
    newGamepath(openconfig(), data)

    leaguegraph_web_input = open(filename, mode='r')
    leaguegraph_web_input = leaguegraph_web_input.read()
    bash = getBash(getLeagueCommand(paser(leaguegraph_web_input)))
    try:
        createBash(bash)
    except:
        print("Cannot create temp file T_T")

    try:
        os.system("TEMP_leaguegraph_spectator.bat")
    except:
        print("Cannot run TEMP file")
else:
    raise Exception("File not Exsit")

import time
time.sleep(3)
