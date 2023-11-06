import pygame as py
import random as r
import time as t
import json

py.font.init()

window = py.display.set_mode((1000,700))

font = py.font.SysFont('Comic Sans MS', 30)

FPSClock =  py.time.Clock()
FPS = 60

arrowDict = {
    py.K_UP : ((0,0,255),(0,0,125),((window.get_width() / 2, window.get_height() / 2),(0,0),(window.get_width(),0))),
    py.K_DOWN : ((0,255,0),(0,125,0),((window.get_width() / 2, window.get_height() / 2),(window.get_width(),window.get_height()),(0,window.get_height()))),
    py.K_LEFT : ((255,0,0),(125,0,0),((window.get_width() / 2, window.get_height() / 2),(0,0),(0,window.get_height()))),
    py.K_RIGHT : ((255,255,0),(125,125,0),((window.get_width() / 2, window.get_height() / 2),(window.get_width(),window.get_height()),(window.get_width(),0)))

}

failTime = 0
activePattern = []
pattern = []

def nextPattern(parrternKey):
    activePattern.append(parrternKey)
    window.fill((0,0,0))
    py.display.update()
    t.sleep(0.05)
    py.draw.polygon(window,arrowDict[parrternKey][0],arrowDict[parrternKey][2])
    py.display.update()
    t.sleep(0.4)
    
def clickKey(key):
    global failTime
    if activePattern[0] == key:
        activePattern.pop(0)
        py.draw.polygon(window,arrowDict[key][0],arrowDict[key][2])
        py.display.update()
        t.sleep(0.2)
        py.draw.polygon(window,arrowDict[key][1],arrowDict[key][2])
        py.display.update()
        failTime = 0
    else:
        quitProgram()
        
def patternNext():
    global failTime
    pattern.append(r.choice(list(arrowDict.keys())))
    for patternKey in pattern:
        nextPattern(patternKey)
    failTime = 0
    for i in list(arrowDict.keys()):
        py.draw.polygon(window,arrowDict[i][1],arrowDict[i][2])
    py.display.update()
    py.event.clear()
    
def quitProgram():
    print("Your score was: " + str(len(pattern) - 1))
    with open("Leaderboard.JSON", "r") as infile:
        leaderboard = json.load(infile)
    leaderboard[input("What is your name? ")] = str(len(pattern) - 1)
    with open("Leaderboard.JSON", "w") as outfile:
        json.dump(leaderboard, outfile)
    py.quit()
    quit()  
    
def checkClick():
    for event in py.event.get():
        if event.type == py.KEYDOWN and event.key in list(arrowDict.keys()):
            clickKey(event.key)
    
while True:
    FPSClock.tick(FPS)
    if len(activePattern) == 0:
        patternNext()
    else:         
        checkClick()
        
    if failTime == 50:
        quitProgram()      
    else:
        failTime += 1 