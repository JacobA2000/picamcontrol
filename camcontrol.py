#RETIRED SCRIPT JUST USING AS POINT OF REFERENCE!!!!1


#from picamera import PiCamera
import validationfunctions
#camera = PiCamera()
#camera.resolution = (1280, 720)

#LOOP UNTIL A VALID ANSWER IS GIVEN
while True:
    useCase = input("What would you like to use the camera for? \n1 = Timelapse, \n2 = Security, \n3 = Preview. \n\n")
    choiceValid = validationfunctions.ValidateIntRange(useCase, 1, 3)

    if choiceValid == True:
        break   
    else:
        print("That is not a valid option please try again.\n")

#TIMELAPSE CAM
if int(useCase) == 1:
    from timelapsecam import startTimelapse

    #LOOP UNTIL A VALID ANSWER IS GIVEN
    while True:
        duration = input("How long do you want to run the timelapse for? (in seconds) : ")
        durationValid = validationfunctions.ValidateIntGreaterThanOrEqual(duration, 2)

        if durationValid == True:
            break
        else:
            print("Capture duration must be greater than 2 in order to capture an image.")

    #LOOP UNTIL A VALID ANSWER IS GIVEN
    while True:
        timeBetweenShots = input("What duration between shots would you like? (in seconds) : ")
        shotTimeValid = validationfunctions.ValidateIntGreaterThanOrEqual(timeBetweenShots, 2)

        if shotTimeValid == True:
            break
        else:
            print("Time between shots must be 2 seconds or more, this is to allow the camera to take high quality images.")
            
    startTimelapse(duration, timeBetweenShots)

#SECURITY CAM
elif int(useCase) == 2:
    from securitycam import startSecurityCam
    startSecurityCam()

#PREVIEW CAM
elif int(useCase) == 3:
    from previewcam import startPreview
    startPreview()

else:
    print("Erorr")
