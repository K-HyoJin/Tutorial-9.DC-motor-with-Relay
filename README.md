# Arduino example 9
Tutorial 9.DC motor with Relay\
버튼 클릭에 따라 LED와 Motor Fan가 on/off되도록 제작

## circuit
 relay 1 : digital 3pin \
 relay 2 : GND \
 relay 6 : motor Vcc \
 relay 4 : digital 13pin\
button과 연결된 저항 : digital 2pin\
![image](https://user-images.githubusercontent.com/79436159/109284507-45054200-7863-11eb-83e6-c640ca198112.png)

## code
``` from pyfirmata import Arduino,util ```\
pyfirmata의 아두이노 모듈을 사용하기 위해 import함 

``` import time ```\
프로그램을 일정시간동안 지연시키기위해 time 모듈을 import함

``` board = Arduino('COM8')``` \
변수1 = Arduino('**포트번호**') 를 해서 보드와 연결 

``` digital_input = board.get_pin('d:3:i')``` \
  -> 3번핀을 digital신호 입력핀으로 설정\
```led = board.get_pin('d:13:o') ```\
  -> 13번 핀을 digital신호 출력핀으로 설정\
변수1 = 변수2.get_pin('**d or a** : **pin number** : **i or o** ') \
**d or a** : The type of the pin \
**pin number** : The number of the pin\
**i or o** : The mode of the pin
  
``` it = util.Iterator(board) ```\
보드의 입력값을 지속적으로 업데이트해주는 iterator 변수 선언

 ``` it.start()``` \
iterator 시작

``` switch = digital_input.read() ```\
button과 연결된 3번핀의 입력을 읽어와서 변수 switch에 저장

```  
if switch is True:
  led.write(1)
else:
  led.write(0)
```
버튼을 누르면 switch가 Ture되고 True가 되면 led가 켜지도록 1을 입력으로 줌\
switch가 false면 led가 꺼지도록 0을 입력으로 줌
    
