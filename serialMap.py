import serial
import numpy as np

serialPort = serial.Serial('/dev/tty.usbmodem21301', 9600)
scanArray = []

while True:
    data = serialPort.readline().decode()
    if len(data) > 0:
        