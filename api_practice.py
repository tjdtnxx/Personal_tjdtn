from roboid import *

beagle = Beagle()

beagle.wheels(50,50)    # 양쪽 바퀴를 50 %의 속력으로 전진한다.


wait(1000)

beagle.wheels(-50,-50)  # 양쪽 바퀴를 50 %의 속력으로 후진한다.


wait(1000)


beagle.wheels(0,0)      # 양쪽 바퀴를 정지한다.