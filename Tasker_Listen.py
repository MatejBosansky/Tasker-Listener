import socket
import time
import os
from pynput.keyboard import Controller, Key
keyboard = Controller()
TurnCWCounter = 0

#function to process data and extract command from recieved API request
def ProcessData(inp):
    DoAction(str(data.decode("utf-8")).split('\n')[-1])


def DoAction(action):
    global TurnCWCounter
    print('Action: ' + str(action))
    if action == 'SWIPE_LEFT':
        keyboard.press(Key.media_play_pause)
        #keyboard.release(Key.media_play_pause)
    elif action == 'SWIPE_RIGHT':
        keyboard.press(Key.media_next)
        keyboard.release(Key.media_next)
    elif action == 'SWIPE_UP':
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
    elif action == 'SWIPE_DOWN':
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
    elif action == 'TURN_CW':
        TurnCWCounter += 1
        if TurnCWCounter >1:
            print('Turn off')
            os.system('shutdown -s')

        return
    TurnCWCounter = 0
    print('')

print('Start listening')
while True:
    with socket.socket() as s:
        host = '' #in api call use your PC IP address. Recommending to set static IP https://portforward.com/networking/static-ip-windows-10.htm
        port = 65431
        s.bind((host, port))
        #print(f'socket binded to {port}')
        s.listen()
        con, addr = s.accept()
        with con:
            while True:
                data = con.recv(1024)
                #print(str(data.decode("utf-8"))) #uncomment if you want to see raw content of you received requests
                if not data:
                    break
                ProcessData(data)
                con.sendall(data)