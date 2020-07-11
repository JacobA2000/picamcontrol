from time import sleep
from math import floor
from datetime import datetime
from os import path, mkdir
import camsettings

camera = camsettings.camera

def startTimelapse(duration, timeBetweenShots):
    now = datetime.now()
    timelaspeStartTime = str(now.strftime("%d-%m-%Y %H:%M:%S"))
    savepath = camsettings.save_path + timelaspeStartTime + '/'
    numberOfShots = floor(int(duration)/int(timeBetweenShots))
    
    if path.exists(savepath) == False:
        print("[TIMELAPSE] Creating output folder")
        mkdir(savepath)

    camera.start_preview()

    for i in range(numberOfShots):
        sleep(int(timeBetweenShots))
        timeNow = datetime.now()
        takenAt = timeNow.strftime("%d/%m/%Y %H:%M:%S")
        print("[TIMELAPSE] Photo %s taken at %s" % (i, takenAt))
        camera.capture(savepath + 'image%s.jpg' % i)

    camera.stop_preview()