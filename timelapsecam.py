from time import sleep
from math import floor
from datetime import datetime

def startTimelapse(duration, timeBetweenShots):
    #from camcontrol import camera
    numberOfShots = floor(int(duration)/int(timeBetweenShots))

    #camera.start_preview()

    for i in range(numberOfShots):
        sleep(int(timeBetweenShots))
        timeNow = datetime.now()
        takenAt = timeNow.strftime("%d/%m/%Y %H:%M:%S")
        print("[TIMELAPSE] Photo %s taken at %s" % (i, takenAt))
        #camera.capture('/home/pi/image%s.jpg' % i)

    #camera.stop_preview()