#!/usr/bin/python3

from gpiozero import Button
from signal import pause
from os import system

button = Button(21, hold_time=3)

def shutdown_pi():
   system("sudo shutdown now -hP")

button.when_held = shutdown_pi
pause()
