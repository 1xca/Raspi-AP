from gpiozero import Button
from time import sleep
import subprocess

button = Button(12)

while True:
    if True:
        print('pressed')
        #subprocess.call('./changePassword.sh')
    else:
        print('released')
    sleep(1)