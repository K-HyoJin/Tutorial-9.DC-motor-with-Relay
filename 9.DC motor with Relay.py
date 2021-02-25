from pyfirmata import Arduino,util
import time 

#핀 모드설정
board = Arduino('COM8')
digital_input = board.get_pin('d:3:i') #3번핀 입력
led = board.get_pin('d:13:o') #13번핀 출력


it = util.Iterator(board) #회로의 입력상태를 읽어올 변수선언
it.start()

print("start")
while True:
    switch = digital_input.read()
    if switch is True:
        led.write(1)
    else:
        led.write(0)
    
