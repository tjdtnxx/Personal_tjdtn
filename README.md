# Beagle Python API 메뉴얼



**Beagle**사용자들을 위한 Python API Wiki입니다.<br>
<Br>
이 문서는 로보메이션의 Beagle을 Python으로 프로그래밍하려는 사용자를 위한 라이브러리 API Guide입니다. 

아래 목차에서 **도움말**을 보고싶은 **목차**를 선택하세요.<br>
각 API들을 클릭하면 [예제코드](###-Beagle())가 제공되어 있습니다.
<br><br>
>Service: [로보메이션](www.robomation.net)<br>
API version: 2024-03-01

<br><br><br><br>
목차
[1.개발을 하고 싶어요](#개발을-하고-싶어요)
[2.코딩을 잘하고 싶어요](#coding을-잘하고-싶어요)

## 개발을 하고 싶어요
## Coding을 잘하고 싶어요

<br><br><br><br>
### 이 문서의 내용
- [생성 및 해제](##생성-및-해제) <br>
- [바퀴 움직임](##-바퀴-움직임) <br>
- [소리](##-소리) <br>
- [센서](##-센서) <br>
- [서보 모터](##-서보-모터) <br>
- [LiDar](##-LiDar) <br>
- [전역 함수](##-전역-함수) <br>

<br><br><br><br><br>
# 생성 및 해제
- 생성 <br>
- 해제 <br>
- 초기화 <br>

| Name | Parameter | Return | Description |
| -------- | -------- | -------- | -------- |
| [Beagle()](#beagle()) |  | Beagle 인스턴스의 참조 | Beagle 인스턴스를 생성하고 하드웨어 beagle 로봇과 통신을 연결한다. Beagle(0)을 호출한 것과 같다.
| [Beagle(index)](###-Beagle(index)) |  | Beagle 인스턴스의 참조 | Beagle 인스턴스를 생성하고 하드웨어 비글 로봇과 통신을 연결한다. 몇 번째 비글 로봇인지를 나타내는 인덱스를 index로 설정한다. 인덱스가 같으면 같은 비글 로봇이다.
| [Beagle(port_name)](###-Beagle(port_name)) | port_name: 시리얼 port 이름 (문자열) | Beagle 인스턴스의 참조 | Beagle 인스턴스를 생성하고 port_name의 시리얼 포트를 통해 하드웨어 비글 로봇과 통신을 연결한다. Beagle(0, port_name)을 호출한 것과 같다.
| [Beagle(index, port_name)](###-Beagle(index,port_name)) | index: 몇 번째 비글 로봇인지를 나타내는 인덱스(0이상의 정수), port_name: 시리얼 포트 이름(문자열) | Beagle 인스턴스의 참조 | Beagle 인스턴스를 생성하고 port_name의 시리얼 포트를 통해 하드웨어 비글 로봇과 통신을 연결한다. Beagle(0, port_name)을 호출한 것과 같다.
| [dispose()](###-dispose()) |  |  | Beagle 로봇의 상태를 초기화하고 통신 연결을 끊는다.
| [reset()](###-reset()) |  |  | Beagle 로봇의 상태를 초기화한다.




<br><br><br><br><br>
# 바퀴 움직임
- 전진
- 후진
- 스핀
- Pivot(바퀴축)
- 그 외



































<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### beagle()
```python
from roboid import *
beagle = Beagle()
```
