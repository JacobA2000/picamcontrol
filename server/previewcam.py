from keyboard import is_pressed

def startPreview():
    #from camcontrol import camera
    #camera.start_preview()
    print("opened preview")
    while True:        
        if is_pressed('esc'):
            #camera.stop_preview()
            print("closed preview")
            break