# pip install pyfirmata
import pyfirmata
import time

board = pyfirmata.Arduino('COM17')

while True:
    board.digital[11].write(1)
    time.sleep(0.5)
    board.digital[11].write(0)
    time.sleep(0.5)