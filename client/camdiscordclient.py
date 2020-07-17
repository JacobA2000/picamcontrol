import socket
import validationfunctions
import discord
from discord.ext import commands, tasks
import atexit
import threading
import asyncio

HEADER = 64
PORT = 5050
SERVER = "192.168.1.253" #SERVER IP (CHANGE TO THE IP OF WHATEVER DEVICE IS RUNNING THE SERVER)
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

camBusy = False

def waitForValidResponse():
    global camBusy
    while True:
        returnedMsg = client.recv(2048).decode(FORMAT)
        if returnedMsg == "[TIMELAPSE] COMPLETE":
            print(returnedMsg)       
            camBusy = False
                  

bot = commands.Bot(command_prefix= '!picam ')

@bot.event
async def on_ready():
    print('Bot is online.')                

@bot.command()
async def timelapse(ctx, duration, timeBetweenShots):
    print(f"timelapse command ran by {ctx.author}")

    global camBusy

    durationValid = validationfunctions.ValidateIntGreaterThanOrEqual(duration, 2)
    shotTimeValid = validationfunctions.ValidateIntGreaterThanOrEqual(timeBetweenShots, 2) 

    if durationValid and shotTimeValid and camBusy == False:
        send("Timelapse|" + duration + "|" + timeBetweenShots)
        camBusy = True
        await ctx.send(f"Starting timelapse for {duration} seconds, taking a photo every {timeBetweenShots} seconds.")
        thread = threading.Thread(target=waitForValidResponse)
        thread.start()

    elif camBusy == True:
        await ctx.send("Camera is currently busy, try again later.")
    else:
        await ctx.send("Incorrect values! Try again.")   

def exit_handler():
    send(DISCONNECT_MESSAGE)
    print("Disconnecting...")

atexit.register(exit_handler)

bot.run('insert token here')

