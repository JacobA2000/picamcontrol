import socket
import validationfunctions

HEADER = 64
PORT = 5050
SERVER = "127.0.1.1" #SERVER IP (CHANGE TO THE IP OF WHATEVER DEVICE IS RUNNING THE SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while True:
    useCase = input("PiCam Main Menu \n1 = Timelapse, \n2 = Video, \n3 = Preview, \n4 = Settings, \n5 = Exit. \n\n")
    choiceValid = validationfunctions.ValidateIntRange(useCase, 1, 5)

    if choiceValid == True:
        break   
    else:
        print("That is not a valid option please try again.\n")

#TIMELAPSE CAM
if int(useCase) == 1:
    #LOOP UNTIL A VALID ANSWER IS GIVEN
    while True:
        duration = input("How long do you want to run the timelapse for? (in seconds) : ")
        durationValid = validationfunctions.ValidateIntGreaterThanOrEqual(duration, 2)

        if durationValid == True:
            break
        else:
            print("Capture duration must be greater than or equal to 2 in order to capture an image.")

    #LOOP UNTIL A VALID ANSWER IS GIVEN
    while True:
        timeBetweenShots = input("What duration between shots would you like? (in seconds) : ")
        shotTimeValid = validationfunctions.ValidateIntGreaterThanOrEqual(timeBetweenShots, 2)

        if shotTimeValid == True:
            break
        else:
            print("Time between shots must be 2 seconds or more, this is to allow the camera to take high quality images.")

    send("Timelapse|" + duration + "|" + timeBetweenShots)

elif int(useCase) == 5:
    send(DISCONNECT_MESSAGE)

while True:
    returnedMsg = client.recv(2048).decode(FORMAT)
    print(returnedMsg)
    
    #if returnedMsg == "[TIMELAPSE] COMPLETE":
    #    send(DISCONNECT_MESSAGE)
    #    break
    
    if returnedMsg != "":
        send(DISCONNECT_MESSAGE)
        break

    elif int(useCase) == 5:
        break
    
