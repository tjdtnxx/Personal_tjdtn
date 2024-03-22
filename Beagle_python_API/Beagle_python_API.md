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







<br><br><br><br><br><br>

