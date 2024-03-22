import random           # 난수를 위한 파이썬의 random 모듈
from roboid import *    # 햄스터 라이브러리
import keyboard
Beagle = Beagle()     # 비글 연결



def calc_speed(proximity):      # 함수 선언
    if proximity > 15:              # 거리가 멀면 앞으로, 가까우면 뒤로 이동한다.
        return (40 - proximity) * 4 # proximity값이 40을 넘으면 음의 값을 가져 뒤로간다.
    else:
        return 0

def LF():
    return Beagle.left_floor()

def RF():
    return Beagle.right_floor()

def blink_short():
    Beagle.leds(Beagle.COLOR_NAME_WHITE)
    wait(200)
    Beagle.leds(0)
    wait(200)

def blink_long():
    Beagle.leds(Beagle.COLOR_NAME_WHITE)
    wait(1000)
    Beagle.leds(0)
    wait(200)

def act_l():
    Beagle.wheels(-30)
    wait(1000)
    Beagle.wheels(-30,30)
    wait(1000)
    Beagle.stop()

def act_r():
    Beagle.wheels(-30)
    wait(1000)
    Beagle.wheels(30,-30)
    wait(1000)
    Beagle.stop()

def on_key_release(event):
    if event.name == 'w':
        Beagle.stop()
    if event.name == 'a':
        Beagle.stop()
    if event.name == 's':
        Beagle.stop()
    if event.name == 'd':
        Beagle.stop()

def keycontrol():
    while True:      
        if keyboard.is_pressed("w"):
            Beagle.wheels(50)
        elif keyboard.is_pressed("a"):
            Beagle.wheels(-50,50)
        elif keyboard.is_pressed("d"):
            Beagle.wheels(50,-50)
        elif keyboard.is_pressed("s"):
            Beagle.wheels(-50)
        wait(20)

# def lidar_4way():
#     Beagle.start_lidar()
#     Beagle.wait_until_lidar_ready()

#     print('Is Beagle ready? ', + Beagle.is_lidar_ready())

#     value = Beagle.lidar()

#     while True:
#         value = Beagle.lidar()
#         value_N = value[0]
#         value_W = value[90]
#         value_S = value[180]
#         value_E = value[270]

#         print("\n\t",value_N,"\t\n",value_W,"\t\t",value_E,"\n\t",value_S)
#         wait(500)

# lidar_4way()
keyboard.on_release(on_key_release)

keycontrol()

