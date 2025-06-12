# pip install pyfirmata
import pyfirmata
import time

board = pyfirmata.Arduino('COM5')
it = pyfirmata.util.Iterator(board)
it.start()

# «a»/«d» (аналоговый или цифровой пин), номера контакта и режима («i» для ввода, «o» для выхода, «p» для ШИМ).
led = board.get_pin('d:9:p')
button = board.get_pin('d:2:i')

while True:
    if button.read():
        led.write(1)
    else:
        led.write(0)