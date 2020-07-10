from picamera import PiCamera
from os import path

camera = PiCamera()

defaultSettings = ["resolution=1280,720", "rotation=0", 
                    "brightness=50", "contrast=0", "saturation=0",
                    "sharpness=0", "led=True"]

def ApplySettings(settingsToApply):
    camera.resolution = (settingsToApply[0].split(',')[0], settingsToApply[0].split(',')[1])
    camera.rotation = int(settingsToApply[1])
    camera.brightness = int(settingsToApply[2])
    camera.contrast = int(settingsToApply[3])
    camera.saturation = int(settingsToApply[4])
    camera.sharpness = int(settingsToApply[5])

    if settingsToApply[6] == "True":
        camera.led = True
    elif settingsToApply[6] == "False":
        camera.led = False

def InitCamera():
    if path.exists("camsettings.txt") == False:
        configFile = open("camsettings.txt", "w+")
        for i in range(7):
            configFile.write(defaultSettings[i] + '\n')
        configFile.close()
        print("[GENERAL] Camera settings file created with default values.")
    
    else:
        print("[GENERAL] Camera settings file already exists, importing settings...")
        configFile = open("camsettings.txt", "r")
        configFileLines = configFile.readlines()

        valuesToChange = []
        for setting in configFileLines:
            splitSetting = setting.split('=')
            settingValue = splitSetting[1].replace('\n', '')
            valuesToChange.append(settingValue)

        ApplySettings(valuesToChange)



InitCamera()





