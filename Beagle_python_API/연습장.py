# from roboid import *

# beagle = Beagle()

# while True:
#     beagle.wheels(50,-50)
#     wait(100)
#     print(beagle.gyroscope_z())
#     wait(100)


# from roboid import *

# beagle = Beagle()

# # 리스너 함수를 정의합니다.
# def listener(index, timestamp, x, y, z):
#     print(index, timestamp, x, y, z)

# beagle.listen_gyroscope(listener)

from roboid import *

beagle = Beagle()

# 서보 모터 C를 30도로 회전시킵니다.
beagle.servo_output_c_until_done(30)