from roboid import *

beagle = Beagle()
beagle.start_lidar()

print(beagle.is_lidar_ready())

# 라이다 센서 값들을 차트로 보여줍니다.
# value = beagle.lidar_chart()

# print(value)