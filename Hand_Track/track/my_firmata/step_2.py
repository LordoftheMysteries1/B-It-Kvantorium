# pip install pyfirmata
import pyfirmata
import time

board = pyfirmata.Arduino('COM5')
# «a»/«d» (аналоговый или цифровой пин), номера контакта и режима («i» для ввода, «o» для выхода, «p» для ШИМ).
led = board.get_pin('d:9:p')

while True:
    for i in range(0, 101):
        print(i / 100)
        led.write(i / 100)
        time.sleep(0.1)
        
    for i in range(100, -1, -1):
        print(i / 100)
        led.write(i / 100)
        time.sleep(0.1)