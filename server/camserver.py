import socket 
import threading
import camsettings
from timelapsecam import startTimelapse

HEADER = 64
PORT = 5050
#SERVER = socket.gethostbyname(socket.gethostname()) #FOR WINDOWS USE
SERVER = "192.168.1.253" #FOR LINUX USE, MUST BE CAHNGED MANUALLY ATM
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            print(f"[{addr}] {msg}")
            #conn.send("Msg received".encode(FORMAT))

            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                camCommand = msg.split('|')
                #START THE TIMELAPSE
                if camCommand[0] == "Timelapse":
                    duration = camCommand[1]
                    timeBetweenShots = camCommand[2]
                    conn.send("[TIMELAPSE] STARTING".encode(FORMAT))
                    startTimelapse(duration, timeBetweenShots)
                    #Need to add code to handle loss of connection.
                    conn.send("[TIMELAPSE] COMPLETE".encode(FORMAT))
    
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[CAMERA] Initialising camera...")
camsettings.InitCamera()
print("[STARTING] Server is starting...")
start()