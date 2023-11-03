import pygame as py
import random as r
import time as t

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

while True:
    FPSClock.tick(FPS)
    if len(activePattern) == 0:
        pattern.append(r.choice((py.K_UP,py.K_DOWN,py.K_LEFT,py.K_RIGHT)))
        for i in pattern:
            activePattern.append(i)
            window.fill((0,0,0))
            py.display.update()
            t.sleep(0.05)
            py.draw.polygon(window,arrowDict[i][0],arrowDict[i][2])
            py.display.update()
            t.sleep(0.4)

        failTime = 0
        for i in (py.K_UP,py.K_DOWN,py.K_LEFT,py.K_RIGHT):
            py.draw.polygon(window,arrowDict[i][1],arrowDict[i][2])
        py.display.update()
        py.event.clear()
    else:         
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key in [py.K_UP,py.K_DOWN,py.K_LEFT,py.K_RIGHT]:
                    if activePattern[0] == event.key:
                        activePattern.pop(0)
                        py.draw.polygon(window,arrowDict[event.key][0],arrowDict[event.key][2])
                        py.display.update()
                        t.sleep(0.2)
                        py.draw.polygon(window,arrowDict[event.key][1],arrowDict[event.key][2])
                        py.display.update()
                        failTime = 0
                    else:
                        print("Your score was: " + str(len(pattern) - 1))
                        py.quit()
                        quit()
        if failTime == 50:
            print("Your score was: " + str(len(pattern) - 1))
            py.quit()
            quit()        
        else:
            failTime += 1 