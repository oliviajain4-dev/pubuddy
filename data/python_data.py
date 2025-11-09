# =========================================================
# 🧠 PyBuddy Knowledge Base — Python 핵심 개념 50개
# =========================================================

python_knowledge = {
    # ------------------- 기본 함수 -------------------
    "print": {
        "type": "기본 함수",
        "importance": 5,
        "desc": "콘솔(터미널)에 데이터를 출력하는 함수입니다. 디버깅 중 변수 값을 확인하거나 결과를 사용자에게 보여줄 때 사용됩니다. 거의 모든 파이썬 프로그램에서 가장 먼저 배우고 가장 자주 쓰입니다.",
        "example": "print('Hello, world!')",
        "usage": "디버깅, 결과 출력, 메시지 표시 등 모든 단계에서 사용됩니다.",
        "related": ["input", "len", "type"],
        "keywords": ["출력", "보여주기", "터미널", "콘솔", "print"]
    },
    "input": {
        "type": "기본 함수",
        "importance": 5,
        "desc": "사용자로부터 데이터를 입력받습니다. 입력된 값은 문자열(str)로 반환되며, 필요에 따라 int()나 float()으로 변환해야 합니다.",
        "example": "name = input('이름을 입력하세요: ')",
        "usage": "사용자의 입력을 받아서 변수에 저장하고 처리할 때 사용됩니다.",
        "related": ["print", "int", "float"],
        "keywords": ["입력", "사용자", "키보드", "받기", "input"]
    },
    "len": {
        "type": "기본 함수",
        "importance": 5,
        "desc": "문자열, 리스트, 튜플 등 시퀀스 자료형의 길이를 반환합니다. 데이터 크기를 빠르게 확인할 수 있습니다.",
        "example": "len([1, 2, 3])  # 3",
        "usage": "반복문에서 개수를 세거나 조건문에 사용됩니다.",
        "related": ["count", "sum"],
        "keywords": ["길이", "요소 수", "크기", "len"]
    },
    "type": {
        "type": "기본 함수",
        "importance": 4,
        "desc": "데이터의 자료형을 확인하는 함수입니다. 디버깅할 때 변수 타입을 확인하는 용도로 많이 사용됩니다.",
        "example": "type(3.14)  # <class 'float'>",
        "usage": "데이터의 형식을 체크하거나 조건 분기 시 타입 비교할 때 사용됩니다.",
        "related": ["isinstance"],
        "keywords": ["자료형", "타입", "형식", "type"]
    },
    "sum": {
        "type": "기본 함수",
        "importance": 4,
        "desc": "리스트나 튜플 등 숫자 요소의 합을 구합니다. 간결하고 빠른 합계 계산용 함수입니다.",
        "example": "sum([1, 2, 3])  # 6",
        "usage": "데이터의 총합이나 누적 합계를 구할 때 사용됩니다.",
        "related": ["max", "min"],
        "keywords": ["합계", "더하기", "총합", "sum"]
    },

    # ------------------- 자료형 -------------------
    "list": {
        "type": "자료형",
        "importance": 5,
        "desc": "여러 값을 순서대로 저장할 수 있는 가변형 데이터 구조입니다. 데이터 추가, 삭제, 변경이 가능합니다.",
        "example": "fruits = ['apple', 'banana', 'cherry']",
        "usage": "여러 데이터를 묶어서 관리할 때 가장 많이 사용되는 자료형입니다.",
        "related": ["tuple", "set", "dict"],
        "keywords": ["리스트", "배열", "모음", "list"]
    },
    "tuple": {
        "type": "자료형",
        "importance": 4,
        "desc": "리스트와 비슷하지만 수정이 불가능한(불변형) 자료형입니다. 데이터의 안정성을 보장합니다.",
        "example": "numbers = (1, 2, 3)",
        "usage": "수정되면 안 되는 데이터를 저장할 때 사용됩니다.",
        "related": ["list", "set"],
        "keywords": ["튜플", "불변", "고정값", "tuple"]
    },
    "set": {
        "type": "자료형",
        "importance": 4,
        "desc": "중복이 허용되지 않는 집합형 데이터입니다. 데이터 중복 제거와 교집합, 합집합 연산에 유용합니다.",
        "example": "s = {1, 2, 3, 3}  # {1, 2, 3}",
        "usage": "중복된 데이터를 자동으로 제거하거나 집합 연산을 수행할 때 사용됩니다.",
        "related": ["list", "dict"],
        "keywords": ["집합", "중복제거", "set"]
    },
    "dict": {
        "type": "자료형",
        "importance": 5,
        "desc": "키(key)-값(value) 쌍으로 이루어진 자료형입니다. 키를 이용해 데이터를 빠르게 찾을 수 있습니다.",
        "example": "person = {'name': 'Nayeon', 'age': 25}",
        "usage": "데이터를 구조적으로 저장하고 빠르게 검색할 때 사용됩니다.",
        "related": ["list", "set"],
        "keywords": ["딕셔너리", "키", "값", "dictionary"]
    },

    # ------------------- 제어문 -------------------
    "if": {
        "type": "제어문",
        "importance": 5,
        "desc": "조건이 참일 경우에만 코드를 실행합니다. 프로그램의 흐름을 제어할 때 핵심적인 문법입니다.",
        "example": "if score >= 60:\n    print('합격')",
        "usage": "조건에 따라 실행할 코드를 다르게 구성할 때 사용됩니다.",
        "related": ["else", "elif"],
        "keywords": ["조건", "판단", "if문"]
    },
    "elif": {
        "type": "제어문",
        "importance": 4,
        "desc": "if 조건이 거짓일 때 새로운 조건을 추가로 검사합니다.",
        "example": "if x > 0:\n    print('양수')\nelif x == 0:\n    print('0')",
        "usage": "조건을 여러 단계로 나눠서 처리할 때 사용됩니다.",
        "related": ["if", "else"],
        "keywords": ["조건 추가", "elif문", "분기"]
    },
    "else": {
        "type": "제어문",
        "importance": 4,
        "desc": "if와 elif 조건이 모두 거짓일 때 실행됩니다.",
        "example": "if x > 0:\n    print('양수')\nelse:\n    print('음수')",
        "usage": "모든 조건이 실패했을 때 실행할 코드를 정의합니다.",
        "related": ["if"],
        "keywords": ["조건", "기타", "else문"]
    },
    "for": {
        "type": "제어문",
        "importance": 5,
        "desc": "시퀀스 데이터(리스트, 문자열 등)를 순서대로 반복합니다. 파이썬의 대표적인 반복문입니다.",
        "example": "for i in range(5): print(i)",
        "usage": "데이터를 반복 처리하거나 누적 연산할 때 사용됩니다.",
        "related": ["while"],
        "keywords": ["반복", "루프", "for문"]
    },
    "while": {
        "type": "제어문",
        "importance": 5,
        "desc": "조건이 참인 동안 코드를 반복 실행합니다. 반복 횟수가 정해지지 않았을 때 유용합니다.",
        "example": "while x < 5:\n    x += 1",
        "usage": "조건이 유지되는 한 반복 실행합니다.",
        "related": ["for"],
        "keywords": ["반복", "조건", "while문"]
    },

    # ------------------- 문자열 메서드 -------------------
    "upper": {
        "type": "문자열 메서드",
        "importance": 4,
        "desc": "문자열의 모든 문자를 대문자로 변환합니다.",
        "example": "'hello'.upper()  # 'HELLO'",
        "usage": "사용자 입력을 표준화하거나 비교 시 대소문자 차이를 없앨 때 사용됩니다.",
        "related": ["lower", "capitalize"],
        "keywords": ["대문자", "문자변환", "upper"]
    },
    "lower": {
        "type": "문자열 메서드",
        "importance": 4,
        "desc": "문자열의 모든 문자를 소문자로 변환합니다.",
        "example": "'Hello'.lower()  # 'hello'",
        "usage": "대소문자 구분 없이 문자열을 비교할 때 사용됩니다.",
        "related": ["upper"],
        "keywords": ["소문자", "lower", "문자변환"]
    },
    "split": {
        "type": "문자열 메서드",
        "importance": 5,
        "desc": "문자열을 특정 구분자를 기준으로 나누어 리스트로 반환합니다.",
        "example": "'a,b,c'.split(',')  # ['a','b','c']",
        "usage": "문자열 데이터를 리스트 형태로 변환할 때 사용됩니다.",
        "related": ["join", "replace"],
        "keywords": ["분리", "나누기", "split"]
    },
    "join": {
        "type": "문자열 메서드",
        "importance": 5,
        "desc": "리스트의 각 요소를 문자열로 결합하여 하나의 문자열을 만듭니다.",
        "example": "','.join(['a', 'b', 'c'])  # 'a,b,c'",
        "usage": "리스트를 문자열로 합칠 때 사용됩니다.",
        "related": ["split"],
        "keywords": ["결합", "join", "문자열 합치기"]
    },
    "replace": {
        "type": "문자열 메서드",
        "importance": 4,
        "desc": "문자열 내 특정 부분을 다른 문자열로 바꿉니다.",
        "example": "'hello'.replace('h','y')  # 'yello'",
        "usage": "텍스트 데이터를 수정하거나 정제할 때 사용됩니다.",
        "related": ["split"],
        "keywords": ["바꾸기", "교체", "replace"]
    },

    # ------------------- 함수/클래스 -------------------
    "def": {
        "type": "함수 정의",
        "importance": 5,
        "desc": "사용자 정의 함수를 선언할 때 사용됩니다. 반복되는 코드를 묶어서 효율적으로 관리할 수 있습니다.",
        "example": "def add(a,b): return a+b",
        "usage": "프로그램을 구조화하고 코드 재사용성을 높이는 데 핵심입니다.",
        "related": ["return", "lambda"],
        "keywords": ["함수", "정의", "def"]
    },
    "return": {
        "type": "함수 제어",
        "importance": 4,
        "desc": "함수에서 실행 결과를 반환합니다. return을 만나면 함수는 즉시 종료됩니다.",
        "example": "return a + b",
        "usage": "함수 결과를 외부로 전달할 때 필수로 사용됩니다.",
        "related": ["def"],
        "keywords": ["반환", "리턴", "결과", "return"]
    },
    "class": {
        "type": "객체지향 문법",
        "importance": 5,
        "desc": "객체를 생성하기 위한 틀(설계도)로, 관련 속성과 동작을 묶습니다.",
        "example": "class Dog:\n    def bark(self):\n        print('멍멍!')",
        "usage": "복잡한 구조를 객체 단위로 관리할 때 사용됩니다.",
        "related": ["object", "__init__"],
        "keywords": ["클래스", "객체", "class"]
    },
    "lambda": {
        "type": "익명 함수",
        "importance": 3,
        "desc": "짧은 일회성 함수를 만들 때 사용됩니다. def와 달리 이름이 없습니다.",
        "example": "square = lambda x: x**2",
        "usage": "간단한 연산이나 매핑에 자주 사용됩니다.",
        "related": ["def"],
        "keywords": ["람다", "간단한 함수", "lambda"]
    },

    # ------------------- 파일 입출력 -------------------
    "open": {
        "type": "파일 입출력",
        "importance": 5,
        "desc": "파일을 열어 읽기 또는 쓰기 작업을 수행할 수 있게 합니다.",
        "example": "f = open('a.txt', 'r')",
        "usage": "파일 입출력의 첫 단계로, 반드시 close()로 닫아야 합니다.",
        "related": ["read", "write"],
        "keywords": ["파일", "열기", "open"]
    },
    "read": {
        "type": "파일 입출력",
        "importance": 4,
        "desc": "파일의 내용을 읽어 문자열로 반환합니다.",
        "example": "data = f.read()",
        "usage": "텍스트 파일을 불러올 때 자주 사용됩니다.",
        "related": ["open", "write"],
        "keywords": ["읽기", "read", "파일"]
    },
    "write": {
        "type": "파일 입출력",
        "importance": 4,
        "desc": "파일에 문자열을 작성(저장)합니다.",
        "example": "f.write('Hello!')",
        "usage": "새로운 텍스트나 데이터를 파일로 저장할 때 사용됩니다.",
        "related": ["open"],
        "keywords": ["쓰기", "저장", "write"]
    },

    # ------------------- 예외 처리 -------------------
    "try": {
        "type": "예외 처리",
        "importance": 4,
        "desc": "코드 실행 중 발생할 수 있는 오류를 처리하기 위한 블록입니다.",
        "example": "try:\n    1/0\nexcept:\n    print('에러 발생!')",
        "usage": "에러로 프로그램이 멈추는 것을 방지합니다.",
        "related": ["except", "finally"],
        "keywords": ["예외", "에러", "try"]
    },
    "except": {
        "type": "예외 처리",
        "importance": 4,
        "desc": "try 블록에서 발생한 오류를 처리합니다.",
        "example": "except ZeroDivisionError:\n    print('0으로 나눌 수 없습니다!')",
        "usage": "특정 오류를 식별하고 대응할 수 있습니다.",
        "related": ["try", "finally"],
        "keywords": ["예외 처리", "except", "에러"]
    },
    "finally": {
        "type": "예외 처리",
        "importance": 3,
        "desc": "try-except 구문에서 오류 발생 여부와 상관없이 항상 실행됩니다.",
        "example": "finally:\n    f.close()",
        "usage": "리소스를 닫거나 종료할 때 사용됩니다.",
        "related": ["try", "except"],
        "keywords": ["마무리", "종료", "finally"]
    },

    # ------------------- 모듈 & 라이브러리 -------------------
    "import": {
        "type": "모듈 관리",
        "importance": 5,
        "desc": "외부 모듈이나 패키지를 불러올 때 사용됩니다. 코드 재사용과 기능 확장을 돕습니다.",
        "example": "import math",
        "usage": "표준 라이브러리나 외부 패키지를 사용할 때 필수입니다.",
        "related": ["from"],
        "keywords": ["불러오기", "모듈", "import"]
    },
    "from": {
        "type": "모듈 관리",
        "importance": 4,
        "desc": "모듈에서 특정 함수나 클래스만 선택적으로 불러옵니다.",
        "example": "from math import sqrt",
        "usage": "필요한 부분만 가져와 네임스페이스 충돌을 방지합니다.",
        "related": ["import"],
        "keywords": ["부분 가져오기", "from", "모듈"]
    },
    "math": {
        "type": "라이브러리",
        "importance": 4,
        "desc": "수학 관련 함수를 제공합니다. 삼각함수, 로그, 제곱근 등을 수행할 수 있습니다.",
        "example": "import math\nmath.sqrt(9)",
        "usage": "수학 연산이 필요한 모든 프로그램에서 사용됩니다.",
        "related": ["import"],
        "keywords": ["수학", "제곱근", "math"]
    },
    "random": {
        "type": "라이브러리",
        "importance": 4,
        "desc": "무작위 숫자, 선택, 섞기 기능을 제공합니다.",
        "example": "import random\nrandom.randint(1,10)",
        "usage": "게임, 시뮬레이션, 데이터 샘플링 등에 활용됩니다.",
        "related": ["import"],
        "keywords": ["랜덤", "무작위", "random"]
    },
    "datetime": {
        "type": "라이브러리",
        "importance": 4,
        "desc": "날짜와 시간을 처리하는 기능을 제공합니다.",
        "example": "from datetime import datetime\nnow = datetime.now()",
        "usage": "시간 기록이나 로그 관리에 사용됩니다.",
        "related":
    "datetime": {
        "type": "라이브러리",
        "importance": 4,
        "desc": "날짜와 시간 관련 작업을 처리하는 표준 라이브러리입니다. 현재 시각, 날짜 계산, 포맷 변경 등이 가능합니다.",
        "example": "from datetime import datetime\nnow = datetime.now()\nprint(now)",
        "usage": "로그 기록, 만료시간 계산, 시간 차이 계산 등에 사용됩니다.",
        "related": ["time"],
        "keywords": ["날짜", "시간", "datetime", "현재시각"]
    },
    "time": {
        "type": "라이브러리",
        "importance": 4,
        "desc": "시간과 관련된 기능을 제공합니다. sleep()으로 대기 시간 설정이 가능하며, 현재 시간도 가져올 수 있습니다.",
        "example": "import time\ntime.sleep(1)  # 1초 대기",
        "usage": "코드 실행 지연, 타이머, 벤치마킹 등에 활용됩니다.",
        "related": ["datetime"],
        "keywords": ["시간", "대기", "sleep", "time"]
    },
    "os": {
        "type": "시스템 라이브러리",
        "importance": 4,
        "desc": "운영체제와 상호작용할 수 있는 기능을 제공합니다. 디렉터리 생성, 삭제, 경로 이동 등을 제어할 수 있습니다.",
        "example": "import os\nos.listdir('.')",
        "usage": "파일 관리나 자동화 스크립트 작성 시 유용합니다.",
        "related": ["pathlib"],
        "keywords": ["파일시스템", "운영체제", "os"]
    },
    "pathlib": {
        "type": "시스템 라이브러리",
        "importance": 3,
        "desc": "파일 경로를 객체 지향적으로 다룰 수 있게 해주는 라이브러리입니다.",
        "example": "from pathlib import Path\np = Path('data.txt')\nprint(p.exists())",
        "usage": "파일 및 폴더의 존재 확인, 경로 결합 등에 사용됩니다.",
        "related": ["os"],
        "keywords": ["경로", "파일", "pathlib"]
    },
    "break": {
        "type": "제어문",
        "importance": 4,
        "desc": "반복문을 즉시 종료하는 명령어입니다. 조건을 만족하면 반복을 멈출 때 사용됩니다.",
        "example": "for i in range(10):\n    if i == 5:\n        break",
        "usage": "특정 조건에서 루프를 중단해야 할 때 사용됩니다.",
        "related": ["continue"],
        "keywords": ["중단", "반복 종료", "break"]
    },
    "continue": {
        "type": "제어문",
        "importance": 4,
        "desc": "현재 반복의 나머지 코드를 건너뛰고 다음 반복으로 넘어갑니다.",
        "example": "for i in range(5):\n    if i == 2:\n        continue\n    print(i)",
        "usage": "특정 조건에서 반복 일부를 건너뛸 때 사용됩니다.",
        "related": ["break"],
        "keywords": ["건너뛰기", "다음반복", "continue"]
    },
    "enumerate": {
        "type": "반복 관련 함수",
        "importance": 4,
        "desc": "반복문에서 인덱스와 값을 동시에 얻을 수 있습니다.",
        "example": "for i, v in enumerate(['a','b']):\n    print(i, v)",
        "usage": "리스트나 튜플을 순회하면서 인덱스도 함께 사용할 때 유용합니다.",
        "related": ["zip"],
        "keywords": ["인덱스", "반복", "enumerate"]
    },
    "zip": {
        "type": "반복 관련 함수",
        "importance": 4,
        "desc": "여러 시퀀스를 병렬로 묶어서 하나의 반복 가능한 객체로 만듭니다.",
        "example": "for x, y in zip([1,2],[3,4]):\n    print(x,y)",
        "usage": "여러 리스트를 동시에 순회할 때 사용됩니다.",
        "related": ["enumerate"],
        "keywords": ["묶기", "zip", "병렬 반복"]
    },
    "format": {
        "type": "문자열 메서드",
        "importance": 4,
        "desc": "문자열 안에 변수를 깔끔하게 삽입할 수 있게 해주는 메서드입니다.",
        "example": "'이름: {}, 나이: {}'.format('나연', 25)",
        "usage": "출력 문자열을 보기 좋게 구성할 때 사용됩니다.",
        "related": ["f-string"],
        "keywords": ["형식", "문자열", "format"]
    },
    "strip": {
        "type": "문자열 메서드",
        "importance": 3,
        "desc": "문자열 앞뒤의 공백이나 특정 문자를 제거합니다.",
        "example": "'  hello  '.strip()  # 'hello'",
        "usage": "텍스트 전처리나 사용자 입력 정제 시 자주 사용됩니다.",
        "related": ["replace"],
        "keywords": ["공백제거", "strip", "문자열"]
    }
}
