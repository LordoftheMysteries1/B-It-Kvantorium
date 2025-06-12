# pip install pyserial
import serial
import time

portNo = "COM17"
uart = serial.Serial(portNo, 9600)

while True:
    # value = int(input('Введите значение от 0 до 255: '))
    # проверка на корректность значений
    # # 2 5 5 ; 2 5 5 2 5 5 2 5 5
    # #255;#255;#255;#255;
    for value in range(0, 256):
        msg = f'#{value};' 
        msg = bytes(msg, 'utf-8')
        uart.write(msg)
        print(msg)
        time.sleep(0.1)