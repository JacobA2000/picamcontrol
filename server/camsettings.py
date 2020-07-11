from picamera import PiCamera
from os import path, mkdir

camera = PiCamera()

save_path = "/home/pi/Camera/camoutput/"

defaultSettings = ["save_path=/home/pi/Camera/camoutput/","resolution=1280,720", "rotation=0", 
                    "brightness=50", "contrast=0", "saturation=0",
                    "sharpness=0", "led=True"]

def ApplySettings(settingsToApply):
    
    global save_path 
    save_path = settingsToApply[0]

    resWidth = int(settingsToApply[1].split(',')[0])
    resHeight = int(settingsToApply[1].split(',')[1])
    camera.resolution = (resWidth, resHeight)

    camera.rotation = int(settingsToApply[2])
    
    camera.brightness = int(settingsToApply[3])
    
    camera.contrast = int(settingsToApply[4])
    
    camera.saturation = int(settingsToApply[5])
    
    camera.sharpness = int(settingsToApply[6])

    if settingsToApply[7] == "True":
        camera.led = True
    elif settingsToApply[7] == "False":
        camera.led = False

def InitCamera():
    

    if path.exists("camsettings.txt") == False:
        configFile = open("camsettings.txt", "w+")
        for i in range(8):
            configFile.write(defaultSettings[i] + '\n')
        configFile.close()
        print("[CAMERA] Camera settings file created with default values.")
    
    else:
        print("[CAMERA] Camera settings file already exists, importing settings...")
        configFile = open("camsettings.txt", "r")
        configFileLines = configFile.readlines()

        valuesToChange = []
        for setting in configFileLines:
            splitSetting = setting.split('=')
            settingValue = splitSetting[1].replace('\n', '')
            valuesToChange.append(settingValue)

        ApplySettings(valuesToChange)

    if path.exists(save_path) == False:
        print("[CAMERA] Creating output folder at " + save_path + "...")
        mkdir(save_path)






