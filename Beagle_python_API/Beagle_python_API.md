# Beagle Python API 메뉴얼



**Beagle**사용자들을 위한 Python API Wiki입니다.<br>
<Br>
이 문서는 로보메이션의 Beagle을 Python으로 프로그래밍하려는 사용자를 위한 라이브러리 API Guide입니다. 

아래 목차에서 **도움말**을 보고싶은 **목차**를 선택하세요.<br>
각 API들의 [제목](#생성)을 클릭하면 [예제코드](#beagle)가 제공되어 있습니다.
<br><br>
>Service: [로보메이션](https://www.robomation.net)<br>
API version: 2024-03-01

<br>

### < 이 문서의 내용 >
>- [시작하기에 앞서](#시작하기에-앞서)
>- [생성 및 해제](#생성-및-해제) <br>
>- [바퀴 움직임](#바퀴-움직임) <br>
>- [소리](#소리) <br>
>- [센서](#센서) <br>
>- [서보 모터](#서보-모터) <br>
>- [LiDar](#LiDar) <br>
>- [전역 함수](#전역-함수) <br>

<br><br>
# 시작하기에 앞서
이 문서는 **Python 개발환경 구축 및 설치가 완료가 되어 개발 준비가 완료되어 있는 사용자들**을 위한 Beagle Python API메뉴얼입니다.

API란?<br>
API는 Application Programming Interface의 줄임말입니다. API의 맥락에서 애플리케이션이라는 단어는 고유한 기능을 가진 모든 소프트웨어를 나타냅니다. 인터페이스는 두 애플리케이션 간의 서비스 계약이라고 할 수 있습니다. 이 계약은 요청과 응답을 사용하여 두 애플리케이션이 서로 통신하는 방법을 정의합니다. API 문서에는 개발자가 이러한 요청과 응답을 구성하는 방법에 대한 정보가 들어 있습니다.

본격적으로 로보메이션의 Beagle로봇을 프로그래밍하기 위해서 Python의 라이브러리를 설치합니다.

<br>

### 1. 라이브러리 설치
터미널 창에 "pip install -U roboid"를 입력하여 roboid 라이브러리를 설치합니다.

roboid 라이브러리가 설치가 완료되었으면 beagle을 사용할 준비가 되었습니다.

Python을 이용하여 Beagle을 프로그래밍하기 위해 python 파일 첫줄에 다음과 같이 입력을 하여 roboid 라이브러리를 활성화 합니다.
```python
from roboid import*
```

<br>


### 2. 로봇과 컴퓨터 연결
"EXPRESS RECEIVER"USB를 컴퓨터에 연결

- Dongles을 컴퓨터에 연결 시 파란색 불빛으로 천천히 깜빡입니다.

    표시등이 파란색이 아니라면,

    - 접촉 불량: 동글을 살짝 눌러 접촉면을 넓게 해봅니다.
    - 포트 문제: PC의 포트 문제일수도 있으니 다른 포트에 연결해봅니다.
    - Dongles 교체

Beagle 로봇의 전원 스위치를 올린 후, 동글과 가까이 두기

- Beagle 전원을 키고 동글과 가까이 두면 삐 소리가 나고 햄스터 로봇과 동글의 불빛이 계속 파란색으로 켜지거나, 빠르게 깜빡입니다.

    - 소리가 나지 않는다면, 햄스터의 배터리가 충분한지 확인 (배터리가 없으면 충전)

<br>

**[ 간단 용어 정리 ]**
| 용어 | 뜻 |
| --- | --- |
| 인스턴스 | Beagle이라는 클래스를 사용하기 위한 객체 선언 |
| Parameter | 함수 내의 변수. f(x)의 x와 같은 의미이다. |
| Return | 반환값. y = f(x) 에서 y와 같은 의미이다. |



<br><br><br><br>
---
---
<br><br><br><br>

# 생성 및 해제
Python을 이용해서 Beagle을 프로그래밍을 하기 위해서는 먼저 PC와 Beagle을 연결시켜 Beagle객체를 사용하기 위해서는 Beagle 인스턴스를 생성해주어야 합니다.

이 차례에서는 개발환경에 Beagle인스턴스를 생성하는 것과 Beagle을 해제하는 방법에 대한 가이드라인입니다.


- [생성](#beagle)
- [해제](#dispose)

<br><br><br>

## Beagle()

변수(예: beagle)에 생성 api인 Beagle()를 대입해주어 파이썬 파일에 비글 인스턴스를 활성화합니다.

Beagle 인스턴스를 생성하고 하드웨어 비글 로봇과 통신을 연결한다. Beagle(0)을 호출한 것과 같습니다.

### 반환값
Beagle 인스턴스 참조

### 코드


```python
from roboid import *

beagle = Beagle()
```

<br>
사용예시

```python
from roboid import *

beagle = Beagle()

beagle.move_forward(50)    # beagle 앞으로 이동
```

| 설명 | |
| --- | --- |
| beagle | Beagle()클래스의 인스턴스 |
| Beagle() | 'Beagle' 클래스의 생성자를 호출하여 새로운 'Beagle'객체를 생성 |







<br><br><br>

## Beagle(index)
Beagle 인스턴스를 생성하고 하드웨어 비글 로봇과 통신을 연결한다. <br>몇 번째 비글 로봇인지를 나타내는 인덱스를 index로 설정한다. 인덱스가 같으면 같은 비글 로봇이다.

### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| index | 몇 번째 비글 로봇인지 나타내는 인덱스 | (0 이상의 정수) | - |

### 반환값

Beagle 인스턴스 참조

### 코드

```python
from roboid import *

beagle1 = Beagle(0)
beagle2 = Beagle(1)
```
<br>
사용예시

```python
from roboid import *

beagle1 = Beagle(0)
beagle2 = Beagle(1)

beagle1.move_forward(50)    # beagle1은 앞으로 이동

beagle2.move_backward(50)   # beagle2는 뒤로 이동
```
| 설명 | |
| --- | --- |
| beagle1 | Beagle()클래스의 첫번째 인스턴스 |
| beagle2 | Beagle()클래스의 두번째 인스턴스 |
| Beagle(0) | 'Beagle' 클래스의 생성자를 호출하여 'Beagle'객체를 생성하고 beagle1에 대입 |
| Beagle(1) | 'Beagle' 클래스의 생성자를 호출하여 'Beagle'객체를 생성하고 beagle2에 대입 |









<br><br><br>

## Beagle(port_name)
Beagle 인스턴스를 생성하고 port_name의 시리얼 포트를 통해 하드웨어 비글 로봇과 통신을 연결한다.<br>
Beagle(0, port_name)을 호출한 것과 같다.

### 파라미터

| Parameter | Description |
| --- | --- |
| port_name | 시리얼 포트 이름 (문자열) |

### 반환값

Beagle 인스턴스 참조

### 코드

```python
from roboid import *

beagle = Beagle('COM52')
```
<br>

| 설명 | |
| --- | --- |
| beagle | Beagle()클래스의 인스턴스 |
| Beagle('COM52') | 'Beagle' 클래스의 생성자를 호출하여 'COM52'의 시리얼 포트를 통해 하드웨어 비글 로봇과 통신을 beagle로 연결한다. |








<br><br><br>

## Beagle(index, port_name)
Beagle 인스턴스를 생성하고 port_name의 시리얼 포트를 통해 하드웨어 비글 로봇과 통신을 연결한다.<br>
몇 번째 비글 로봇인지를 나타내는 인덱스를 index로 설정한다. 인덱스가 같으면 같은 비글 로봇이다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| index | 몇 번째 비글 로봇인지 나타내는 인덱스 | (0 이상의 정수) | - |
| port_name | 시리얼 포트 이름 (문자열) |



### 반환값

Beagle 인스턴스 참조

### 코드


```python
from roboid import *

beagle1 = Beagle(0,'COM52')
beagle2 = Beagle(1,'COM53')
```
<br>

| 설명 | |
| --- | --- |
| beagle1 | Beagle()클래스의 첫번째 인스턴스 |
| beagle2 | Beagle()클래스의 두번째 인스턴스 |
| Beagle(0,'COM52') | 'Beagle' 클래스의 생성자를 호출하여 인덱스 0으로 'COM52'의 시리얼 포트를 통해 하드웨어 비글 로봇과 통신을 beagle1로 연결한다. |
| Beagle(1,'COM53') | 'Beagle' 클래스의 생성자를 호출하여 인덱스 1로 'COM53'의 시리얼 포트를 통해 하드웨어 비글 로봇과 통신을 beagle2로 연결한다. |









<br><br><br>

## dispose()
비글 로봇의 상태를 초기화하고 통신 연결을 끊는다.


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.dispose()    # 비글 로봇 연결을 끊는다.
```
<br>

| 설명 | |
| --- | --- |
| beagle | Beagle()클래스의 인스턴스 |
| beagle.dispose() | beagle 로봇의 연결을 끊는다.








<br><br><br>

## reset()
비글 로봇의 상태를 초기화한다.

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.reset()    # 비글 로봇을 초기화한다.
```
<br>

| 설명 | |
| --- | --- |
| beagle.reset() | beagle 로봇의 연결을 끊는다.








<br><br><br><br>

---
---

<br><br><br><br>






# 바퀴 움직임

이 문서에서는 연결이 완료된 비글 로봇을 앞뒤, 좌우 등 바퀴를 이용해서 여러 움직임을 높은 자유도로 원하는 프로그래밍을 할 수 있습니다.

- [전진](#전진)
- [후진](#후진)
- [스핀](#스핀)
- [피봇](#피봇)
- [바퀴제어](#바퀴-제어)

<br><br><br>

# 전진



## move_forward()

비글을 앞으로 1 초 이동한다. (기본 속도인 50%의 속도로 이동)

move_forward(1) 또는 move_forward(1,50)을 호출한 것과 같다.

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.move_forward()
```
<br>


| beagle.move_forward() | beagle 로봇을 기본속도로 앞으로 1초 이동한다. |
| --- | --- |


<br><br><br>

## move_forward(sec)

비글을 앞으로 sec 초 이동한다. (기본 속도인 50%의 속도로 이동)

move_forward(sec,50)을 호출한 것과 같다.

### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.move_forward(2)  # 기본속도로 앞으로 2초 이동한다.
```

<br><br><br>

## move_forward(sec, velocity)

sec초 앞으로 이동한다. (velocity 속도로 이동)

sec 값이 음수이면 반대 방향으로 이동한다.

velocity 값이 음수이면 반대 방향으로 이동한다.


### 파라미터


| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.move_forward(2,50)  # 50 %의 속도로 앞으로 2초 이동한다.
```



<br><br><br>

## move_forward(pulse)

펄스(pulse) 수만큼 앞으로 이동한다. (기본 속도인 50%의 속도로 이동)

move_forward_pulse(pulse, 50)을 호출한 것과 같다.

pulse 값이 음수이면 반대 방향으로 이동한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.move_forward_pulse(1000)
# 50 %의 속도로 앞으로 1000 pulse 이동한다.
```





<br><br><br>

## move_forward(pulse,velocity)

펄스(pulse) 수만큼 앞으로 이동한다. (velocity 속도로 이동)

pulse 값이 음수이면 반대 방향으로 이동한다.

velocity 값이 음수이면 반대 방향으로 이동한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.move_forward_pulse(1000,50)
# 50 %의 속도로 앞으로 1000 pulse 이동한다.
```



<br><br><br><br>

---
---



<br><br><br><Br>

# 후진


## move_backward()

비글을 뒤로 1 초 이동한다. (기본 속도인 50%의 속도로 이동)

move_backward(1) 또는 move_backward(1,50)을 호출한 것과 같다.

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.move_backward()
```
<br>


| beagle.move_backward() | beagle 로봇을 기본속도로 뒤로 1초 이동한다. |
| --- | --- |


<br><br><br>

## move_backward(sec)

비글을 뒤로 sec 초 이동한다. (기본 속도인 50%의 속도로 이동)

move_backward(sec,50)을 호출한 것과 같다.

### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.move_backward(2)  # 기본속도로 뒤로 2초 이동한다.
```

<br><br><br>

## move_backward(sec, velocity)

sec초 뒤로 이동한다. (velocity 속도로 이동)

sec 값이 음수이면 반대 방향으로 이동한다.

velocity 값이 음수이면 반대 방향으로 이동한다.


### 파라미터


| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 

### 코드


```python
from roboid import *

beagle = Beagle()

beagle.move_backward(2,50)  # 50 %의 속도로 뒤로 2초 이동한다.
```



<br><br><br>

## move_backward(pulse)

펄스(pulse) 수만큼 뒤로 이동한다. (기본 속도인 50%의 속도로 이동)

move_backward_pulse(pulse, 50)을 호출한 것과 같다.

pulse 값이 음수이면 반대 방향으로 이동한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.move_backward_pulse(1000)
# 50 %의 속도로 뒤로 1000 pulse 이동한다.
```





<br><br><br>

## move_backward(pulse,velocity)

펄스(pulse) 수만큼 뒤로 이동한다. (velocity 속도로 이동)

pulse 값이 음수이면 반대 방향으로 이동한다.

velocity 값이 음수이면 반대 방향으로 이동한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.move_backward_pulse(1000,50)
# 50 %의 속도로 뒤로 1000 pulse 이동한다.
```

<br><br><br><br>

---
---

<br><br><br><br>

# 스핀

## turn_left()

제자리에서 왼쪽으로 1초 회전한다. (기본 속도인 50%의 속도로 회전)

turn_left(1) 또는 turn_left(1, 50)을 호출한 것과 같다.

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_left()
# 50 %의 속도로 제자리에서 왼쪽으로 1초 회전한다.
```

<br><br><br>

## turn_left(sec)

sec초 제자리에서 왼쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)

turn_left(sec, 50)을 호출한 것과 같다.

sec 값이 음수이면 반대 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_left(2)
# 50 %의 속도로 제자리에서 왼쪽으로 2초 회전한다.
```


<br><br><br>

## turn_left(sec,velocity)

sec초 제자리에서 왼쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)

turn_left(sec, 50)을 호출한 것과 같다.

sec 값이 음수이면 반대 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_left(2,50)
# 50 %의 속도로 제자리에서 왼쪽으로 2초 회전한다.
```



<br><br><br>

## turn_left_pulse(pulse)

펄스(pulse) 수만큼 제자리에서 왼쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)

turn_left_pulse(pulse, 50)을 호출한 것과 같다.

pulse 값이 음수이면 반대 방향으로 회전한다.



### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_left_pulse(1000)
# 50 %의 속도로 제자리에서 왼쪽으로 1000 펄스 회전한다.
```




<br><br><br>

## turn_left_pulse(pulse,velocity)

펄스(pulse) 수만큼 제자리에서 왼쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)

pulse 값이 음수이면 반대 방향으로 회전한다.

velocity 값이 음수이면 반대 방향으로 회전한다.



### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_left_pulse(1000,50)
# 50 %의 속도로 제자리에서 왼쪽으로 1000 펄스 회전한다.
```



<br><br><br><br>

---
---

<br><br><br><br>

## turn_right()

제자리에서 오른쪽으로 1초 회전한다. (기본 속도인 50%의 속도로 회전)

turn_right(1) 또는 turn_right(1, 50)을 호출한 것과 같다.

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_right()
# 50 %의 속도로 제자리에서 오른쪽으로 1초 회전한다.
```

<br><br><br>







## turn_right(sec)

sec초 제자리에서 오른쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)

turn_right(sec, 50)을 호출한 것과 같다.

sec 값이 음수이면 반대 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_right(2)
# 50 %의 속도로 제자리에서 오른쪽으로 2초 회전한다.
```







<br><br><br>

## turn_right(sec,velocity)

sec초 제자리에서 오른쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)

turn_right(sec, 50)을 호출한 것과 같다.

sec 값이 음수이면 반대 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_right(2,50)
# 50 %의 속도로 제자리에서 오른쪽으로 2초 회전한다.
```



<br><br><br>

## turn_right_pulse(pulse)

펄스(pulse) 수만큼 제자리에서 오른쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)

turn_right_pulse(pulse, 50)을 호출한 것과 같다.

pulse 값이 음수이면 반대 방향으로 회전한다.



### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_right_pulse(1000)
# 50 %의 속도로 제자리에서 오른쪽으로 1000 펄스 회전한다.
```




<br><br><br>

## turn_right_pulse(pulse,velocity)

펄스(pulse) 수만큼 제자리에서 오른쪽으로 회전한다. (기본 속도인 50%의 속도로 회전)

pulse 값이 음수이면 반대 방향으로 회전한다.

velocity 값이 음수이면 반대 방향으로 회전한다.



### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.turn_right_pulse(1000,50)
# 50 %의 속도로 제자리에서 오른쪽으로 1000 펄스 회전한다.
```

<br><br><br><br>

---
---

<br><br><br><br>


# 피봇

## pivot_left()

왼쪽 바퀴를 중심으로 1초 회전한다. (기본 속도인 50 %의 속도로 회전)

pivot_left(1) 또는 pivot_left(1,50)을 호출한 것과 같다.

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_left()
# 50 %의 속도로 왼쪽 바퀴를 중심으로 1 초 회전한다.
```






<br><br><br>

## pivot_left(sec)

왼쪽 바퀴를 중심으로 sec초 회전한다. (기본 속도인 50%의 속도로 회전)

pivot_left(sec, 50)을 호출한 것과 같다.

sec 값이 양수이면 로봇의 앞쪽 방향으로 회전하고, 음수이면 뒤쪽 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_left(2)
# 50 %의 속도로 왼쪽 바퀴를 중심으로 2 초 회전한다.
```

<br><br><br>

## pivot_left(sec, velocity)

왼쪽 바퀴를 중심으로 sec초 회전한다. (velocity 속도로 회전)

sec 값이 양수이면 로봇의 앞쪽 방향으로 회전하고, 음수이면 뒤쪽 방향으로 회전한다.

velocity 값이 음수이면 반대 방향으로 회전한다.

### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_left(2,50)
# 50 %의 속도로 왼쪽 바퀴를 중심으로 2 초 회전한다.
```





<br><br><br>

## pivot_left_pulse(pulse)

왼쪽 바퀴를 중심으로 펄스(pulse) 수만큼 회전한다. (기본 속도인 50%의 속도로 회전)

pivot_left_pulse(pulse, 50)을 호출한 것과 같다.

pulse 값이 양수이면 로봇의 앞쪽 방향으로 회전하고, 음수이면 뒤쪽 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 



### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_left_pulse(1000)
# 50 %의 속도로 왼쪽 바퀴를 중심으로 1000 pulse 회전한다.
```





<br><br><br>

## pivot_left_pulse(pulse,velocity)

왼쪽 바퀴를 중심으로 펄스(pulse) 수만큼 회전한다. (velocity 속도로 회전)

pulse 값이 양수이면 로봇의 앞쪽 방향으로 회전하고, 음수이면 뒤쪽 방향으로 회전한다.

velocity 값이 음수이면 반대 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 



### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_left_pulse(1000,50)
# 50 %의 속도로 왼쪽 바퀴를 중심으로 1000 pulse 회전한다.
```


<br><br><br><br>

---
---

<br><br><br><br>


## pivot_right()

오른쪽 바퀴를 중심으로 1초 회전한다. (기본 속도인 50 %의 속도로 회전)

pivot_right(1) 또는 pivot_right(1,50)을 호출한 것과 같다.

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_right()
# 50 %의 속도로 오른쪽 바퀴를 중심으로 1 초 회전한다.
```






<br><br><br>

## pivot_right(sec)

오른쪽 바퀴를 중심으로 sec초 회전한다. (기본 속도인 50%의 속도로 회전)

pivot_right(sec, 50)을 호출한 것과 같다.

sec 값이 양수이면 로봇의 앞쪽 방향으로 회전하고, 음수이면 뒤쪽 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_right(2)
# 50 %의 속도로 오른쪽 바퀴를 중심으로 2 초 회전한다.
```

<br><br><br>

## pivot_right(sec, velocity)

오른쪽 바퀴를 중심으로 sec초 회전한다. (velocity 속도로 회전)

sec 값이 양수이면 로봇의 앞쪽 방향으로 회전하고, 음수이면 뒤쪽 방향으로 회전한다.

velocity 값이 음수이면 반대 방향으로 회전한다.

### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| sec | 이동할 시간 | (실수) | 초 |
| velocity | 이동할 속도 | (-100과 100 사이의  실수) | % | 


### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_right(2,50)
# 50 %의 속도로 오른쪽 바퀴를 중심으로 2 초 회전한다.
```





<br><br><br>

## pivot_right_pulse(pulse)

오른쪽 바퀴를 중심으로 펄스(pulse) 수만큼 회전한다. (기본 속도인 50%의 속도로 회전)

pivot_right_pulse(pulse, 50)을 호출한 것과 같다.

pulse 값이 양수이면 로봇의 앞쪽 방향으로 회전하고, 음수이면 뒤쪽 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 



### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_right_pulse(1000)
# 50 %의 속도로 오른쪽 바퀴를 중심으로 1000 pulse 회전한다.
```





<br><br><br>

## pivot_right_pulse(pulse,velocity)

오른쪽 바퀴를 중심으로 펄스(pulse) 수만큼 회전한다. (velocity 속도로 회전)

pulse 값이 양수이면 로봇의 앞쪽 방향으로 회전하고, 음수이면 뒤쪽 방향으로 회전한다.

velocity 값이 음수이면 반대 방향으로 회전한다.


### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| pulse | 이동할 펄스 수 | (0 이상의 정수) | - | 
| velocity | 이동할 속도 | (-100과 100사이의  실수) | % | 



### 코드

```python
from roboid import *

beagle = Beagle()

beagle.pivot_right_pulse(1000,50)
# 50 %의 속도로 오른쪽 바퀴를 중심으로 1000 pulse 회전한다.
```


<br><br><br><br>

---
---


<br><br><br><br>


# 바퀴 제어

## wheels(left_velocity, right_velocity)

왼쪽 바퀴와 오른쪽 바퀴의 속도를 설정한다.

양수 값은 전진 방향으로의 회전을 음수 값은 후진 방향으로의 회전을 의미한다.

부호를 제외한 절대치가 클 수록 속도가 빨라진다.

### 파라미터

| Parameter | Description | Range | Demension |
| -------- | -------- | --- | --- |
| left_velocity | 왼쪽 바퀴의 속도 | (-100과 100사이의 실수) | % |
| right_velocity | 오른쪽 바퀴의 속도 | (-100과 100사이의 실수) | % |

### 코드

```python
from roboid import *

beagle = Beagle()

beagle.wheels(50,50)    # 양쪽 바퀴를 50 %의 속력으로 전진한다.

beagle.wheels(-50,-50)  # 양쪽 바퀴를 50 %의 속력으로 후진한다.

beagle.wheels(0,0)      # 양쪽 바퀴를 정지한다.
```

### 설명

실제로 위 코드로는 비글이 움직이지 않는다.<br>
바퀴 제어와 제어 사이에 wait(ms)를 넣어주어야 해당 ms만큼 움직인다.



<br><br><br>

## wheels(velocity)

양쪽 바퀴의 속도를 설정한다. `wheels(velocity, velocity)`를 호출한 것과 같다. 

양수 값은 전진 방향으로의 회전을, 음수 값은 후진 방향으로의 회전을 의미한다. 

부호를 제외한 절대치가 클수록 속도가 빨라진다.

### 파라미터

| Parameter | Description | Range | Dimension |
| -------- | -------- | --- | --- |
| velocity | 양쪽 바퀴의 속도 | (-100과 100사이의  실수, 0: 정지) | % | 

### 코드

```python
from roboid import *

beagle = Beagle()

# 양쪽 바퀴를 50%의 속력으로 앞으로 회전하게 한다.
beagle.wheels(50)

# 양쪽 바퀴를 50%의 속력으로 뒤로 회전하게 한다.
beagle.wheels(-50)

# 양쪽 바퀴를 정지한다.
beagle.wheels(0)
```

<br><br><br>
## left_wheel(velocity)

왼쪽 바퀴의 속도를 설정한다. 

양수 값은 전진 방향으로의 회전을, 음수 값은 후진 방향으로의 회전을 의미한다. 

부호를 제외한 절대치가 클수록 속도가 빨라진다.

### 파라미터

| Parameter | Description | Range | Dimension |
| -------- | -------- | --- | --- |
| velocity | 왼쪽 바퀴의 속도 | (-100과 100사이의  실수, 0: 정지) | % | 

### 코드

```python
from roboid import *

beagle = Beagle()

# 왼쪽 바퀴를 50%의 속력으로 앞으로 회전하게 한다.
beagle.left_wheel(50)

# 왼쪽 바퀴를 50%의 속력으로 뒤로 회전하게 한다.
beagle.left_wheel(-50)

# 왼쪽 바퀴를 정지한다.
beagle.left_wheel(0)
```





<br><br><br>

## right_wheel(velocity)

오른쪽 바퀴의 속도를 설정한다. 

양수 값은 전진 방향으로의 회전을, 음수 값은 후진 방향으로의 회전을 의미한다. 

부호를 제외한 절대치가 클수록 속도가 빨라진다.

### 파라미터

| Parameter | Description | Range | Dimension |
| -------- | -------- | --- | --- |
| velocity | 오른쪽 바퀴의 속도 | (-400과 400사이의  실수, 0: 정지) | % | 

### 코드

```python
from roboid import *

beagle = Beagle()

# 오른쪽 바퀴를 50%의 속력으로 앞으로 회전하게 한다.
beagle.right_wheel(50)

# 오른쪽 바퀴를 50%의 속력으로 뒤로 회전하게 한다.
beagle.right_wheel(-50)

# 오른쪽 바퀴를 정지한다.
beagle.right_wheel(0)
```

<br><br><br>


## stop()

양쪽 바퀴를 정지한다. `wheels(0, 0)` 또는 `wheels(0)`을 호출한 것과 같다.

### 코드

```python
from roboid import *

beagle = Beagle()

# 50%의 속력으로 앞으로 이동한다.
beagle.wheels(50, 50)

# 양쪽 바퀴를 정지한다.
beagle.stop()
```

<br><br><br><br>

---
---

<br><br><br><br>


## buzzer(hz)

버저 소리의 음 높이 주파수를 `hz` [Hz]로 설정한다. 음 높이는 소수점 첫째 자리까지 입력할 수 있으며, 버저 소리를 끄기 위해서는 0을 입력하면 된다.

### 파라미터

| Parameter | Description | Range | Dimension |
| --------- | ----------- | ----- | --------- |
| hz        | 버저 소리의 음 높이 | (0 ~ 167772.15 [Hz], 0: off) | Hz |

### 코드

```python
from roboid import *

beagle = Beagle()

# 버저 소리의 음 높이를 1000 Hz로 한다.
beagle.buzzer(1000)

# 버저 소리의 음 높이를 261.6 Hz로 한다.
beagle.buzzer(261.6)

# 버저 소리를 끈다.
beagle.buzzer(0)
```

<br><br><br>


## tempo(bpm)

연주하거나 쉬는 속도를 `bpm` (분당 박자 수)으로 설정한다.

### 파라미터

| Parameter | Description | Range | Dimension |
| --------- | ----------- | ----- | --------- |
| bpm       | 분당 박자 수 | (실수 [BPM], 초기 값: 60) | BPM |

### 코드

```python
from roboid import *

beagle = Beagle()

# 연주 속도를 60 BPM으로 한다.
beagle.tempo(60)
```


<br><br><br>


## note(pitch)

버저를 이용하여 오차가 0.01% 이하인 정확한 음정으로 소리를 낸다.

### 음의 높이

음의 높이를 설정하여 소리를 낼 수 있으며, 다음은 각 음에 대한 설명이다:

- "OFF": 소리를 끈다.
- "C4": 4번째 옥타브의 도 음
- "C#4" 또는 "Db4": 4번째 옥타브의 도#(레b) 음
- "D4": 4번째 옥타브의 레 음
- "D#4" 또는 "Eb4": 4번째 옥타브의 레#(미b) 음
- "E4": 4번째 옥타브의 미 음
- "F4": 4번째 옥타브의 파 음
- "F#4" 또는 "Gb4": 4번째 옥타브의 파#(솔b) 음
- "G4": 4번째 옥타브의 솔 음
- "G#4" 또는 "Ab4": 4번째 옥타브의 솔#(라b) 음
- "A4": 4번째 옥타브의 라 음
- "A#4" 또는 "Bb4": 4번째 옥타브의 라#(시b) 음
- "B4": 4번째 옥타브의 시 음

### 파라미터

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| pitch     | 음의 높이    | "C#5"   |

### 코드

```python
from roboid import *

beagle = Beagle()

# 5옥타브 도# 음을 소리 낸다.
beagle.note("C#5")

# 소리를 끈다.
beagle.note("OFF")
```


<br><br><br>

## note(pitch, beats)

버저를 이용하여 오차가 0.01% 이하인 정확한 음정을 `beats` 박자 만큼 소리를 낸다.

### 음의 높이

음의 높이를 설정하여 소리를 낼 수 있으며, 다음은 각 음에 대한 설명이다:

- "OFF": 소리를 끈다.
- "C4": 4번째 옥타브의 도 음
- "C#4" 또는 "Db4": 4번째 옥타브의 도#(레b) 음
- "D4": 4번째 옥타브의 레 음
- "D#4" 또는 "Eb4": 4번째 옥타브의 레#(미b) 음
- "E4": 4번째 옥타브의 미 음
- "F4": 4번째 옥타브의 파 음
- "F#4" 또는 "Gb4": 4번째 옥타브의 파#(솔b) 음
- "G4": 4번째 옥타브의 솔 음
- "G#4" 또는 "Ab4": 4번째 옥타브의 솔#(라b) 음
- "A4": 4번째 옥타브의 라 음
- "A#4" 또는 "Bb4": 4번째 옥타브의 라#(시b) 음
- "B4": 4번째 옥타브의 시 음

### 파라미터

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| pitch     | 음의 높이    | "C#5"   |
| beats     | 박자        | 0.5     |

### 코드

```python
from roboid import *

beagle = Beagle()

# 5옥타브 도# 음을 0.5 박자 소리낸다.
beagle.note("C#5", 0.5)

# 0.5 박자 쉰다.
beagle.note("OFF", 0.5)
```


<br><br><br>




## sound(sound_id)

`sound_id`에 해당하는 소리를 재생한다. 소리를 끄기 위해서는 `sound_id`에 “OFF”를 입력하면 된다. `sound_until_done` 메소드와는 달리 소리를 재생하라고 명령하기만 할 뿐, 소리의 재생이 끝날 때까지 기다리지는 않는다.

### 소리 목록

다음은 각 `sound_id`에 대한 설명이다:

- "OFF": 소리를 끈다.
- "BEEP": 삐 소리를 재생한다.
- "RANDOM BEEP": 무작위 음 높이의 삐 소리를 재생한다.
- "NOISE": 지지직 소리를 재생한다.
- "SIREN": 사이렌 소리를 재생한다.
- "ENGINE": 엔진 소리를 재생한다.
- "CHOP": 쩝 소리를 재생한다.
- "ROBOT": 로봇 소리를 재생한다.
- "DIBIDIBIDIP": 디비디비딥 소리를 재생한다.
- "GOOD JOB": 칭친하는 소리를 재생한다.
- "HAPPY": 행복 음악을 재생한다.
- "ANGRY": 화남 음악을 재생한다.
- "SAD": 슬픔 음악을 재생한다.
- "SLEEP": 졸림 음악을 재생한다.
- "MARCH": 행진 음악을 재생한다.
- "BIRTHDAY": 생일 축하 음악을 재생한다.

### 파라미터

| Parameter | Description |
| --------- | ----------- |
| sound_id  | 재생할 소리(대소문자 구분하지 않음) |

### 코드

```python
from roboid import *

beagle = Beagle()

# 엔진 소리를 내면서 앞으로 이동한다.
beagle.sound("ENGINE")
beagle.move_forward()
```


<br><br><br>





## sound(sound_id, repeat)

`sound_id`에 해당하는 소리를 `repeat`번 재생한다. 소리를 끄기 위해서는 `sound_id`에 “OFF”를 입력하면 된다. `repeat`가 음수 값이면 영원히 반복하여 재생한다.

### 파라미터

| Parameter | Description |
| --------- | ----------- |
| sound_id  | 재생할 소리(대소문자 구분하지 않음) |
| repeat    | 재생할 횟수(정수) |

### 코드

```python
from roboid import *

beagle = Beagle()

# 엔진 소리를 2번 내면서 앞으로 이동한다.
beagle.sound("ENGINE", 2)
beagle.move_forward()

# 로봇 소리를 영원히 반복하여 재생한다.
beagle.sound("ROBOT", -1)
wait(-1)
```


<br><br><br>






## beep()

삐 소리를 재생하고 소리의 재생이 끝날 때까지 기다린다. `sound_until_done('beep')`를 호출한 것과 같다.

### 코드

```python
from roboid import *

beagle = Beagle()

# 삐 소리를 재생한다.
beagle.beep()
```
<br><br><br>



<br><br><br><br>

---
---

<br><br><br><br>

# 센서

## signal_strength()

신호 세기 값을 반환한다. 비글 로봇과 컴퓨터 간의 블루투스 무선 통신의 신호 세기를 나타낸다. 신호의 세기가 셀수록 값이 커진다.

### 반환값

| Return | Range | Dimension |
| ----------- | ----- | --------- |
| 신호 세기 값 | (정수, -128 ~ 0 [dBm], 초기 값: 0) | BPM |



### 코드

```python
from roboid import *

beagle = Beagle()

# 신호 세기 값을 얻는다.
value = beagle.signal_strength()
```
<br><br><br>




## temperature()

온도 센서 값을 반환한다. 로봇 내부의 온도 값이다.

### 반환값

| Return | Range | Dimension |
| ----------- | ----- | --------- |
| 온도 센서 값 | (정수, -41 ~ 87 [&deg;C], 초기 값: 0) | &deg;C |


### 코드

```python
from roboid import *

beagle = Beagle()

# 온도 센서 값을 얻는다.
value = beagle.temperature()
```
<br><br><br>





## left_encoder()

왼쪽 바퀴의 엔코더 값을 반환한다. 바퀴가 앞쪽 방향으로 회전하면 값이 증가하고 뒤쪽 방향으로 회전하면 값이 감소한다.

### 반환값

| Return | Range | Dimension |
| ----------- | ----------------------- | --------- |
| 왼쪽 바퀴의 엔코더 펄스 수 | (정수, -2147483648 ~ 2147483647, 초기 값: 0) | - |


### 예시

```python
from roboid import *

beagle = Beagle()

# 왼쪽 바퀴의 엔코더 값을 얻는다.
value = beagle.left_encoder()
```
<br><br><br>






## right_encoder()

오른쪽 바퀴의 엔코더 값을 반환한다. 바퀴가 앞쪽 방향으로 회전하면 값이 증가하고 뒤쪽 방향으로 회전하면 값이 감소한다.

### 반환 값

| Return | Range | Dimension |
| ----------- | ----------------------- | --------- |
| 오른쪽 바퀴의 엔코더 펄스 수 | (정수, -2147483648 ~ 2147483647, 초기 값: 0) | - |


### 예시

```python
from roboid import *

beagle = Beagle()

# 오른쪽 바퀴의 엔코더 값을 얻는다.
value = beagle.right_encoder()
```
<br><br><br>






## reset_encoder()

양쪽 바퀴의 엔코더 값을 초기화한다.

### 예시

```python
from roboid import *

beagle = Beagle()

# 엔코더 값을 초기화한다.
beagle.reset_encoder()
```
<br><br><br>






## accelerometer_x()

X축 가속도 센서 값을 반환합니다. 비글 로봇의 가속도 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------------ | ------- | --------- |
| X축 가속도 센서 값 | (실수, -16 ~ 16, 초기 값: 0) | $$g=9.8 m/s^2$$ |


### 코드

```python
from roboid import *

beagle = Beagle()

# X축 가속도 값을 얻습니다.
value = beagle.accelerometer_x()
```
<br><br><br>






## accelerometer_y()

Y축 가속도 센서 값을 반환합니다. 비글 로봇의 가속도 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------------ | ------- | --------- |
| y축 가속도 센서 값 | (실수, -16 ~ 16, 초기 값: 0) | $$g=9.8 m/s^2$$ |

### 코드

```python
from roboid import *

beagle = Beagle()

# Y축 가속도 값을 얻습니다.
value = beagle.accelerometer_y()
```

<br><br><br>






## accelerometer_z()

Z축 가속도 센서 값을 반환합니다. 비글 로봇의 가속도 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------------ | ------- | --------- |
| z축 가속도 센서 값 | (실수, -16 ~ 16, 초기 값: 0) | $g=9.8 m/s^2$ |

### 코드

```python
from roboid import *

beagle = Beagle()

# Z축 가속도 값을 얻습니다.
value = beagle.accelerometer_z()
```
<br><br><br>






## accelerometer()

X, Y, Z축 가속도 센서 값을 반환합니다. 비글 로봇의 가속도 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Description | Range | Dimension |
| ------ | ----------- | ----- | --------- |
| index  | 센서 값의 인덱스 | (정수) | - |
| x      | X축 가속도 센서 값 | (실수, -16 ~ 16, 초기 값: 0) | $g=9.8 m/s^2$ |
| y      | Y축 가속도 센서 값 | (실수, -16 ~ 16, 초기 값: 0) | $g=9.8 m/s^2$ |
| z      | Z축 가속도 센서 값 | (실수, -16 ~ 16, 초기 값: 0) | $g=9.8 m/s^2$ |

### 코드

```python
from roboid import *

beagle = Beagle()

# 가속도 값을 얻습니다.
index, x, y, z = beagle.accelerometer()
```
<br><br><br>






## raw_accelerometer_x()

스케일 값을 곱하지 않은 X축 가속도 센서 값을 반환합니다. 비글 로봇의 가속도 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| X축 가속도 센서 값 | (-2048 ~ 2047, 초기 값: 0) | - |

$$ 9.8 m/s^2 = 1010 $$
$$ 1 m/s^2 = 103 $$

### 코드

```python
from roboid import *

beagle = Beagle()

# X축 가속도 값을 얻습니다.
value = beagle.raw_accelerometer_x()
```
<br><br><br>



## raw_accelerometer_y()

스케일 값을 곱하지 않은 Y축 가속도 센서 값을 반환합니다. 비글 로봇의 가속도 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| Y축 가속도 센서 값 | (-2048 ~ 2047, 초기 값: 0) | - |

$$ 9.8 m/s^2 = 1010 $$
$$ 1 m/s^2 = 103 $$

### 코드

```python
from roboid import *

beagle = Beagle()

# Y축 가속도 값을 얻습니다.
value = beagle.raw_accelerometer_y()
```

<br><br><br>

## raw_accelerometer_z()

스케일 값을 곱하지 않은 Y축 가속도 센서 값을 반환합니다. 비글 로봇의 가속도 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| Y축 가속도 센서 값 | (-2048 ~ 2047, 초기 값: 0) | - |

$$ 9.8 m/s^2 = 1010 $$
$$ 1 m/s^2 = 103 $$

### 코드

```python
from roboid import *

beagle = Beagle()

# Z축 가속도 값을 얻습니다.
value = beagle.raw_accelerometer_z()
```
<br><br><br>


## raw_accelerometer()

스케일 값을 곱하지 않은 X, Y, Z축 가속도 센서 값을 반환합니다. 비글 로봇의 가속도 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| Index | - | - |
| X축 가속도 센서 값 | (-2048 ~ 2047, 초기 값: 0) | - |
| Y축 가속도 센서 값 | (-2048 ~ 2047, 초기 값: 0) | - |
| Z축 가속도 센서 값 | (-2048 ~ 2047, 초기 값: 0) | - |

$$ 9.8 m/s^2 = 1010 $$
$$ 1 m/s^2 = 103 $$

### 코드

```python
from roboid import *

beagle = Beagle()

# 가속도 값을 얻습니다.
index, x, y, z = beagle.raw_accelerometer()
```
<br><br><br>


## scale_accelerometer()

가속도 센서의 스케일 값을 반환합니다.
이는  센서의 resolution을 나타내며, 스케일 값이 0.0009765625이면 센서가 1G의 가속도를 측정할 때 해당하는 디지털 값이 1에 가깝게 됩니다.

### 반환 값

| Scale 값 | Range | Demension |
| -------- | --- | --- |
| 가속도 센서의 스케일 값 | (실수, 0.0009765625 ~ 0.0078125, 초기 값: 0.0009765625) | - |

$$ 0.0009765625 \mathrm{[G/bit]} \times 1024 \mathrm {[bit]} = 1 \mathrm [G] $$

### 코드

```python
from roboid import *

beagle = Beagle()

# 스케일 값을 얻습니다.
scale = beagle.scale_accelerometer()
print(beagle.accelerometer_x() == beagle.raw_accelerometer_x() * scale)
```
<br><br><br>

## listen_accelerometer(fn, interpolation=None)

가속도 센서 값을 얻기 위한 리스너 함수 `fn`을 설정합니다. <br>리스너 함수는 `fn(index, timestamp, x, y, z)`의 형태를 가집니다. <br>함수 이름이 `fn`일 필요는 없습니다. 새로운 가속도 센서 값을 얻으면 `fn` 함수가 호출됩니다. <br>`index`는 센서 값의 인덱스, `timestamp`는 센서 값을 측정한 시간(보간한 경우에는 보간한 때의 시간), `x`는 X축 가속도 센서 값, `y`는 Y축 가속도 센서 값, `z`는 Z축 가속도 센서 값입니다. <br>함수 내에서 시간을 끌면 안 됩니다.

### 파라미터
- `fn`: 새로운 가속도 센서 값을 얻었을 때 호출할 함수
- `interpolation`:
    - `None`: 보간법 적용하지 않음
    - `'constant'`: 이전 값으로 채우기
    - `'linear'`: 선으로 이어서 샘플링

### 예시

```python
from roboid import *

beagle = Beagle()

# 리스너 함수를 정의합니다.
def listener(index, timestamp, x, y, z):
    print(index, timestamp, x, y, z)

beagle.listen_accelerometer(listener)
```
<br><br><br>






## listen_raw_accelerometer(fn, interpolation=None)

스케일 값을 곱하지 않은 가속도 센서 값을 얻기 위한 리스너 함수 `fn`을 설정합니다. 리스너 함수는 `fn(index, timestamp, x, y, z)`의 형태를 가집니다. 함수 이름이 `fn`일 필요는 없습니다. 새로운 가속도 센서 값을 얻으면 `fn` 함수가 호출됩니다. `index`는 센서 값의 인덱스, `timestamp`는 센서 값을 측정한 시간(보간한 경우에는 보간한 때의 시간), `x`는 X축 가속도 센서 값, `y`는 Y축 가속도 센서 값, `z`는 Z축 가속도 센서 값입니다. 함수 내에서 시간을 끌면 안 됩니다.

### 파라미터
- `fn`: 새로운 가속도 센서 값을 얻었을 때 호출할 함수
- `interpolation`:
    - `None`: 보간법 적용하지 않음
    - `'constant'`: 이전 값으로 채우기
    - `'linear'`: 선으로 이어서 샘플링

### 예시

```python
from roboid import *

beagle = Beagle()

# 리스너 함수를 정의합니다.
def listener(index, timestamp, x, y, z):
    print(index, timestamp, x, y, z)

beagle.listen_raw_accelerometer(listener)
```

<br><br><br>

## gyroscope_x()

X축에 대한 자이로 센서 값을 반환합니다. 비글 로봇의 자이로 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| X축 자이로 센서 값 | (-2000 ~ 2000, 초기 값: 0) | °/s |

### 코드

```python
from roboid import *

beagle = Beagle()

# X축 자이로 값을 얻습니다.
value = beagle.gyroscope_x()
```


<br><br><br>

## gyroscope_y()

Y축에 대한 자이로 센서 값을 반환합니다. 비글 로봇의 자이로 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| Y축 자이로 센서 값 | (-2000 ~ 2000, 초기 값: 0) | °/s |

### 코드

```python
from roboid import *

beagle = Beagle()

# Y축 자이로 값을 얻습니다.
value = beagle.gyroscope_y()
```


<br><br><br>

## gyroscope_z()

Z축에 대한 자이로 센서 값을 반환합니다. 비글 로봇의 자이로 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| Z축 자이로 센서 값 | (-2000 ~ 2000, 초기 값: 0) | °/s |

### 코드

```python
from roboid import *

beagle = Beagle()

# Z축 자이로 값을 얻습니다.
value = beagle.gyroscope_z()
```


<br><br><br>

## gyroscope()

X, Y, Z축에 대한 자이로 센서 값을 반환합니다. 비글 로봇의 자이로 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| Index | - | - |
| X축 자이로 센서 값 | (-2000 ~ 2000, 초기 값: 0) | °/s |
| Y축 자이로 센서 값 | (-2000 ~ 2000, 초기 값: 0) | °/s |
| Z축 자이로 센서 값 | (-2000 ~ 2000, 초기 값: 0) | °/s |


### 코드

```python
from roboid import *

beagle = Beagle()

# 자이로 값을 얻습니다.
index, x, y, z = beagle.gyroscope()
```



<br><br><br>


## raw_gyroscope_x()

X축에 대한 자이로 센서 값을 스케일 값을 곱하지 않은 상태로 반환합니다. 비글 로봇의 자이로 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| X축 자이로 센서 값 | (-32768 ~ 32767, 초기 값: 0) | - |

### 코드

```python
from roboid import *

beagle = Beagle()

# X축 자이로 값을 얻습니다.
value = beagle.raw_gyroscope_x()
```





<br><br><br>


## raw_gyroscope_y()

Y축에 대한 자이로 센서 값을 스케일 값을 곱하지 않은 상태로 반환합니다. 비글 로봇의 자이로 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| Y축 자이로 센서 값 | (-32768 ~ 32767, 초기 값: 0) | - |

### 코드

```python
from roboid import *

beagle = Beagle()

# Y축 자이로 값을 얻습니다.
value = beagle.raw_gyroscope_y()
```
<br><br><br>


## raw_gyroscope_z()

Z축에 대한 자이로 센서 값을 스케일 값을 곱하지 않은 상태로 반환합니다. 비글 로봇의 자이로 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| Z축 자이로 센서 값 | (-32768 ~ 32767, 초기 값: 0) | - |

### 코드

```python
from roboid import *

beagle = Beagle()

# Z축 자이로 값을 얻습니다.
value = beagle.raw_gyroscope_z()
```
<br><br><br>

## raw_gyroscope()

X, Y, Z축에 대한 자이로 센서 값을 반환합니다. 비글 로봇의 자이로 센서 좌표계는 로봇이 전진하는 방향이 X축, 로봇의 왼쪽 방향이 Y축, 위쪽 방향이 Z축의 양수 방향입니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| Index | - | - |
| X축 자이로 센서 값 | (-32768 ~ 32767, 초기 값: 0) | - |
| Y축 자이로 센서 값 | (-32768 ~ 32767, 초기 값: 0) | - |
| Z축 자이로 센서 값 | (-32768 ~ 32767, 초기 값: 0) | - |

### 코드

```python
from roboid import *

beagle = Beagle()

# 자이로 값을 얻습니다.
index, x, y, z = beagle.raw_gyroscope()
```

<br><br><br>

## scale_gyroscope()

자이로 센서의 스케일 값을 반환합니다.

### 반환 값

| Scale 값 | Range | Dimension |
| -------- | ----- | --------- |
| 자이로 센서의 스케일 값 | (실수, 0.003814697265625 ~ 0.06103515625, 초기 값: 0.00762939453125) | - |

### 코드

```python
from roboid import *

beagle = Beagle()

# 스케일 값을 얻습니다.
scale = beagle.scale_gyroscope()
print(beagle.gyroscope_x() == beagle.raw_gyroscope_x() * scale)
```


<br><br><br>


## listen_gyroscope(fn, interpolation=None)

자이로 센서 값을 얻기 위한 리스너 함수 `fn`을 설정합니다. 리스너 함수는 `fn(index, timestamp, x, y, z)`의 형태를 가집니다. 함수 이름이 `fn`일 필요는 없습니다. 새로운 자이로 센서 값을 얻으면 `fn` 함수가 호출됩니다. `index`는 센서 값의 인덱스, `timestamp`는 센서 값을 측정한 시간(보간한 경우에는 보간한 때의 시간), `x`는 X축 자이로 센서 값, `y`는 Y축 자이로 센서 값, `z`는 Z축 자이로 센서 값입니다. 함수 내에서 시간을 변경하면 안 됩니다.

### 파라미터

- `fn`: 새로운 자이로 센서 값을 얻었을 때 호출할 함수
- `interpolation`:
    - None: 보간법을 적용하지 않습니다.
    - 'constant': 이전 값으로 채웁니다.
    - 'linear': 선으로 이어서 샘플링합니다.

### 예제

```python
from roboid import *

beagle = Beagle()

# 리스너 함수를 정의합니다.
def listener(index, timestamp, x, y, z):
    print(index, timestamp, x, y, z)

beagle.listen_gyroscope(listener)
```


<br><br><br>


## listen_raw_gyroscope(fn, interpolation=None)

스케일 값을 곱하지 않은 자이로 센서 값을 얻기 위한 리스너 함수 `fn`을 설정합니다. 리스너 함수는 `fn(index, timestamp, x, y, z)`의 형태를 가집니다. 함수 이름이 `fn`일 필요는 없습니다. 새로운 자이로 센서 값을 얻으면 `fn` 함수가 호출됩니다. `index`는 센서 값의 인덱스, `timestamp`는 센서 값을 측정한 시간(보간한 경우에는 보간한 때의 시간), `x`는 X축 자이로 센서 값, `y`는 Y축 자이로 센서 값, `z`는 Z축 자이로 센서 값입니다. 함수 내에서 시간을 변경하면 안 됩니다.

### 파라미터

- `fn`: 새로운 자이로 센서 값을 얻었을 때 호출할 함수
- `interpolation`:
    - None: 보간법을 적용하지 않습니다.
    - 'constant': 이전 값으로 채웁니다.
    - 'linear': 선으로 이어서 샘플링합니다.

### 예제

```python
from roboid import *

beagle = Beagle()

# 리스너 함수를 정의합니다.
def listener(index, timestamp, x, y, z):
    print(index, timestamp, x, y, z)

beagle.listen_raw_gyroscope(listener)
```

<br><br><br>


## tilt()

비글 로봇의 기울임 상태 값을 반환합니다.

### 반환 값

| 기울임 상태 값 | 설명 |
| -------------- | ---- |
| 1 | 앞으로 기울임 |
| -1 | 뒤로 기울임 |
| 2 | 왼쪽으로 기울임 |
| -2 | 오른쪽으로 기울임 |
| 3 | 거꾸로 뒤집음 |
| -3 | 똑바로 놓음 |

### 예제

```python
from roboid import *

beagle = Beagle()

# 기울임 상태 값을 얻습니다.
value = beagle.tilt()
```



<br><br><br>





## battery_state()

배터리 상태 값을 반환합니다.

### 반환 값

| 배터리 상태 값 | 설명 |
| -------------- | ---- |
| 3 | 정상 |
| 2 | 중간 |
| 1 | 부족 |
| 0 | 없음 |

### 예제

```python
from roboid import *

beagle = Beagle()

# 배터리 상태 값을 얻습니다.
value = beagle.battery_state()
```


<br><br><br>

## charge_state()

충전 상태 값을 반환합니다.

### 반환 값

| 충전 상태 값 | 설명          |
| ------------ | ------------- |
| 1            | 충전 중       |
| 0            | 충전 중 아님 |

### 예제

```python
from roboid import *

beagle = Beagle()

# 충전 상태 값을 얻습니다.
value = beagle.charge_state()
```



<br><br><br>





## timestamp_basic()

IMU 센서를 제외한 기본 센서 값들을 측정한 시간을 반환합니다.

### 반환 값

기본 센서 값들을 측정한 시간(정수)

### 예제

```python
from roboid import *

beagle = Beagle()

# 기본 센서 값들을 측정한 시간을 얻습니다.
value = beagle.timestamp_basic()
```


<br><br><br>

## timestamp_imu()

IMU 센서(가속도, 자이로 등) 값들을 측정한 시간을 반환합니다.

### 반환 값

센서 값들을 측정한 시간(정수)

### 예제

```python
from roboid import *

beagle = Beagle()

# IMU 센서 값들을 측정한 시간을 얻습니다.
value = beagle.timestamp_imu()
```


<br><br><br>


<br><br><br><br>

---
---

<br><br><br><br>


# 서보 모터

<br>

## servo_output_a(degree)

서보 모터 A를 지정한 각도로 회전시킵니다. 이 메소드는 회전 완료를 기다리지 않습니다.

### Parameters

| Parameter | Range | Dimension |
| --------- | ----- | --------- |
| degree    | (정수, 0 ~ 180) | 도 |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 A를 30도로 회전시킵니다.
beagle.servo_output_a(30)
```
<br><br><br>



## servo_output_b(degree)

서보 모터 B를 지정한 각도로 회전시킵니다. 이 메소드는 회전 완료를 기다리지 않습니다.

### Parameters

| Parameter | Range | Dimension |
| --------- | ----- | --------- |
| degree    | (정수, 0 ~ 180) | 도 |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 B를 30도로 회전시킵니다.
beagle.servo_output_b(30)
```

<br><br><br>
## servo_output_c(degree)

서보 모터 C를 지정한 각도로 회전시킵니다. 이 메소드는 회전 완료를 기다리지 않습니다.

### Parameters

| Parameter | Range | Dimension |
| --------- | ----- | --------- |
| degree    | (정수, 0 ~ 180) | 도 |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 C를 30도로 회전시킵니다.
beagle.servo_output_c(30)
```


<br><br><br>

## servo_output_a_until_done(degree)

서보 모터 A를 지정한 각도로 회전시키고 회전이 완료될 때까지 기다립니다.

### Parameters

| Parameter | Range | Dimension |
| --------- | ----- | --------- |
| degree    | (정수, 0 ~ 180) | 도 |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 A를 30도로 회전시키고 회전이 완료될 때까지 기다립니다.
beagle.servo_output_a_until_done(30)
```

<br><br><br>
## servo_output_b_until_done(degree)

서보 모터 B를 degree 각도로 회전시키고 회전이 완료될 때까지 기다립니다.

### Parameters

| Parameter | Range | Dimension |
| --------- | ----- | --------- |
| degree    | (정수, 0 ~ 180) | 도 |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 B를 30도로 회전시키고 회전이 완료될 때까지 기다립니다.
beagle.servo_output_b_until_done(30)
```



<br><br><br>




## servo_output_c_until_done(degree)

서보 모터 C를 degree 각도로 회전시키고 회전이 완료될 때까지 기다립니다.

### Parameters

| Parameter | Range | Dimension |
| --------- | ----- | --------- |
| degree    | (정수, 0 ~ 180) | 도 |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 C를 30도로 회전시키고 회전이 완료될 때까지 기다립니다.
beagle.servo_output_c_until_done(30)
```


<br><br><br>


## servo_speed_a(speed)

서보 모터 A의 속도를 지정된 값으로 설정합니다.

### Parameters

| Parameter | Range | Dimension |
| --------- | ----- | --------- |
| speed     | (정수, 1 ~ 7) | - |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 A의 속도를 3으로 설정합니다.
beagle.servo_speed_a(3)
```


<br><br><br>



## servo_speed_b(speed)

서보 모터 B의 속도를 지정된 값으로 설정합니다.

### Parameters

| Parameter | Range | Dimension |
| --------- | ----- | --------- |
| speed     | (정수, 1 ~ 7) | - |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 B의 속도를 3으로 설정합니다.
beagle.servo_speed_b(3)
```


<br><br><br>





## servo_speed_c(speed)

서보 모터 C의 속도를 지정된 값으로 설정합니다.

### Parameters

| Parameter | Range | Dimension |
| --------- | ----- | --------- |
| speed     | (정수, 1 ~ 7) | - |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 C의 속도를 3으로 설정합니다.
beagle.servo_speed_c(3)
```


<br><br><br>



## release_servo_a()

서보 모터 A의 전원을 끕니다.

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 A의 전원을 끕니다.
beagle.release_servo_a()
```

<br><br><br>



## release_servo_b()

서보 모터 B의 전원을 끕니다.

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 B의 전원을 끕니다.
beagle.release_servo_b()
```




## release_servo_c()

서보 모터 C의 전원을 끕니다.

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 C의 전원을 끕니다.
beagle.release_servo_c()
```

<br><br><br>


## servo_input_a()

서보 모터 A의 현재 각도 값을 반환합니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| 현재 각도 값 | (정수, 0 ~ 180, 초기 값: 0) | 도 |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 A의 현재 각도 값을 얻습니다.
value = beagle.servo_input_a()
```

<br><br><br>

## servo_input_b()

서보 모터 B의 현재 각도 값을 반환합니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| 현재 각도 값 | (정수, 0 ~ 180, 초기 값: 0) | 도 |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 B의 현재 각도 값을 얻습니다.
value = beagle.servo_input_b()
```


## servo_input_c()

서보 모터 C의 현재 각도 값을 반환합니다.

### 반환 값

| Return | Range | Dimension |
| ------ | ----- | --------- |
| 현재 각도 값 | (정수, 0 ~ 180, 초기 값: 0) | 도 |

### 코드

```python
from roboid import *

beagle = Beagle()

# 서보 모터 C의 현재 각도 값을 얻습니다.
value = beagle.servo_input_c()
```



<br><br><br>


<br><br><br><br>

---
---

<br><br><br><br>

# LiDar

<br>

## start_lidar()

라이다를 시작합니다. 시작한 후 실제 값이 들어오기까지 시간이 좀 걸립니다.

### 코드

```python
from roboid import *

beagle = Beagle()

# 라이다를 시작합니다.
beagle.start_lidar()
```


<br><br><br>

## stop_lidar()

라이다를 종료합니다.

### 코드

```python
from roboid import *

beagle = Beagle()

# 라이다를 종료합니다.
beagle.stop_lidar()
```


<br><br><br>

## is_lidar_ready()

라이다가 준비되었는지(센서 값을 얻는 상태가 되었는지) 여부를 반환합니다.

### Returns

| Return | Description |
| ------ | ----------- |
| True   | 라이다가 준비된 상태일 때 |
| False  | 라이다가 아직 준비되지 않은 상태일 때 |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다가 준비되었는지 확인합니다.
value = beagle.is_lidar_ready()
```

<br><br><br>



## wait_until_lidar_ready()

라이다가 준비될 때까지 기다립니다.

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다가 준비될 때까지 기다립니다.
value = beagle.wait_until_lidar_ready()
```



<br><br><br>




## lidar()

라이다 센서 값을 반환합니다.

### 반환 값

| Return | Range | Dimension |
| -- | -- | -- |
| LiDar 센서 값 | (1도 간격, 360개 정수의 리스트)<br> 각 값의 정상 범위 : (0~65534) <br> 센서 값이 유하지 않으면 65535 | [mm] |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서 값을 얻습니다.
values = beagle.lidar()
```
<br><br><br>


## left_lidar()

라이다 센서의 왼쪽 영역 값들의 평균 값을 반환합니다.

### 반환 값

| Value Range         | Dimension | Description                      |
|---------------------|-----------|----------------------------------|
| 0 ~ 65534           | mm        | 정상적인 센서 값의 평균           |
| 65535               | -         | 센서 값이 유효하지 않음          |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서의 왼쪽 영역 평균 값을 얻습니다.
value = beagle.left_lidar()
```

<br><br><br>


## right_lidar()

라이다 센서의 오른쪽 영역 값들의 평균 값을 반환합니다.

### 반환 값

| Value Range         | Dimension | Description                      |
|---------------------|-----------|----------------------------------|
| 0 ~ 65534           | mm        | 정상적인 센서 값의 평균           |
| 65535               | -         | 센서 값이 유효하지 않음          |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서의 오른쪽 영역 평균 값을 얻습니다.
value = beagle.right_lidar()
```



<br><br><br>

## front_lidar()

라이다 센서의 앞쪽 영역 값들의 평균 값을 반환합니다.

### 반환 값

| Value Range         | Dimension | Description                      |
|---------------------|-----------|----------------------------------|
| 0 ~ 65534           | mm        | 정상적인 센서 값의 평균           |
| 65535               | -         | 센서 값이 유효하지 않음          |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서의 앞쪽 영역 평균 값을 얻습니다.
value = beagle.front_lidar()
```

<br><br><br>





## rear_lidar()

라이다 센서의 뒤쪽 영역 값들의 평균 값을 반환합니다.

### 반환 값

| Value Range         | Dimension | Description                      |
|---------------------|-----------|----------------------------------|
| 0 ~ 65534           | mm        | 정상적인 센서 값의 평균           |
| 65535               | -         | 센서 값이 유효하지 않음          |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서의 뒤쪽 영역 평균 값을 얻습니다.
value = beagle.rear_lidar()
```

<br><br><br>



## left_front_lidar()

라이다 센서의 왼쪽 앞 영역 값들의 평균 값을 반환합니다.

### 반환 값

| Value Range         | Dimension | Description                      |
|---------------------|-----------|----------------------------------|
| 0 ~ 65534           | mm        | 정상적인 센서 값의 평균           |
| 65535               | -         | 센서 값이 유효하지 않음          |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서의 왼쪽 앞 영역 평균 값을 얻습니다.
value = beagle.left_front_lidar()
```

<br><br><br>




## right_front_lidar()

라이다 센서의 오른쪽 앞 영역 값들의 평균 값을 반환합니다.

### 반환 값

| Value Range         | Dimension | Description                      |
|---------------------|-----------|----------------------------------|
| 0 ~ 65534           | mm        | 정상적인 센서 값의 평균           |
| 65535               | -         | 센서 값이 유효하지 않음          |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서의 오른쪽 앞 영역 평균 값을 얻습니다.
value = beagle.right_front_lidar()
```

<br><br><br>


## left_rear_lidar()

라이다 센서의 왼쪽 뒤 영역 값들의 평균 값을 반환합니다.

### 반환 값

| Value Range         | Dimension | Description                      |
|---------------------|-----------|----------------------------------|
| 0 ~ 65534           | mm        | 정상적인 센서 값의 평균           |
| 65535               | -         | 센서 값이 유효하지 않음          |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서의 왼쪽 뒤 영역 평균 값을 얻습니다.
value = beagle.left_rear_lidar()
```

<br><br><br>







## right_rear_lidar()

라이다 센서의 오른쪽 뒤 영역 값들의 평균 값을 반환합니다.

### 반환 값

| Value Range         | Dimension | Description                      |
|---------------------|-----------|----------------------------------|
| 0 ~ 65534           | mm        | 정상적인 센서 값의 평균           |
| 65535               | -         | 센서 값이 유효하지 않음          |

### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서의 오른쪽 뒤 영역 평균 값을 얻습니다.
value = beagle.right_rear_lidar()
```

<br><br><br>


## resolution()

라이다 센서의 해상도 값을 반환합니다.

### 반환 값

해상도 값 : 1 도

| Return | Range | Dimension |
| ------ | ----- | --------- |
| 해상도 값 | (정수, 0 ~ 180, 초기 값: 0) | 도 |


### 코드

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서의 해상도 값을 얻습니다.
value = beagle.resolution()
```

<br><br><br>

## lidar_chart()

라이다 센서 값들을 차트로 보여줍니다.

```python
from roboid import *

beagle = Beagle()
beagle.start_lidar()

# 라이다 센서 값들을 차트로 보여줍니다.
value = beagle.lidar_chart()
```















<br><br><br><br><br><br>

