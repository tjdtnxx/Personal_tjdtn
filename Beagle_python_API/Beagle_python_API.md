# Beagle Python API 메뉴얼



**Beagle**사용자들을 위한 Python API Wiki입니다.<br>
<Br>
이 문서는 로보메이션의 Beagle을 Python으로 프로그래밍하려는 사용자를 위한 라이브러리 API Guide입니다. 

아래 목차에서 **도움말**을 보고싶은 **목차**를 선택하세요.<br>
각 API들의 [제목](#생성)을 클릭하면 [예제코드](#beagle)가 제공되어 있습니다.
<br><br>
>Service: [로보메이션](https://www.robomation.net)<br>
API version: 2024-03-01

<br><br>



### 이 문서의 내용
- [생성 및 해제](#생성-및-해제) <br>
- [바퀴 움직임](#바퀴-움직임) <br>
- [소리](#소리) <br>
- [센서](#센서) <br>
- [서보 모터](#서보-모터) <br>
- [LiDar](#LiDar) <br>
- [전역 함수](#전역-함수) <br>

<br><br><br><br><br>
# 생성 및 해제
- 생성 <br>
- 해제 <br>


### [생성](#beagle)

| Name | Parameter | Return | Description |
| -------- | -------- | -------- | -------- |
| Beagle() |  | Beagle 인스턴스의 참조 | Beagle 인스턴스를 생성하고 하드웨어 비글 로봇과 통신을 연결한다. Beagle(0)을 호출한 것과 같다.
| Beagle(index) |  | Beagle 인스턴스의 참조 | Beagle 인스턴스를 생성하고 하드웨어 비글 로봇과 통신을 연결한다. <br>몇 번째 비글 로봇인지를 나타내는 인덱스를 index로 설정한다. 인덱스가 같으면 같은 비글 로봇이다.
| Beagle(port_name) | port_name: 시리얼 port 이름 (문자열) | Beagle 인스턴스의 참조 | Beagle 인스턴스를 생성하고 port_name의 시리얼 포트를 통해 하드웨어 비글 로봇과 통신을 연결한다. <Br>Beagle(0, port_name)을 호출한 것과 같다.
| Beagle(index, port_name) | index: 몇 번째 비글 로봇인지를 나타내는 인덱스(0이상의 정수), port_name: 시리얼 포트 이름(문자열) | Beagle 인스턴스의 참조 | Beagle 인스턴스를 생성하고 port_name의 시리얼 포트를 통해 하드웨어 비글 로봇과 통신을 연결한다. <br>Beagle(0, port_name)을 호출한 것과 같다.

<br>

### [해제](#dispose)

| Name | Parameter | Return | Description |
| -------- | -------- | -------- | -------- |
| dispose() |  |  | Beagle 로봇의 상태를 초기화하고 통신 연결을 끊는다.
| reset() |  |  | Beagle 로봇의 상태를 초기화한다.




<br><br><br><br><br>
# 바퀴 움직임
- 전진
- 후진
- 스핀
- Pivot(바퀴축)
- 그 외



### 전진

| Name | Parameter | Return | Description |
| -------- | -------- | -------- | -------- |
| move_forward() |  |  | 앞으로 1초 이동한다. (기본 속도인 50%의 속도로 이동), <br>move_forward(1) 또는 move_forward(1, 50)을 호출한 것과 같다.
| move_forward(sec) | sec: 이동할 시간(실수) [초] |  | sec초 앞으로 이동한다. (기본 속도인 50%의 속도로 이동) <br> move_forward(sec, 50)을 호출한 것과 같다. <br> sec 값이 음수이면 반대 방향으로 이동한다.
| move_forward(sec,velocity) | sec: 이동할 시간(실수) [초] <br> velocity: 이동할 속도(실수)(-100~100)[%] |  | sec초 앞으로 이동한다. (velocity 속도로 이동) <br> sec값이 음수이면 반대 방향으로 이동한다. <br> velocity 값이 음수이면 반대 방향으로 이동한다.
| move_forward_pulse(pulse) | pulse: 이동할 펄스 수(0이상의 정수, 0:정지) |  | 펄스(pulse) 수만큼 앞으로 이동한다. (기본 속도인 50%의 속도로 이동) <br> move_forward_pulse(pulse, 50)을 호출한 것과 같다. <br> pulse 값이 음수이면 반대 방향으로 이동한다.
| move_forward_pulse(pulse,velocity) | pulse: 이동할 펄스 수(0이상의 정수, 0: 정지) <br> velocity: 이동할 속도(실수)(-100~100)[%] | | 펄스(pulse) 수만큼 앞으로 이동한다. (velocity 속도로 이동) <br> pulse 값이 음수이면 반대 방향으로 이동한다. <br> velocity 값이 음수이면 반대 방향으로 이동한다. |

### 후진

| Name | Parameter | Return | Description |
| -------- | -------- | -------- | -------- |
| move_backward() | | | 뒤로 1 초 이동한다. (기본 속도인 50 %의 속도로 이동) <br> move_backward(1) 또는 move_backward(1,50)을 호출한 것과 같다. |
| move_backward(sec) | sec: 이동할 시간(실수) [초]| | sec초 뒤로 이동한다. (기본 속도인 50%의 속도로 이동) <br>move_backward(sec, 50)을 호출한 것과 같다. <br>sec 값이 음수이면 반대 방향으로 이동한다.|
| move_backward(sec,velocity) | sec: 이동할 시간(실수) [초]<br>velocity: 이동할 속도(실수)(-100~100)[%]| | sec초 뒤로 이동한다. (velocity 속도로 이동) <br>sec 값이 음수이면 반대 방향으로 이동한다.<br> velocitty 값이 음수이면 반대 방향으로 이동한다.|
| move_backward_pulse(pulse) | pulse: 이동할 펄스 수 (0이상의 정수, 0:정지) |  | 펄스(pulse) 수만큼 뒤로 이동한다. (기본 속도인 50%의 속도로 이동) <br> move_backward_pulse(pulse, 50)을 호출한 것과 같다. <br> pulse 값이 음수이면 반대 방향으로 이동한다.|
| move_backward_pulse(pulse,velocity) | pulse: 이동할 펄스 수 (0이상의 정수, 0: 정지) <br> velocity: 이동할 속도(실수)(-100~100)[%] | | 펄스(pulse) 수만큼 뒤로 이동한다. (velocity 속도로 이동) <br> pulse 값이 음수이면 반대 방향으로 이동한다. <br> velocity 값이 음수이면 반대 방향으로 이동한다. |


### 스핀

| Name | Parameter | Return | Description |
| -------- | -------- | -------- | -------- |
| turn_left() | | | 제자리에서 왼쪽으로 1 초 회전한다. (기본 속도인 50 %의 속도로 회전) <br> turn_left(1) 또는 turn_left(1,50)을 호출한 것과 같다. |
| turn_left(sec) | sec: 이동할 시간(실수) [초] | | sec 초 동안 제자리에서 왼쪽으로 회전한다. (기본 속도인 50 %의 속도로 회전) <br> turn_left(sec,50)을 호출한 것과 같다. sec 값이 음수이면 반대 방향으로 회전한다. |
| turn_left(sec,velocity) | sec: 이동할 시간(실수) [초] <br>velocity: 이동할 속도(실수)(-100~100)[%] | | sec 초 동안 제자리에서 왼쪽으로 회전한다. (velocity 속도로 회전) <br> sec 값이 음수이면 반대 방향으로 회전한다. <br> velocity 값이 음수이면 반대 방향으로 회전한다. |
| turn_left_pulse(pulse) | pulse: 이동할 펄스 수 (0이상의 정수, 0: 정지) | | 펄스(pulse) 수만큼 제자리에서 왼쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)<br>turn_left_pulse(pulse, 50)을 호출한 것과 같다.<br>pulse 값이 음수이면 반대 방향으로 회전한다. |
| turn_left_pulse(pulse,velocity) | pulse: 이동할 펄스 수 (0이상의 정수, 0: 정지)<br>velocity: 이동할 속도(실수)(-100~100)[%]  | | 펄스(pulse) 수만큼 제자리에서 왼쪽으로 회전한다. (velocity 속도로 회전)<br>pulse 값이 음수이면 반대 방향으로 회전한다. <br> velocity 값이 음수이면 반대 방향으로 회전한다.|

<br>

| Name | Parameter | Return | Description |
| -------- | -------- | -------- | -------- |
| turn_right() | | | 제자리에서 오른쪽으로 1 초 회전한다. (기본 속도인 50 %의 속도로 회전) <br> turn_right(1) 또는 turn_right(1,50)을 호출한 것과 같다. |
| turn_right(sec) | sec: 이동할 시간(실수) [초] | | sec 초 동안 제자리에서 오른쪽으로 회전한다. (기본 속도인 50 %의 속도로 회전) <br> turn_right(sec,50)을 호출한 것과 같다. sec 값이 음수이면 반대 방향으로 회전한다. |
| turn_right(sec,velocity) | sec: 이동할 시간(실수) [초] <br>velocity: 이동할 속도(실수)(-100~100)[%] | | sec 초 동안 제자리에서 오른쪽으로 회전한다. (velocity 속도로 회전) <br> sec 값이 음수이면 반대 방향으로 회전한다. <br> velocity 값이 음수이면 반대 방향으로 회전한다. |
| turn_right_pulse(pulse) | pulse: 이동할 펄스 수 (0이상의 정수, 0: 정지) | | 펄스(pulse) 수만큼 제자리에서 오른쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)<br>turn_right_pulse(pulse, 50)을 호출한 것과 같다.<br>pulse 값이 음수이면 반대 방향으로 회전한다. |
| turn_right_pulse(pulse,velocity) | pulse: 이동할 펄스 수 (0이상의 정수, 0: 정지)<br>velocity: 이동할 속도(실수)(-100~100)[%]  | | 펄스(pulse) 수만큼 제자리에서 오른쪽으로 회전한다. (velocity 속도로 회전)<br>pulse 값이 음수이면 반대 방향으로 회전한다. <br> velocity 값이 음수이면 반대 방향으로 회전한다.|


### Pivot

### 그 외



























<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### Beagle()
```python
from roboid import *
beagle = Beagle()
```