#!/usr/bin/python3

import RPi.GPIO as GPIO
import sys
from pynput.keyboard import Key, Controller
from mfrc522 import SimpleMFRC522
from time import sleep

keyboard = Controller()
reader = SimpleMFRC522()
debug = False

while True:
   try:
      uuid = reader.read_id()
      if debug:
         print(uuid)
         print("HEX = ")
      #hexuuid = hex(uuid)
      hexuuid = format(uuid,"010x")
      if debug:
         print(hexuuid)
         print("Reversed HEX = ")
      rehexuuid = "".join(map(str.__add__, hexuuid[-2::-2] ,hexuuid[-1::-2]))
      if debug:
         print(rehexuuid)
         print("Stripped reversed HEX = ")
      strrehexuuid = rehexuuid[-8:]
      if debug:
         print(strrehexuuid)
         print("Final dec version = ")
      cardDec = int(strrehexuuid, 16)
      if debug:
         print(cardDec)
         print("Keyboard write: ")
      keyboard.type(str(cardDec))
      keyboard.press(Key.enter)
      keyboard.release(Key.enter)
      sleep(1)
   except KeyboardInterrupt:
      GPIO.cleanup()
      sys.exit(1)
