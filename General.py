# PEP 8 -- Style Guide for Python Code (스타일 가이드): https://www.python.org/dev/peps/pep-0008/#inline-comments
# 내용 중 일부 출처: 점프투파이썬  # https://wikidocs.net/13
# 내용 중 일부 출처: https://www.codingfactory.net/11753


# [기본용어]
# 프로그래밍(Programming): 계산할 수식을 컴퓨터에 알려줌.
# 소스 코드 (source code): 사람들이 쉽게 읽고 이해하도록 프로그래밍 언어로 작성한 코드. 프로그래밍 언어로 소스 코드를 만들고, 이를 컴퓨터가 이해하는 이진코드로 바꾼다.
# 토큰(Token): 공백, 쉼표, 마침표 등으로 분리할 수 없는 가장작은 단위.
# 토큰 > 식별자(Identifier): 함수, 변수 등.  ex> my_name 처럼 공백이 아닌, 언더스코어(_)로 구분.
# 코멘트(Comment): 복잡한 코드설명 + 다른 개발자들과 소통
# 할당(지정)연산자(Assignment Operator): = 우측 값을 좌측(변수)에 할당(지정)함.
# 비교연산자(Comparison Operator): == 값이 동일하다. / != 값이 동일하지 않다.
# 세계 표준시(UTC): 세계표준시(UTC)로 1970년 1월 1일 0시 0분 0초를 기준으로 몇 초가 지났는지를 정수로 나타냄.
# 인터프리터(interpreter): 프로그래밍 소스코드를 실행시켜주는 프로그램. 한 번에 한 줄씩 읽어 실행. 파이썬의 경우 '파이썬 인터프리터'
# 자료형(Data Type): 자료 형태로 사용하는 모든 것을 뜻한다. 프로그램의 기본이자 핵심 단위가 바로 '자료형'
# 추상화(Abstraction): 복잡한 내용을 숨겨, 주요 기능에만 신경쓰도록 함.


# [기본개념]
# 자료형(Data Type) > 숫자(Number) > 정수(Integer) + 소수(Floating Point) > 연산
#                  > 문자열(String) > " ", ' '로 감싸짐 > 포맷팅 > 문자열 함수
#                  > 불린(Boolean) > 불대수[참(True) / 거짓(False)] > 불린 연산
#                  > 리스트(List)
#                  > 튜플(Tuple)
#                  > 딕셔너리(Dictionary)
#                  > 집합(Set)
# 추상화(Abstraction) > 변수(Variable) / 함수(Function) / 객체(Object)


# [PEP 8 : Style Guide 중요포인트]
# 1) 이름: 변수/함수 이름은 '소문자', 여러단어는 '_(언더바)'로 연결.
some_variable_name = 1


def some_function_name():
    print("Hello!")


# 1-2) 상수 이름은 '대문자'
SOME_CONSTANT_NAME = 3.14

# 1-3) '의미있는 이름'
radius = 2
PI = 3.14
print(PI * radius * radius)


def say_hello():
    print("Hello, Harry!")


# 2) White space(화이트 스페이스): 들여쓰기는 무조건 '4 스페이스'
def say_hello():
    print("Hello, Harry!")  # 들여쓰기 4번


# 3) 함수 정의: 함수 정의 '위아래로 빈 줄 2개씩.' 파일의 첫 줄이 함수면 괜찮다.
def a():  # 위,아래 빈 줄 2줄씩.
    print('a')


# 4) 괄호 안: 괄호 바로 안은 띄어쓰기 하지 말 것.
# spam( ham[ 1 ], { eggs: 2 } )  # 띄어쓰기의 안 좋은 예


# 5) 함수 괄호: 함수 정의/호출시, 함수이름과 괄호사이 띄어쓰기 하지 말 것.
# def name  <함수명 <-> 괄호 사이 띄어쓰기 x> (a):
def name(x):  # def name (x) < 이처럼 띄어쓰기 x
    print(x + 2)


# 6) 쉼표: 쉼표 앞은 띄어쓰기 하지 말 것.
print(a, a)  # good   /  print(a , b) >  # bad

# 7) 지정연산자: 지정연산자 앞뒤 띄어쓰기 한 번.
x = 1  # good

# 8) 연산자: 연산자 앞뒤 띄어쓰기 한 번.
x = x + 1
x += 1

# 9) 하지만, 연산의 '우선순위' 강조시 연산자 앞뒤 붙여쓰길 권장.
x = x*2 - 1
x = x*x + x*x
c = (x+x) * (x-x)

# 10) 코멘트: 일반코드와 같은 줄에 코멘트를 쓸 경우, 코멘트 앞 띄어쓰기 두 개.
x = x + 1  # 코멘트

# +) 코딩 스타일: 이해하기 쉽고 가독성이 좋은 코드가 좋은 스타일을 가진 코드.
# 나쁜 코딩스타일> 코드의 목적이 뭔지, 숫자들이 뭘 의미하는지 알 수 없고, 가독성이 떨어짐.
print(6.28*4)  # 200.96
print(3.14*4*4)  # 50.24
print(6.28*8)  # 50.24
print(3.14*8*8)  # 200.96

# 좋은 코딩스타일> 숫자를 변수에 넣어 사용, 적절한 함수사용 및 코멘트로 설명.
PI = 3.14  # 원주율(파이)


# [핵심개념]
# [자료형(Data Type)]
# 1> 숫자형(정수) 연산
# 덧셈(addition)
print(4 + 6)  # 10

# 뺄셈(subtraction)
print(2 - 4)  # -2

# 곱셈(multiplication)
print(4 * 2)  # 8

# 나머지(modulo) 연산
print(7 % 3)  # 1

# 거듭제곱(exponentiation)
print(2 ** 3)  # 8


# 소수형 연산: 어느 하나라도 소수형이면 결과도 소수형.
# 덧셈
print(4.0 + 6.0)  # 10.0

# 뺄셈
print(2.0 - 4.0)  # -2.0

# 곱셈
print(4.0 * 2.0)  # 8.0

# 나머지 연산
print(7.0 % 3.0)  # 1.0

# 거듭제곱
print(2.0 ** 3.0)  # 8.0


# 나눗셈(division): 언제나 결과는 '소수형'으로 나옴. (부동소수 때문)
print(7 / 2)  # 3.5
print(6 / 2)  # 3.0
print(7.0 / 2)  # 3.5
print(6.0 / 2.0)  # 3.0

# 복합계산
print(2 + 3 * 2)  # 3 * 2 = 6 + 2 = 8 (일반 사칙연산과 같음)
print(2 * (2 + 3))  # 2 + 3 = 5 * 2 = 10 (괄호 먼저계산)

# floor division(버림 나눗셈): 나누되 정수형으로 값을 변환.
print(7 // 2)  # 7 / 2에서 소숫점을 버리고 '3'만 출력.
print(8 // 3)  # 8 / 3에서 소숫점을 버리고 '2'만 출력.
print(8.0 // 3)  # 2.0 (하나라도 소수면 결과는 소수형)
print(8 // 3.0)  # 2.0
print(8.0 // 3.0)  # 2.0

# round 함수(반올림 함수): 가장 가까운 정수형으로 반올림.
print(round(3.1415926535))  # 3
print(round(3.1415926535, 2))  # 3.14 (숫자, 반올림할 자릿수)
print(round(3.1415926535, 4))  # 3.1416


# 2> 문자열(String): "",'' 따옴표로 감싸짐.
print("해리포터")  # 해리포터
print("론위즐리")  # 론위즐리

# 문장 안 '따옴표' 표시
print("I'm happy!")  # I'm happy!  # 문장 전체를 감싸준 따옴표말고, 다른 따옴표 사용.
print('I\'m happy!')  # I'm happy!  # 역슬래쉬 '\'를 따옴표 앞에 써줌.

# 문자열 연결(String Concatenation): 문자열끼리 연결하는 연산.
print("Hello " + "Harry!")  # Hello Harry!
print("2" + "4")  # 24
print("프레드 " * 2)  # 프레드 프레드 # 옆으로 반복출력
print("헤르미온느\n" * 2)  # 헤르미온느 # 헤르미온느 # 밑으로 반복출력 ('\n'은 줄바꿈)


# 3> 형 변환(Type Conversion/Casting): 값을 한 자료형에서 다른 자료형으로 변경.
print(int(3.8))  # 3 # 소수형 >정수형
print(float(3))  # 3.0 # 정수형 > 소수형
print(int("2") + int("5"))  # 2 + 5 = 7 # 문자열 > 정수형
print(float("1.1") + float("2.5"))  # 1.1 + 2.5 = 3.6 # 문자열 > 소수형
print(str(2) + str(5))  # "2" + "5" = "25" # 정수형 > 문자열

age = 17
print("제 나이는 " + str(age) + "살 입니다.")  # 제 나이는 17살 입니다. # 정수형 > 문자열
# print(int("Hello harry!"))  # 문자열을 정수형으로 형 변환 할 수 없는 경우.


# 4> 문자열 포맷팅(format)
year = 2020
month = 12
day = 29
# 1) 기본적인 방법  # 오늘은 2020년 12월 29일 입니다.
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 입니다.")
# 2) '.format' 을 이용한 문자열 작성  # 오늘은 2020년 12월 29일 입니다.
print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))
# 3) '변수'를 이용한 문자열 작성  # 오늘은 2020년 12월 30일 입니다.
date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day + 1))
# 4) 'f-string'을 이용한 문자열 작성  # 오늘은 2020년 12월 31일 입니다.
print(f"오늘은 {year}년 {month}월 {day + 2}일 입니다.")
# 5) '%'를 이용한 문자열 작성  # 오래된 방법(잘 안씀)  # 오늘은 2020년 12월 30일 입니다.
print("오늘은 %s년 %d월 %r일 입니다." % (year, month, day + 1))

# 6) format: 어떤 자료형이든 문자열로 변환.  # 난 해리, 론, 조지를(을) 좋아해!
print("난 {}, {}, {}를(을) 좋아해!".format("해리", "론", "조지"))
# 7) 파라미터 순서변경(0,1,2순으로 순서지정)  # 난 조지, 해리, 론를(을) 좋아해!
print("난 {2}, {0}, {1}를(을) 좋아해!".format("해리", "론", "조지"))

# 8) 소수형 반올림 및 자리수 표시 방법
num_1 = 1
num_2 = 3
# 1나누기 3은 0.3333333333333333입니다.
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1 / num_2))
# 반올림 표시: 원하는 파라미터 뒤 ':.(n)f'  # 소숫점 이하 몇자리까지 표시지정  # 1나누기 3은 0.33입니다.
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))
# 소수형을 정수로 표시 할 때 ':.0f'  # 1나누기 3은 0입니다.
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1 / num_2))
# round 함수를 이용한 반올림  # 1나누기 3은 0.33입니다.
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, round(num_1 / num_2, 2)))

# 9) '{' or '}' 표현하기
c = "{{ and }}".format()
print(c)  # { and }
# format 함수로 문자열 포맷팅시 { }와 같은 중괄호를 문자 그대로 쓸 경우, {{ }}처럼 2개를 연속해 사용.


# 5> 문자열 관련 함수들
# 문자열 자료형은 자체적으로 '문자열 내장함수'가 있다.
# 내장함수 사용시 문자열 변수이름 뒤 ‘.’를 붙인뒤 함수이름을 써주면 된다.

# 1) 문자 갯수 세기: '.count(x)' 문자열 중 문자 x의 갯수를 돌려줌.
a = "hobby"
print(a.count('b'))  # 2

# 2) 위치 알려주기: '.find(x)' 문자열 중 문자 x가 '처음으로 나온' 위치 반환. 만약, 찾는 문자나 문자열이 '존재하지 않는다면 -1'을 반환.
a = "Python is the best choice"
print(a.find('b'))  # 14
print(a.find('k'))  # -1  # 찾는 문자나 문자열이 '존재하지 않아 -1 반환'

# 3) 위치 알려주기2: '.index(x)' 문자열 중 문자 x가 처음으로 나온 위치 반환. 찾는 문자나 문자열이 존재하지 않으면 오류 발생.
a = "Life is too short"
print(a.index('t'))  # 8  # 문자열 중 문자 t가 맨 처음으로 나온 위치 반환.
# print(a.index('k'))  # Traceback (most recent call last):  # ValueError: substring not found
# 만약 찾는 문자나 문자열이 존재하지 않는다면 위처럼 오류 발생.
# 'find(x)' 함수와 다른 점: 문자열에 존재하지 않는 문자를 찾으면 '오류 발생'

# 4) 문자열 삽입: ", or /".join()
e = ",".join('abcd')
print(e)  # 'a,b,c,d'
# abcd 문자열 각각의 문자 사이에 ','를 삽입.
# join 함수는 문자열뿐 아니라 리스트나 튜플에도 사용.

# 4-1) join 함수의 입력으로 리스트를 사용시,
g = ",".join(['a', 'b', 'c', 'd'])
print(g)  # 'a,b,c,d'

# 5) 소문자를 대문자로(upper): '.upper()' 소문자를 대문자로 바꿈. 문자열이 이미 대문자면, 아무 변화도 일어나지 않음.
a = "hi"
print(a.upper())  # 'HI'

# 6) 대문자를 소문자(lower): '.lower()' 대문자를 소문자로 바꿈.
a = "HI"
print(a.lower())  # 'hi'

# 7) 왼쪽 공백 지우기(lstrip): '.lstrip()' 문자열 중 가장 왼쪽 공백을 모두 지움. lstrip의 l은 left.
a = " hi "
print(a.lstrip())  # 'hi '

# 8) 오른쪽 공백 지우기(rstrip): '.rstrip()' 문자열 중 가장 오른쪽 공백을 모두 지움. rstrip의 r은 right.
a = " hi "
print(a.rstrip())  # ' hi'

# 9) 양쪽 공백 지우기(strip): '.strip()' 문자열 양쪽 공백을 모두 지움.
a = " hi "
print(a.strip())  # 'hi'

# 10) 문자열 바꾸기: '.replace(바꾸고싶은 문자, 바꿀 문자))' 문자열 안의 특정 값을 다른 값으로 변경.
a = "Life is too short"
print(a.replace("Life", "Your leg"))  # 'Your leg is too short'

# 11) 문자열 나누기(.split()): '.split()'
a = "Life is too short"
print(a.split())  # ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
print(b.split(':'))  # ['a', 'b', 'c', 'd']
# a.split()처럼 괄호 안에 아무값도 넣지 않으면, 공백(스페이스, 탭, 엔터 등) 기준으로 문자열을 나눔.
# 만약 b.split(':')처럼 괄호 안 특정 값이 있을 경우, 괄호 안의 값을 구분자로 문자열을 나눔.
# 위처럼 나눈 값은 리스트에 하나씩 들어감. ['Life', 'is', 'too', 'short']나 ['a', 'b', 'c', 'd']가 리스트.


# 6> 이스케이프 문자(escape character): 원래 가지고 있던 문자열의 출력하는 기능을 벗어나 다른 특정한 기능을 하는 문자.
#                                    \(백슬래시) 기호가 붙은 특수한 문자.
# 1) \n : 다음 줄로 이동(개행)
# 2) \r :해당 줄의 처음으로 이동
# 3) \t : '8칸' 공백
# 4) \' or \" : ' or " 문자
# 5) \ : \문자

# 1)\n
# print("Hello\nWorld")
# 출력결과:
# Hello  # 다음 줄로 개행(줄 바꿈)
# World

# 2) \r
# print("Hello\rHi")
# 출력결과:
# Hillo # Hello 출력 후 '맨 앞으로 이동해 Hi를 덮어씀'
#         한글과 영어를 섞어쓸 땐 결과가 다를 수 있는데, 영어는 글자당 1byte 한글은 2byte 라서임.

# 3) \t
# print("Hello\tWorld")
# 출력결과:
# Hello   World # 문자사이 8칸이아닌 '앞 글자 포함 8칸' 확보.(이경우 'Hello+공백' 합해 8칸)

# 4) \'
# print("\'Hello World\'")
# 출력결과:
# 'Hello World'

# 4-2) \"
# print("\"Hello World\"")
# 출력결과:
# "Hello World"

# 6) \\
# print("C:\\Program Files\\Python35\Scripts\\")
# 출력결과:
# C:\Program Files\Python35\Scripts\  # \ 문자.

# 7) 문자열 곱하기 응용 1
# print("-"*10)  # 출력:---------- 이렇게 문자열을 곱하기면 '문자열이 곱한 수 만큼' 반복됨.
print("\nHello Harry! "*3)
# 출력결과:
# Hello Harry! Hello Harry! Hello Harry!  # 문자열이 3번 나옴.

# 8) 문자열 곱하기 응용 2
# multistring.py
print("=" * 50)
print("My Program")
print("=" * 50)

# 출력결과: 프로그램을 실행시킬때 출력되는 화면 제일 위쪽에 프로그램 제목이 이처럼 표시됨.
# ==================================================
# My Program
# ==================================================


# 7> 여러 줄인 문자열을 변수에 대입시
# 작은따옴표 사용
multiline = '''  
Life is too short
You need python
'''

# 큰따옴표 사용
multiline2 = """  
Life is too short
You need python
"""

# 출력결과:
print(multiline)  # Life is too short (다음줄) You need python 2줄로 표현.
print(multiline2)  # Life is too short (다음줄) You need python 2줄로 표현.


# 8> 문자열 길이 구하기
# len 함수로 구할 수 있다. len 함수는 파이썬의 기본 내장함수.

a = "Life is too short"
len(a)
# 출력결과: 17(공백포함)


# 9> 문자열 인덱싱(indexing): 문자열 가리키기. 'a[번호]'는 문자열 안의 특정한 값을 뽑아내는 역할.(리스트나 튜플에서도 사용)
a = "Life is too short, You need Python"

# 위 소스 코드에서 변수 a에 저장한 문자열의 각 문자마다 번호를 매기면,
# Life is too short, You need Python
# 0         1         2         3
# 0123456789012345678901234567890123
# "Life is too short, You need Python" 문자열에서 L은 첫 번째 자리를 뜻하는 숫자 0, 바로 다음인 i는 1 같이 계속 번호를 붙인 것.
# 중간에 있는 short 의 s는 12가 됨.

# a = "Life is too short, You need Python"
# a[3] == 'e'
# a[3]이 뜻하는 것은 a라는 문자열의 네 번째 문자 e. "파이썬은 0부터 숫자를 센다."

# a[0]:'L', a[1]:'i', a[2]:'f', a[3]:'e', a[4]:' ', ...
# a[번호]는 문자열 안 '특정 값'을 뽑아내는 역할.


# 9-1> 문자열 인덱싱 활용하기
# a = "Life is too short, You need Python"
# a[0] == 'L'
# a[12] == 's'
# a[-1] == 'n'
# a[-0] == 'L' == a[0]
# 마이너스(-) 기호는 문자열을 뒤에서 부터 가리킴. 즉, a[-1]은 뒤에서 첫 번째가 되는 문자.
# 0과 -0은 똑같기 때문에, a[-0]은 a[0]과 똑같은 값.

# a[-2] == 'o'
# a[-5] == 'y'
# a[-2]는 뒤에서 두 번째 문자. a[-5]는 뒤에서 다섯 번째 문자.


# 10> 문자열 슬라이싱(slicing): 문자열에서 특정한 단어를 뽑아내는 방법.(리스트나 튜플에서도 사용)
# 1) 단순 접근:
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)  # 'Life'

# 2) 슬라이싱:
a = "Life is too short, You need Python"
print(a[12:17])  # 'short'
# a[12:17]은 a문자열 "Life is too short, You need Python" 문장에서 자리번호 12부터 17까지 문자를 뽑아냄.
print(a[12:16])  # 'shor'
# 슬라이싱으로 a[시작 번호:끝 번호] 지정시, 끝 번호는 포함하지 않음.
# a[12:16]을 수식으로 나타내면,  # 12 <= a < 16
# 이를 만족하는 것은 a[12], a[13], a[14], a[15]. 따라서 a[12:16]은 'shor', a[12:17]는 'short'.

print(a[0:5])  # 'Life '
# 위 예는 a[0] + a[1] + a[2] + a[3] + a[4]와 동일. a[4]는 공백문자라 'Life' 가 아닌 'Life ' 출력.
# 공백문자 역시 L, i, f, e 같은 문자와 동일하게 취급. 'Life' 와 'Life '는 완전히 다른 문자열.

# 3) 슬라이싱할 떄, 항상 시작번호가 0일 필요는 없다.
print(a[0:2])  # 'Li'
print(a[5:7])  # 'is'
print(a[12:17])  # 'short'

# 4) a[시작 번호:끝 번호], 끝 번호 생략시 시작번호부터 문자열의 끝까지 뽑아낸다.
print(a[19:])  # 'You need Python'

# 5) a[시작 번호:끝 번호]에서 시작번호를 생략하면, 문자열의 처음부터 끝 번호까지 뽑아낸다.
print(a[:17])  # 'Life is too short'

# 6) a[시작 번호:끝 번호]에서 시작번호와 끝 번호를 생략하면, 문자열의 처음부터 끝까지 뽑아낸다.
print(a[:])  # 'Life is too short, You need Python'

# 7) 슬라이싱에서도 인덱싱과 마찬가지로 마이너스(-)(:문자열 뒤에서부터 접근)기호를 사용할 수 있다.
print(a[19:-7])  # 'You need'
# a[19:-7]은, a[19]에서부터 a[-8]까지. 이 역시 a[-7]은 포함하지 않음.

# 8) 슬라이싱으로 문자열 나누기: 문자열을 나누는 방법.
# 위 문자열을 두 부분으로 나누면,
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)  # '20010331'
print(weather)  # 'Rainy'
# 숫자 8기준으로 문자열 a를 양쪽으로 슬라이싱.
# a[:8]은 a[7]까지 잘라내며, a[8:]은 a[8]부터 시작하므로 문자열 a를 '8'을 기준으로 나눔.

# 위 문자열을 세 부분으로 나누면,
a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)  # '2001'
print(day)  # '0331'
print(weather)  # 'Rainy'


# 9) 문자열 수정
# Pithon 문자열을 Python 으로 바꾸려면?
# a = 'Pithon'  >  # a[1] = 'y' >  # i가 a[1]이므로, a[1] = 'y'로 글자를 바꿈.
# 하지만, 위 방법은 오류가 발생. '문자열'의 요솟값은 바꿀 수 있는 값이 아니기 때문.(그래서 immutable 한 자료형이라고도 함.)

# 슬라이싱을 이용해 변경시,
a = "Pithon"
print(a[:1] + 'y' + a[2:])  # 'Python'
# 슬라이싱으로 'P'와 'thon' 사이에 'y' 문자를 추가해, 'Python' 이라는 새로운 문자열 생성.


# 11> 불린(Boolean): 따옴표 없이, 첫자는 대문자!(True, False)
# 불 대수의 값: 진리값(True, False). 2가지 값만 존재.
# 불 대수의 연산 : AND, OR, NOT 연산.
# 명제 : 참, 거짓이 확실한 문장.

# 1) AND 연산: x, y가 '모두 참'일 때만, x AND y 참.
# ex) 대한민국의 수도는 서울이고, 2는 1보다 크다. # True AND True> True
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# 2) OR 연산: x or y중 하나라도, 참이면 x OR y 참.
# ex) 대한민국의 수도는 서울이거나 제주도이다. # True OR False > True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# 3) NOT 연산: NOT x = y. NOT y = x. 반대로 바꿔줌.
# ex) NOT 대한민국의 수도는 서울이다. > 대한민국의 수도는 서울이 아니다. > False
print(not True)  # False
print(not(not True))  # True  # (not(False)) > True
print(not not True)  # True

# 예제)
print(2 > 1)  # True
print(2 < 1)  # False
print(3 >= 2)  # True
print(3 <= 3)  # True
print(2 == 2)  # True
print(2 != 2)  # False
print("Hello" == "Hello")  # True
print("Hello" != "Hello")  # False
print("Hello" == "hello")  # False
print(2 > 1 and "Hello" == "Hello")  # True
print(7 == 7 or (4 < 3 and 12 > 10))  # True
s = 3
print(s > 4 or not (s < 2 or s == 3))  # False

# 4) 자료형의 참과 거짓: 문자열, 리스트, 튜플, 딕셔너리의 값이 비어 있거나 None, 숫자 값이 0일때 거짓(" ", [ ], ( ), { }). 그외는 참.


# 12> type 함수: 자료형을 확인하는 함수.
print(type(3))  # <class 'int'>
print(type(3.0))  # <class 'float'>
print(type("3"))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type("True"))  # <class 'str'>


def hello():
    print("Hello Harry!")


print(type(hello))  # <class 'function'>  # 함수
print(type(print))  # <class 'builtin_function_or_method'>  # 내장형 함수


# 13> 리스트(List): 리스트는 자료들을 목록화시킨 데이터의 묶음. 여러변수를 한번에 묶어 하나의 변수로 사용할 수 있다.
# 리스트는 대괄호([ ])로 감싸고, 각 요솟값은 쉼표(,)로 구분.

# 리스트명 = [요소1, 요소2, 요소3, ...]
a = []
a = list()
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트는 a처럼 비어있는 리스트([ ]), b처럼 숫자, c처럼 문자열, d처럼 숫자+문자열, e처럼 리스트 자체를 요소값으로 가질 수 있다.
# 즉, 리스트는 어떤 자료형도 포함시킬 수 있다.
# ※ 비어 있는 리스트는 a = list()로 생성할 수도 있다.


# 1) 리스트의 인덱싱
# 리스트도 문자열처럼 인덱싱을 적용할 수 있다. 먼저 a 변수에 [1, 2, 3] 값 설정.
a = [1, 2, 3]
print(a)  # [1, 2, 3]

# 'a[0]'은 리스트의 첫 번째 요솟값.
print(a[0])  # 1

# 리스트의 첫 번째 요소인 a[0]와 세 번째 요소인 a[2]의 값을 더함. ('a[자릿수]+a[자릿수]')
print(a[0] + a[2])  # 1 + 3 = '4'

# 'a[-1]'은 문자열에서와 마찬가지로 리스트 a의 마지막 요솟값.
print(a[-1])  # 3

# 리스트 중첩: [x, x1, x2, [x3, x4, x5]] : 이때 a[-1], a[3]은 동일하게 [x3, x4, x5]임.
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])  # 1
print(a[-1])  # ['a', 'b', 'c']
print(a[3])  # ['a', 'b', 'c']
# a[-1]은 마지막 요솟값 ['a', 'b', 'c']임. a[3]은 리스트 a의 네 번째 요소를 나타내서, 마지막 요소를 나타내는 a[-1]과 동일한 결괏값.

# 리스트 a에서 'a' 값을 인덱싱으로 끄집어내기: 'a[중첩 리스트 자릿수][해당 리스트에서 0부터 자릿수]' (a[-1][0])
print(a[-1][0])  # 'a'
# 위와 같이 하면 'a'를 끄집어낼 수 있다. a[-1]이 ['a', 'b', 'c'] 리스트. 바로 이 리스트에서 첫 번째 요소를 불러오기 위해 [0]을 붙여줌.
print(a[-1][1])  # 'b'
print(a[-1][2])  # 'c'


# [삼중 리스트의 인덱싱]
a = [1, 2, ['a', 'b', ['Life', 'is']]]
# 리스트 안에 ['a', 'b', ['Life', 'is']] 리스트가 포함, 그 리스트 안에 다시 ['Life', 'is'] 리스트가 포함된 삼중 구조의 리스트.

# 이떄 'Life' 문자열만 끄집어내려면,
print(a[2][2][0])  # 'Life'
# 리스트 a의 세 번째 요소 리스트 ['a', 'b', ['Life', 'is']]에서 세 번째 요소인 리스트 ['Life', 'is']의 첫 번째 요소.
# 리스트를 삼중으로 중첩하면, 혼란스러워 자주 사용하지 않는다.


# 2) 리스트의 슬라이싱
# 문자열과 마찬가지로 리스트에서도 슬라이싱 기법을 적용할 수 있다. 슬라이싱은 ‘나눈다’는 뜻으로, 문자열에서 했던것과 동일.

a = [1, 2, 3, 4, 5]
print(a[0:2])  # [1, 2]

# 위를 문자열에서 슬라이싱했던 것과 비교시:  # 2가지가 완전히 동일하게 사용.
a = "12345"
print(a[0:2])  # '12'

# 예시)
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)  # [1, 2]  # a[2] 값인 3은 포함되지 않음.
print(c)  # [3, 4, 5]  # 리스트 a의 세 번째 요소부터 끝까지 나타냄.


# [중첩된 리스트의 슬라이싱]
# 리스트가 포함된 중첩리스트 역시 슬라이싱 방법은 같다.
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])  # [3, ['a', 'b', 'c'], 4]
print(a[3][:2])  # ['a', 'b']
# a[3]은 ['a', 'b', 'c']를 나타냄. 따라서 a[3][:2]는 ['a', 'b', 'c']의 첫 번째 요소부터 세 번째 요소 직전까지의 값.


# 3) 리스트 연산
# 리스트 역시 '+' 기호로 더할 수도, '*' 기호로 반복할 수도 있다.

# 3-1) 리스트 더하기(+): 리스트를 합치는 기능. 문자열에서 "abc" + "def" = "abcdef"가 되는 것과 같다.
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # [1, 2, 3, 4, 5, 6]

# 3-2) 리스트 반복(*): 리스트를 반복. 문자열에서 "abc" * 3 = "abcabcabc" 가 되는 것과 같다.
a = [1, 2, 3]
print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# [1, 2, 3] 리스트가 세 번 반복돼, 새로운 리스트를 만들어냄.


# 4) 리스트 길이구하기: 'len(a)' # len 함수(len 함수는 문자열, 리스트, 튜플과 딕셔너리에도 사용.)
a = [1, 2, 3]
print(len(a))  # 3


# 5) 리스트의 수정, 삭제: 리스트는 값을 수정하거나 삭제할 수 있다.
# 5-1) 리스트 값 수정: 'a[변경할 자릿수] = 바꿔줄 값'
a = [1, 2, 3]
a[2] = 4
print(a)  # [1, 2, 4]  # a[2]의 요솟값 3이 4로 바뀜.

# 5-2) 리스트 요소 삭제: 'del a[자릿수]' (del 함수). 'del a[x]'는 x번째 요솟값을 삭제. del 함수는 파이썬이 자체적으로 가지고 있는 함수.
a = [1, 2, 3]
del a[1]
print(a)  # [1, 3]

# 5-3) 여러개 삭제: 'del a[자릿수] or [자릿수:]' (슬라이싱으로 특정 자릿수부터 특정자릿수까지 삭제 등등..활용)
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)  # [1, 2]  # a[2:]에 해당하는 리스트의 요소들 삭제.


# 13-1> 리스트 관련 함수들
# 리스트 변수 이름 뒤 '.'을 붙여 리스트함수 사용.(문자열과 동일)

# 1) 리스트 요소 추가(append): '.append(x)' 리스트의 '맨 마지막에' x를 추가.  # append: 덧붙이다, 첨부하다.
a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]  # 리스트에는 어떤 자료형도 추가가능.

# 리스트에 '리스트 추가'
a.append([5, 6])
print(a)  # [1, 2, 3, 4, [5, 6]]


# 2) 리스트 정렬(sort): '.sort()' 리스트의 요소를 순서대로 정렬.
a = [1, 4, 3, 2]
a.sort()
print(a)  # [1, 2, 3, 4]

# 문자도 순서대로 정렬.
a = ['a', 'c', 'b']
a.sort()
print(a)  # ['a', 'b', 'c']


# 3) 리스트 뒤집기(reverse): '.reverse()' 리스트를 역순으로 뒤집음. 현재 리스트를 그대로 거꾸로 뒤집는다.(리스트를 순서대로 정렬하고 역순으로 정렬x)
a = ['a', 'c', 'b']
a.reverse()
print(a)  # ['b', 'c', 'a']


# 4) 위치반환(index): '.index(x)' 리스트에 x값이 있으면, x의 '위치 값 반환.'
a = [1, 2, 3]
print(a.index(3))  # 2
print(a.index(1))  # 0
# 만약 리스트에 없는 값 호출시, 값 오류(ValueError)발생.


# 5) 리스트 요소삽입(insert): '.insert(자릿값a, 삽입할 값b)' 리스트의 'a번째 위치에 b를 삽입' 하는 함수.
a = [1, 2, 3]
a.insert(0, 4)
print(a)  # [4, 1, 2, 3]

# a = [4, 1, 2, 3] 일때 다시 삽입
a.insert(3, 5)
print(a)  # [4, 1, 2, 5, 3]


# 6)리스트 요소제거(remove): '.remove(삭제할 값x)' 리스트에서 첫 번째로 나오는 x를 삭제.
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)  # [1, 2, 1, 2, 3]  # 삭제할 값이 2개 이상이면, 첫 번째 값만 제거.
a.remove(3)
print(a)  # [1, 2, 1, 2]


# 7) 리스트 요소 끄집어내기(pop): '.pop()' 리스트 맨 마지막 요소를 돌려주면서, 해당요소 삭제.
a = [1, 2, 3]
print(a.pop())  # 3
print(a)  # [1, 2]  # 리스트에서 3을 끄집어내고, [1, 2]만 남음.

# '.pop(삭제할 자릿수a)' 리스트의 a번째 요소를 끄집어내고, 해당요소 삭제.
a = [1, 2, 3]
print(a.pop(1))  # 2
print(a)  # [1, 3]


# 8) 요소 x의 갯수 세기(count): '.count(x)' 리스트 안에 x가 몇 개인지 그 갯수를 돌려주는 함수.
a = [1, 2, 3, 1]
print(a.count(1))  # 2


# 9) 리스트 확장(extend): '.extend(리스트x)' x는 리스트만 가능, 원래의 리스트a에 리스트x를 더함. (중첩리스트가 아닌 하나의 리스트가 됨)
a = [1, 2, 3]
a.extend([4, 5])  # 리스트 자체를 표기
print(a)  # [1, 2, 3, 4, 5]
b = [6, 7]
a.extend(b)  # 리스트를 정의후 리스트명을 표기
print(a)  # [1, 2, 3, 4, 5, 6, 7]


# 13-3> [초보자가 범하기 쉬운 리스트 연산오류]
# 예제) 다음 소스 코드를 입력했을 때 결괏값?
a = [1, 2, 3]
# print(a[2] + "hi")
# a[2]의 값인 3과 문자열 hi가 더해져 3hi가 출력된다고 생각할 수 있다. 하지만, 형 오류(TypeError)가 발생.
# Traceback (most recent call last):  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# a[2]에 저장된 3은 '정수', "hi"는 '문자열' 이라, 정수와 문자열은 더할 수 없기 때문에 형 오류가 발생.

# '3hi' 를 만들려면, '숫자 3'을 '문자 3'으로 바꿔야함.
print(str(a[2]) + "hi")  # 3hi


# 14> 튜플(Tuple): 데이터 변경이 불가능한 자료형. 리스트와 거의 비슷하다.
# 1) 리스트와 튜플: 리스트는 [ ]으로 감싸지만, 튜플은 ( )으로 감싼다.
# 리스트는 그 값의 (생성, 삭제, 수정) 가능하나, 튜플은 그 값을 바꿀 수 없다.

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
# t2 = (1,)처럼 요소가 1개일때는 요소 뒤 콤마(,)를 반드시 붙여야 한다. t4 = 1, 2, 3처럼 괄호( )를 생략해도 된다.

# 튜플과 리스트는 비슷한 역할을 하지만 프로그래밍을 할 때 튜플과 리스트는 구별해서 사용.
# 프로그램 실행동안 그 값이 변하지 않기를 바라면 튜플 사용.
# 실제 프로그램에서는 값이 변경되는 형태의 변수가 많아 리스트를 더 많이 사용.


# 2) 튜플의 요소값을 지우거나 변경시? 튜플의 요솟값은 한 번 정하면 지우거나 변경할 수 없다.
# 2-1. 튜플 요솟값 삭제
t1 = (1, 2, 'a', 'b')
# del t1[0]  # del 함수로 0번쨰 요솟값을 지울시 오류 발생.
# File "<stdin>", line 1, in <module>  # TypeError: 'tuple' object doesn't support item deletion
# 튜플은 요소를 지우는 행위가 지원되지 않는다는 메시지.

# 2-2. 튜플 요솟값 변경
t1 = (1, 2, 'a', 'b')
# >>> t1[0] = 'c'
#   File "<stdin>", line 1, in <module>  # TypeError: 'tuple' object does not support item assignment
# 튜플의 요솟값 변경때도 오류 발생.

# 3) 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])  # 1
print(t1[3])  # 'b'

# 4) 슬라이싱하기
t1 = (1, 2, 'a', 'b')
print(t1[1:])  # (2, 'a', 'b')

# 5) 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 'a', 'b', 3, 4)

# 6) 튜플 곱하기(반복)
t2 = (3, 4)
print(t2 * 3)  # (3, 4, 3, 4, 3, 4)

# 7) 튜플 길이 구하기: 'len()' 함수.
t1 = (1, 2, 'a', 'b')
print(len(t1))  # 4


# 15> 딕셔너리: 사람은 누구든 "이름" = "홍길동", "생일" = "몇 월 며칠" 등으로 구별할 수 있다. 파이썬은 이런 대응관계를 나타낼 수 있는 자료형을 갖고있다.
# 이를,'딕셔너리(Dictionary)'라 하고, 다른 언어에서 연관배열(Associative array) 또는 해시(Hash).
# 즉, "people"에 "사람", "baseball"에 "야구"라는 뜻이 부합되듯 딕셔너리는 'Key와 Value를 한 쌍으로 갖는 자료형'
# 딕셔너리는 리스트, 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고, Key를 통해 Value를 얻으며 이것이 바로 딕셔너리의 가장 큰 특징.
# baseball 단어 뜻을 찾으려 사전 내용을 순차적으로 모두 검색않고, 'baseball이라는 단어가 있는 곳만 펼쳐 보는 것'

# 1) 딕셔너리는 어떻게 만들까?
# 기본 딕셔너리: {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# Key와 Value의 쌍 여러 개가 { }로 감싸짐. 각각 요소는 Key : Value 형태로 이루어져 쉼표(,)로 구분.
# ※ Key에는 변하지 않는 값을 사용, Value에는 변하는 값, 변하지 않는 값 모두 사용가능.

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
# Key는 'name', 'phone', 'birth', Key에 해당하는 Value는 'pey', '0119993323', '1118'
# 딕셔너리 dic의 정보
# [key: value]
# name: pey
# phone: 01199993323
# birth: 1118

# Key로 정수 값 1, Value로 문자열 'hi' 사용한 예.
a = {1: 'hi'}
# 다음 예처럼 Value에 리스트를 넣을 수 있다.
a = {'a': [1, 2, 3]}


# 2) 딕셔너리 쌍 추가: 'a[key] = value'
a = {1: 'a'}
a[2] = 'b'
print(a)  # {1: 'a', 2: 'b'}
# 딕셔너리에 a[2] = 'b'와 같이 입력하면, 딕셔너리 a에 Key와 Value가 2 : 'b'인 딕셔너리 쌍 추가.

a['name'] = 'pey'
print(a)  # {1: 'a', 2: 'b', 'name': 'pey'}
# 딕셔너리 a에 'name': 'pey' 쌍 추가.

a[3] = [1, 2, 3]
print(a)  # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
# Key는 3, Value는 [1, 2, 3] 한 쌍 추가.

# 3) 딕셔너리 요소 삭제: 'del a[]' del 함수 이용.
del a[1]
print(a)  # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}
# del 함수를 사용해 del a[key]입력시 Key에 해당하는 {key : value} 쌍 삭제.

# 4) 딕셔너리 사용방법
# 예를들어 4명의 사람이 있다, 각자 특기를 표현할 수 있는 좋은방법은? 이 경우 리스트, 문자열로는 표현하기 까다롭지만 딕셔너리를 사용하면 표현하기 쉽다.
# {"김연아": "피겨스케이팅", "류현진": "야구", "박지성": "축구", "귀도": "파이썬"}  # 이름과 특기를 한 쌍으로 하는 딕셔너리.

# Key사용해 Value얻기: 딕셔너리 a는 a[Key]로 입력해 Key에 해당하는 Value를 얻는다. 어떤 Key의 Value를 얻기위해 딕셔너리변수이름[Key] 사용.
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])  # 10
print(grade['julliet'])  # 99
# 리스트, 튜플, 문자열은 요솟값을 얻을때 인덱싱, 슬라이싱 사용. 하지만 딕셔너리는 단 한 가지 방법뿐.

a = {1: 'a', 2: 'b'}
print(a[1])  # 'a'
print(a[2])  # 'b'
# a변수에 {1:'a', 2:'b'} 딕셔너리 대입. a[1]은 'a' 값 돌려줌.
# 리스트, 튜플의 a[1]은 두 번째 요소를 뜻하지만(0,1,2,..), 딕셔너리[ ]안 숫자 1은 'Key에 해당하는 1'

a = {'a': 1, 'b': 2}
print(a['a'])  # 1
print(a['b'])  # 2
# 역시 a['a'], a['b']처럼 Key를 사용해 Value를 얻을 수 있다.


# 5) 딕셔너리 주의사항: 딕셔너리에 Key는 고유한 값, 중복되는 Key값을 설정하면 하나를 제외한 나머지 key가 모두 무시된다.
# 동일한 Key가 2개 존재할 경우 나머지 쌍이 무시됨.
a = {1: 'a', 1: 'b'}
print(a)  # {1: 'b'}
# Key가 중복일때, 1개를 제외한 나머지 Key:Value 값이 모두 무시. 동일한 Key 존재시 어떤 Key에 해당하는 Value를 불러야 할지 알 수 없기 때문.

# 또, Key에는 리스트를 쓸 수 없지만 '튜플은 Key로 쓸 수' 있다.
# 딕셔너리의 Key로 쓸 수 있느냐 없느냐는 Key가 변하는 값인지, 변하지 않는 값인지에 달려있다. 리스트는 그 값이 변할 수 있어 Key로 쓸 수 없다.
# 리스트를 Key로 설정시 리스트를 키 값으로 사용할 수 없다는 오류발생.
# a = {[1, 2]: 'hi'}  # File "<stdin>", line 1, in <module>  # TypeError: unhashable type: 'list'
# 따라서 딕셔너리의 Key값으로 리스트를 사용할 수 없음. 단, Value에는 아무 값이나 넣을 수 있다.


# 6) 딕셔너리 관련 함수들
# Key리스트 만들기: '.keys()'  a.keys()는 딕셔너리 a의 Key만 모아 dict_keys 객체를 돌려줌.
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())  # dict_keys(['name', 'phone', 'birth'])

# [파이썬 3.0 이후 버전의 keys 함수, 어떻게 달라졌나?]
# 파이썬 2.7 버전까지는 a.keys() 함수호출시 반환값으로 dict_keys가 아닌 리스트를 돌려줬지만, 메모리 낭비가 발생. 메모리 낭비를 줄이려 dict_keys 객체를 돌려주게 됨.
# 다음에 소개할 dict_values, dict_items 역시 파이썬 3.0 이후 추가된 것들. 만약 반환 값으로 리스트가 필요하면, 'list(a.keys())' 사용.
# dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않아도 기본적인 반복(iterate)구문(for문)을 실행할 수 있다.

# dict_keys 객체는 리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.
for k in a.keys():
    print(k)  # name # phone # birth (아래로 한줄씩 순서대로 나옴)
# print(k) 입력시 들여쓰기 하지 않으면 오류발생.

# dict_keys 객체 리스트 변환: 'list(a.keys())' a딕셔너리의 키를 리스트로 변환.
print(list(a.keys()))  # ['name', 'phone', 'birth']

# Value 리스트 만들기: '.values()' Value만 얻고싶으면 values 함수사용. values 함수호출시 dict_values 객체를 돌려줌.
print(a.values())  # dict_values(['pey', '0119993323', '1118'])

# Key, Value 쌍 얻기: '.items()'  items 함수는 Key와 Value의 쌍을 '튜플로 묶은 값'을 dict_items 객체로 돌려줌.
print(a.items())  # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
# dict_values, dict_items, dict_keys 객체는 리스트 사용과 동일하게 사용할 수 있다.

# Key: Value 쌍 모두 지우기: '.clear()'  clear 함수는 딕셔너리 안 모든 요소삭제. 빈 딕셔너리는 { }로 표현.
a.clear()
print(a)  # {}  # {} = 빈 딕셔너리라는 뜻.

# Key로 Value얻기: '.get(x)'  get(x)함수는 x라는 Key의 Value를 돌려줌. a.get('name')은 a['name']과 동일한 결괏값.
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('name'))  # 'pey'
print(a.get('phone'))  # '0119993323'

# 존재하지 않는 키로 값을 가져올 경우: 1) 'a.get('없는 키')' = None 값 반환. / 2) 'a['없는 키']' = 오류발생.
# a.get('nokey')는 None을 돌려줌. ※ 여기서 None은 "거짓"이라는 뜻.
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('nokey'))  # None
# print(a['nokey'])  # File "<stdin>", line 1, in <module>  # KeyError: 'nokey' > 이경우는 에러발생.

# Key값 부재시 디폴트 값 불러오기: 'get(x, '디폴트 값')' 찾으려는 x값이 없을때, '디폴트 값' 불러옴.
print(a.get('foo', 'bar'))  # 'bar'
# a 딕셔너리에 'foo' 값이 없으므로 디폴트 값인 'bar'를 돌려줌.

# Key가 딕셔너리에 있는지 조사(in): '('찾을값' in a)'  a딕셔너리에 '찾을값'이 있는지 조사해 True, False를 돌려줌.
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print('name' in a)  # True
print('email' in a)  # False
# 'name' 문자열은 a딕셔너리의 Key이므로, 'name' in a를 호출하면 참(True)을 돌려줌.
# 반대로 'email'은 a딕셔너리 안에 존재하지 않는 Key이므로, 거짓(False)을 돌려줌.


# 16> 집합(set): 파이썬 2.3부터 지원한 자료형. 집합 관련된 것을 쉽게 처리하기 위해 만든 자료형.
# 집합 자료형은 다음과 같이 set 키워드 사용
s1 = set([1, 2, 3])
print(s1)  # {1, 2, 3}

# 위같이 set() 괄호에 리스트를 입력하거나 문자열을 입력해 만들 수 있다.
s2 = set("Hello")
print(s2)  # {'H', 'o', 'e', 'l'}

s = set()
print(s)  # set{}
# ※ 비어있는 집합자료형은 s = set()로 만들 수 있다.


# 1) 집합 자료형의 특징
# 그런데 위 set("Hello")의 결과가 이상하다. 분명 "Hello"문자열로 set를 만들어 생성된 자료형에는 l이 하나 빠지고 순서도 엉망이다. 이유는 set에 2가지 큰 특징이 있기 때문.
# 중복을 허용하지 않는다.
# 순서가 없다.(Unordered)
# 리스트, 튜플은 순서가 있기(ordered)때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만, set자료형은 순서가 없기(unordered)때문에 인덱싱으로 값을 얻을 수 없다.
# 딕셔너리는 순서가 없는 자료형으로 인덱싱을 지원않는다.
# 만약 set자료형에 저장된 값을 인덱싱으로 접근하려면 다음처럼 리스트, 튜플로 변환 필요.
# ※ 중복을 허용않는 set의 특징은 자료형의 중복을 제거하기 위한 필터역할로 종종 사용하기도.

s1 = set([1, 2, 3])
l1 = list(s1)  # set 자료형인 s1을 리스트로 형변환 > 이를 l1으로 할당.
print(l1)  # [1, 2, 3]  # 그래서 l1을 프린트시, 리스트 s1이 나옴.
print(l1[0])  # 1  # 리스트로 형변환되어, 인덱싱 사용가능.
t1 = tuple(s1)  # s1을 튜플로 형변환 > 이를 t1으로 할당.
print(t1)  # (1, 2, 3)  # t1을 프린트시, 튜플로 형변환된 s1이 나옴.
print(t1[2])  # 3  # 튜플로 형변환되어, 인덱싱 사용가능.


# 2) 교집합, 합집합, 차집합
# set 자료형을 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때이다.

# 예) s1은 1부터 6까지의 값을 가지고, s2는 4부터 9까지의 값을 가진다.
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 2-1. 교집합
# 1) s1과 s2의 교집합 & : 'print(a1 & a2)' a1과 a2의 교집합 프린트.
print(s1 & s2)  # {4, 5, 6}
# "&" 기호로 교집합을 간단히 구할 수 있다.

# 2) 교집합 intersection 함수: 'print(a1.intersection(a2))' a1과 a2의 교집합 프린트.
print(s1.intersection(s2))  # {4, 5, 6}


# 2-2. 합집합
# 1) "|" 기호 사용: 'print(a1 | a2)' 이때 4, 5, 6처럼 중복포함된 값은 한 개씩만 표현.
print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 2) union 함수: 'print(a1.union(a2))' a1과 a2의 합집합 프린트.
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}


# [추상화(Abstraction)]
# 1> 변수(Variable): '값'을 저장.
# 예시1)
a = 222  # 변수 'a', 'b'
b = 333
print(a + b)  # 555

# 예시2)
extra_points = 50
clean_points = 20
answer_points = 30

print(extra_points)  # 50
print(extra_points * 2)  # 100
print(extra_points + clean_points)  # 70
print(extra_points * 2 + clean_points + answer_points * 3)  # 210

# 예시3)
z = 6
z = z + 1  # 7  # z = 6 + 1  즉, 7 = 6 + 1
# '=' 할당연산자: 우측 값을 좌측(변수)에 할당(지정)함.


# 2> 함수(Function): '명령' 저장. 내부적으로 복잡한 동작과정을 몰라도 간편하게 사용가능.
# python에서는 들여쓰기로 함수의 범위를 나타냄.
# 예시1)
print("Hello Harry!")  # Hello Harry!


# 예시2) 파라미터(Parameter,매개변수): 함수를 정의할때 쓰는 변수(함수에 넘겨주는 값)
def hello(name):
    print("Hello!")
    print(name)  # 파라미터
    print("Welcome to Burrow!")


hello("Hermione")  # Hello! Hermione Welcome to Burrow!


# 예시3) 여러개의 파라미터
def print_sum(num1, num2, num3):
    print(num1 + num2 + num3)


print_sum(7, 3, 2)  # 7 + 3 + 2 = 12


# 2-1> 함수(function)의 실행 순서
# 예시1)
def hello():  # 함수 정의
    print("Hello!")
    print("Welcome to Hogwarts!")


print("함수 호출 전")  # 함수 호출 전
hello()  # Hello! # Welcome to Hogwarts!
print("함수 호출 후")  # 함수 호출 후


# 예시2)
def square(v):
    return v * v


print("함수 호출 전")  # 함수 호출 전
print(square(3) + square(4))  # 25
print("함수 호출 후")  # 함수 호출 후


# 3> 'return 문': 함수에 어떤 정보를 주면 특정 값을 반환(돌려줌) + 함수를 즉시 종료시킴.
# 예시1)
def get_square(c):
    return c * c


print(get_square(3))  # 3 * 3 = 9

y = get_square(2)
print(y)  # 2 * 2 = 4 > y = 4. # print(y) = print(4) > 최종출력 4.


# 예시2)
def get_square(d):
    return d * d


print(get_square(3) + get_square(4))
# 3 * 3 = 9 + 4 * 4 = 16  # 9 + 16 = 25


# 예시3)
def square(n):
    print("함수 시작")
    return n * n
    # print("함수 끝")  # Dead Code(의미없는 코드) - 사용될 일 없는 코드


print(square(3))  # 함수 시작 # 9
print("Hello Harry!")  # Hello Harry!


# 4> 'return'과 'print'의 차이
def print_square(m):  # 파라미터 m의 제곱을 '출력' 해주는 함수.
    print(m * m)


def get_square(m):  # 파라미터 m의 제곱을 '리턴' 해주는 함수.
    return m * m


print_square(2)  # m = 2 / 2 * 2 = 4 > '4' 출력.
get_square(2)  # m = 2 / 2 * 2 = 4 > get_square 가 '4'로 대체됨.
# 하지만 대체되기만 할 뿐, 출력하라는 명령이 없으므로 아무것도 출력되지않고 그대로 함수종료.
print(print_square(3))  # 9 와 None 이 출력.
# m = 3 / 3 * 3 = 9 > print 9 > '9' 출력.
# print_square() 함수에는 return 문이 없음 > return 할 값이 없으므로 'None' 출력.
# 파이썬에선 리턴문이 없으면, 리턴값이 없다는 의미에서 'None' 출력.


# 5> 옵셔널 파라미터(Optional Parameter): 필수로 값을 넘겨줄 필요가 없는 파라미터.
# 파라미터에는 '기본값(default value)'를 설정할 수 있다. 기본값 설정시 호출할때 파라미터에 꼭 값을 넘겨줄 필요가 없음.
# 옵셔널 파라미터는 갯수는 상관없으며, 반드시 "마지막에 위치" 해야 함!
def myself(name, age1, nationality="영국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}".format(age1))
    print("국적은 {}".format(nationality))


myself("해리 포터", 17)  # 옵셔널 파라미터 제공하지 않음 # 내 이름은 해리 포터 나이는 17 국적은 영국.
print()
myself("론 위즐리", 18, "미국")  # 옵셔널 파라미터 제공 # 내 이름은 론 위즐리 나이는 18 국적은 미국.


# 6> Syntactic Sugar: 자주 쓰이는 표현을 더 간략하게 쓸 수 있게 해주는 문법.
x = 1
# 더하기 연산
x = x + 1 == 'x += 1'
# 곱하기 연산
x = x * 2 == 'x *= 2'
# 빼기 연산
x = x - 3 == 'x -= 3'
# 나누기 연산
x = x / 2 == 'x /= 2'
# 나머지 연산
x = x % 7 == 'x %= 7'


# 7> scope(범위): 변수의 사용 가능 범위.
# 함수에서 변수를 사용시, 로컬 변수 > 글로벌 변수 순으로 사용.
# 예시1) 로컬 변수(local variable): 함수 내에서 정의해, 함수 내에서만 사용.
def my_function():
    f = 3  # 로컬변수(local variable)
    print(f)


my_function()  # 함수호출 > x = 3 > print(x = 3) > '3' 출력
# print(f)  # 함수호출 > x = 3 > print(x = 3) > my_function()줄을 거쳐 print(x) 실행 > 오류발생
# > NameError: name 'f' is not defined('f'가 정의된적 없다) > 'f'는 로컬 변수이므로 유효하지 않은 범위에서 사용

# 예시2) 전역 변수(global variable): 함수 밖에서 정의해, 모든 곳에서 사용. 단, 함수 내에서 수정 할 수 없음.
x = 2


def my_function():
    print(x)


my_function()  # x = 2 > 함수 > my_function 함수호출 > print(x = 2) > '2' 출력.
print(x)  # x = 2 > '2' 출력.


# 예시3)
x = 2  # 전역(글로벌) 변수


def my_function():
    x = 3  # 로컬 변수
    print(x)  # 함수내에서 동작시 로컬 변수 > 글로벌 변수 순으로 사용.


my_function()  # my_function 함수호출 > x = 3 > print(x = 3) > '3' 출력.
print(x)  # x = 2 > '2' 출력. # 글로벌 변수 사용.


# 파라미터도 로컬 변수!
def square(x):  # 파라미터 'x' = square 함수 내에서만 쓸 수 있는 로컬 변수!
    return x * x


print(square(3))  # x = 3 > 3 * 3 = '9' 출력.


# 예제1)
x = 10


def my_function():
    y = 5
    print(x + y)


my_function()  # x + y = 10 + 5 = '15' 출력.
print(x)  # x = '10' 출력.


# 8> 상수 (Constant): 변하지 않고 항상 일정한 값을 가지는 수. 변수 이름의 모든 글자를 '대문자'!
# 리터럴(literal): 소스코드 내에서 직접 입력된 값.(=자료(data)라고도 함.) 상수와 같은 의미지만,
# 프로그램에서는 상수는 저장한 값을 변경할 수 없다고 정의하기 때문에, 이와 구분을 위해 '리터럴' 이라는 용어를 사용한다.

# 예제1)
PI = 3.14  # 원주율 '파이' = 상수

# 반지름을 받아서 원의 넓이 계산


def calculate_area(r):  # r = 원의 반지름
    return PI * r * r


radius = 4  # 반지름
print(f"반지름이 {radius}이면, 넓이는 {calculate_area(radius)}")
# 반지름이 4이면, 넓이는 50.24

radius = 6
print(f"반지름이 {radius}이면, 넓이는 {calculate_area(radius)}")
# 반지름이 6이면, 넓이는 113.03999999999999

radius = 7
print(f"반지름이 {radius}이면, 넓이는 {calculate_area(radius)}")
# 반지름이 7이면, 넓이는 153.86


# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r


# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r


radius = 4  # 반지름
print(2 * PI * radius)
print(PI * radius * radius)

radius = 8  # 반지름
print(2 * PI * radius)
print(PI * radius * radius)


# 예제1)
# 어떤 수가 짝수인지 홀수인지 판단해 주는 함수 is_evenly_divisible 를 쓰세요.
# is_evenly_divisible 는 number 를 파라미터로 받습니다.
# 짝수인 경우, 즉 number 가 2로 나누어 떨어질 경우에는 True 를 리턴해 줍니다.
# 홀수인 경우, 즉 number 가 2로 나누어 떨어지지 않을 경우에는 False 를 리턴해 줍니다.
# 함수 안에는 print 문이 아닌, return 문을 사용해야 합니다. 불린 개념을 잘 사용하면, 함수 한 줄로 작성할 수 있습니다.


def is_evenly_divisible(number):
    # 코드를 작성하세요.
    return number % 2 == 0


# 테스트
print(is_evenly_divisible(3))  # False
print(is_evenly_divisible(7))  # False
print(is_evenly_divisible(8))   # True
print(is_evenly_divisible(218))  # True
print(is_evenly_divisible(317))  # False


# 예제2)
# 현명하게 거스름돈을 계산해 주는 프로그램을 만들려고 합니다. 예를 들어 33,000원짜리 물건을 사기 위해 100,000원을 냈다면,
# 50,000원 1장, 10,000원 1장, 5,000원 1장 ,1,000원 2장.
# 이런 식으로 '가장 적은 수'의 지폐를 거슬러 주는 것입니다. 방금 같은 경우에는 총 5장을 거슬러 준 거죠.
# 우리는 calculate_change 라는 함수를 작성하려고 하는데요.
# 이 함수는 지불한 금액을 나타내는 payment 와 물건의 가격을 나타내는 cost 를 파라미터로 받습니다.
# 아래의 코드에 이어서 깔끔하게 프로그램을 작성해 보세요.


def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐
    ten_count = (change % 50000) // 10000  # 10,000원 지폐
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐

    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))


# 다른답안
def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈

    print(f"50000원 지폐: {change // 50000}장")  # 50000원 지폐 : ()장
    print(f"10000원 지폐: {change % 50000 // 10000}장")  # 10000원 지폐 : ()장
    print(f"5000원 지폐: {change % 10000 // 5000}장")  # 5000원 지폐 : ()장
    print(f"1000원 지폐: {change % 5000 // 1000}장")  # 1000원 지폐 : ()장


# 간단해설)
# 67,000원을 거슬러 줘야 하면, 50,000원 지폐는 몇 장 주면 될까요?
# 67,000원에 50,000원이 몇 번 들어가는지 확인하면 되죠?
# 파이썬에서는 버림 나눗셈(//)을 사용하면 이를 알 수 있습니다.
# 67,000원에서 50,000원으로 최대한 거슬러 주고 남은 금액은 17,000원입니다.
# 파이썬에서는 나머지 연산(%)을 사용하면 이를 알 수 있습니다.
# 만약 50,000원과 10,000원을 최대한 거슬러 주고 남은 금액은 뭘까요? 단순하게 생각하면 change % 50000 % 10000인데요.
# 조금만 머리를 굴려 보면 이게 change % 10000과 같다는 걸 알 수 있습니다. 50,000은 10,000의 배수이기 때문이죠!
# 그럼 50,000원, 10,000원, 5,000원을 최대한 거슬로 주고 남은 금액은 어떻게 계산할까요?
# 단순하게 생각하면 change % 50000 % 10000 % 5000이지만, 그냥 간단하게 change % 5000만 해도 똑같은 결과가 나옵니다.
# 50,000과 10,000은 둘 다 5,000의 배수이기 때문입니다!

# 테스트
calculate_change(100000, 33000)  # 50000원 지폐: 1장, 10000원 지폐: 1장, 5000원 지폐: 1장, 1000원 지폐: 2장
print()
calculate_change(500000, 378000)  # 50000원 지폐: 2장, 10000원 지폐: 2장, 5000원 지폐: 0장, 1000원 지폐: 2장


# 예제3)
# 어떤 수를 넣었을 때 10보다 크면 True, 작으면 False 를 반환하는 함수를 만들어보자.

def compare_ten(number):
    if number > 10:
        return True
    else:
        return False


# 위의 코드에서 없어도 되는 코드를 지우면,
def compare_ten(number):
    if number > 10:
        return True
    return False


# 가장 심플하게 코드를 작성하면,
def compare_ten(number):
    return number > 10


# [제어문]
# 1> 'while 반복문': 무언가를 반복하기 위해 사용. 조건이 '참'인 동안 실행하는 반복문. 코드에서 루프를 빠져나올때 break 사용.

# while 조건부분:  # 그 명령들을 실행하기 위한 조건. # 불린 값으로 계산되는 식 = 'True' 일 동안 실행.
#    수행부분  # 반복적으로 수행하고 싶은 명령들. # 출력할 수도 있고 변수 등을 수정할 수도 있음.

# while 다운로드 안 받은 이미지가 있다: # = 사이트에 있는 모든 이미지를 다 다운로드 받으면, 이 반복문을 끝내도 좋다!
#    다음 이미지를 보고, 다운로드 받는다
# > 만약 사이트에 이미지를 다 다운로드 받으면, 조건부분을 충족하지 않기 때문에 반복문은 자동으로 종료됨.


# 예시1)
i = 1
while i <= 3:
    i += 1
    print("나는 잘났다!")
# 결과: 나는 잘났다! 나는 잘났다! 나는 잘났다!

# 예시2)
i = 1
while i <= 3:
    print("나는 예쁘다!")
    i += 1
# 결과: 나는 예쁘다! 나는 예쁘다! 나는 예쁘다!
# 'i += 1'을 나중에 해줘서, '1,2,3'의 값으로 3번 출력.
# 'i += 1'의 위치에 따라 미묘한 결과차이가 생김.

# 예시3)
i = 1
while i <= 3:
    i += 1
    if i <= 3:
        print("나는 잘생겼다!")
# 결과: 나는 잘생겼다! 나는 잘생겼다!
# 'i += 1'을 먼저 해줘서, '2,3'의 값으로 2번 출력.


# 예제1)
# while 반복문을 사용해 1 이상 100 이하의 짝수를 모두 출력해 보세요.

# 먼저, while 반복문을 이용해 1부터 10까지 출력하려면 이렇게 하면 됩니다.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# 그러면 1부터 50까지 출력하려면? 이렇게 하면 되겠죠.
# i = 1
# while i <= 50:
#     print(i)
#     i += 1

# 저희는 1부터 100까지의 수 중 짝수(2, 4, 6, 8, ... , 96, 98, 100)만 출력하고 싶은 건데요.
# 생각해 보면 이건 1 * 2, 2 * 2, 3 * 2, 4 * 2, ... , 48 * 2, 49 * 2, 50 * 2와 같습니다.
# 그러면 위 코드에서 출력하는 값을 i * 2로 수정하기만 하면 되는 거죠!

i = 1
while i <= 50:
    print(i * 2)
    i += 1

# 결과: 2, 4, 6, ..., 96, 98, 100

# 다른답안)
# i = 2
# while (i <=100):
#     print(i)
#     i += 2


# 예제2)
# while 문을 사용하여, 100 이상의 자연수 중 가장 작은 23의 배수를 출력해 보세요.
i = 100

while (i % 23) != 0:    # i % 23 == 0이면 조건부분이 충족되지 않음.
    i += 1              # 조건부분이 FALSE, 수행부분이 실행되지 않음.

print(i)                # 따라서 i % 23 != 0가 FALSE, 이 라인에 프린트문이 실행됨.

# 결과: 115


# 2> 'if...else~' 문: if(만약), else(그렇지 않으면). 상황 별 다른 동작을 위해 사용.
# while 문 처럼 반복하지않고, 딱 한번만 조건문을 확인.
# if 조건부분:  # 불린값으로 계산되는 식. # 이조건을 충족하면 명령실행.
#     실행부분  # 조건을 충족했을때, 실행하고 싶은 명령.
# else:       # 만약 위의 조건을 충족하지 않으면 아래 수행부분을 수행.
#     수행부분

# while 다운로드 안 받은 이미지가 있다:
#     다음 이미지를 본다
#    if 이미지가 png 파일이다:
#        이미지를 다운로드 받는다
#    else:   # else 는 필요에따라 선택적으로 사용
#        print("png 파일이 아닙니다!")

# 예시)
temperature = 8
if temperature <= 10:
    print("자켓을 입는다.")
# 결과: 자켓을 입는다.

temperature = 16
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 벗는다.")
# 결과: 자켓을 벗는다.


# 3> 'elif 문': 수행부분이 여러개 있지만, 단 하나의 수행부분만이 실행 될 수 있음.
# else..if..가 반복되는걸 줄여서 'elif' 로 단순하게 표현.
# if..else 문을 사용할때 1)
temperature = 18
if temperature <= 10:
    print("자켓을 입는다.")
else:
    if temperature <= 15:
        print("긴팔을 입는다.")
    else:
        print("반팔을 입는다.")
# 결과: 반팔을 입는다.

# if..else 문을 사용할때 2)
score = 78
if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

# 결과: C

# elif 문을 사용할때)
score = 56
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 결과: F
# 수행부분이 5개나 있지만, 단 하나의 수행부분만이 실행될 수 있음 > elif 문의 핵심.


# 4> 'break 문': 만약 while 문의 조건부분과 상관없이 반복문에서 나오고 싶으면, break 문 사용.

# i = 100

# while True:
#     # i가 23의 배수면 반복문을 끝냄
#     if i % 23 == 0:
#         break
#     i = i + 1

# print(i)
# 결과: 115

# 추가질문) 이 코드에서 while 의 조건 부분에 해당하는 True 는 무엇이 참인 것을 의미하나요?
# 답: 무엇이 참이라기 보다는 그냥 참을 의미하는 'Boolean 값 그 자체' 를 의미합니다.
# 그래서 while 문 다음에 나오는 while 표현식 부분이 True 로 평가되는 것들을 사용하실 수 있어요.
# False, None, 0, '', (), [], {}
# 이런 것들이 False 로 평가되는데, 이 외의 값들, 예를 들어 while 1 과 같은 것들은 '1'이 'True' 로 평가되기 떄문에 같은 의미로 사용할 수 있습니다.


# 5> 'continue 문': 현재 진행되고 있는 수행부분을 중단하고, 바로 조건부분을 확인하고 싶으면 continue 문을 사용.

# i = 0

# while i < 15:
#     i = i + 1

#     if i % 2 == 1:  # i가 홀수면 print(i) 안 하고, 바로 조건 부분으로 돌아감.
#         continue
#     print(i)

# 결과: 2, 4, 6, 8, 10, 12, 14


# 예제1)
# 학생들에게 최종성적을 알려 주는 '학점 계산기' 를 만들려고 합니다.
# 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있는데요. 두 시험의 점수를 합해서 최종성적을 내는 방식입니다.
# 규칙은 다음과 같습니다.
# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만
# print_grade 함수는 파라미터로 중간고사 점수 midterm_score 와 기말고사 점수 final_score 를 받고, 최종성적을 출력.

def print_grade(midterm_score, final_score):
    total = midterm_score + final_score

    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

# 결과: B, F, D, A
# 해설: B를 받기 위해서는 총 점수가 '80점 이상이면서 90점 미만' 이어야 하는데요.
# 위에 작성된 조건을 보면 80 <= total < 90이 아니라 그냥 total >= 80입니다. 왜 그런 걸까요?
# elif 문으로 넘어 왔다는 것은 앞선 if 문의 조건 부분을 통과하지 않았다는 뜻입니다.
# 그러니까 점수가 90점 미만일 수밖에 없다는 거죠.


# 예제2)
# while 문과 if 문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.
# 예를 들어서 16은 8의 배수이지만 12의 배수가 아니니까 조건에 부합합니다. 하지만 48은 8의 배수이면서 12의 배수이기도 해서 조건에 부합하지 않습니다.
# 실행하면 콘솔에 아래와 같이 출력되어야 합니다.

# 내 답안:
i = 7
while i < 100:
    i += 1
    if (i % 8) == 0:
        if (i % 12) != 0:
            print(i)


# 모범답안:
i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
    i += 1

# 결과: 8, 16, 32, 40, 56, 64, 80, 88
# 해설: 매번 출력해 주는 것이 아니라 i가 8의 배수이면서 12의 배수가 아닐 때에만 출력하고 싶은 것입니다.
# 8의 배수인지 아닌지, 그리고 12의 배수인지 아닌지는 어떻게 판단할 수 있을까요?
# 8로 나누어 떨어지는지, 그리고 12로 나누어 떨어지는지 확인하면 되겠죠?
# i가 8의 배수라면 i % 8의 결괏값이 0일 것이고, i가 12의 배수라면 i % 12의 결괏값이 0일 것입니다.
# 그러니까 i % 8 == 0 and i % 12 != 0을 만족하는 경우에만 i를 출력하면 됩니다.
# 참고로 i += 1은 if문 밖에 있어야 합니다. 그렇지 않으면 끝이 안 나는 "무한 루프"에 빠지게 됩니다. 주의해 주세요!


# 예제3)
# 10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.
# while 문과 if 문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써 보세요.
i = 1
total = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        total += i
    i += 1

print(total)

# 결과: 333167
# 해설: 먼저 '2 또는 3의 배수' 라는 조건은 무시하고, 그냥 10보다 작은 자연수의 합을 출력하는 프로그램을 작성해 봅시다.
# 10보다 작은 자연수의 합을 출력하는 프로그램을 쓰기 위해서는 누적된 합을 보관하는 변수가 필요한데요. 우리는 그 변수를 total 이라고 하겠습니다.
# 그러면 이렇게 작성할 수 있습니다.

# i = 1
# total = 0
#
# while i < 10:
#     total += i  # total = total + i와 동일
#     i += 1  # i = i + 1과 동일
#
# print(total)  # 결과: 45

# 반복문을 돌면서 매번 total 에 i를 더해 주면 되는 거죠. 그리고 반복문이 끝나면 총 누적된 합인 total 을 출력하면 됩니다.
# 만약 1,000보다 작은 자연수의 합을 출력하려면, 위 코드에서 10을 1000으로 바꿔 주기만 하면 되겠죠?
# 이제 위 코드에서 한 줄만 추가하면 되는데요. total += 1을 매번 하는 게 아니라, i가 '2 또는 3의 배수' 라는 조건을 부합할 때만 부르는 것입니다.
# 2 또는 3의 배수인지 판단하기 위해서는, 2 또는 3으로 나누어 떨어지는지 확인해야 합니다.
# 어떤 수가 2 또는 3으로 나누어 떨어진다는 것은, 2 또는 3으로 나누었을 때 나머지가 0이라는 의미입니다.
# i라는 변수가 2로 나누어 떨어지는지 확인하는 코드는 i % 2 == 0입니다. i라는 변수가 3으로 나누어 떨어지는지 확인하는 코드는 i % 3 == 0입니다.
# 그렇다면 i가 2 또는 3으로 나누어 떨어지는지 확인하는 코드는?
# 그냥 불린 연산 or을 사용해서 i % 2 == 0 'or' i % 3 == 0입니다.
# 참고로 i += 1은 if문 밖에 있어야 합니다. 그렇지 않으면 끝이 안 나는 "무한 루프"에 빠지게 됩니다. 주의해 주세요!


# 예제4)
# 정수 n의 약수는 n을 나누었을 때 나누어 떨어지는 수입니다. 만약 정수 i가 정수 n의 약수라면, n을 i로 나누었을 때 나머지가 0이 나와야 하는 거죠.
# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램을 써 보세요. 아래처럼 콘솔에 출력되어야 합니다.

# 내 답안:
i = 1
while i <= 120:
    if 120 % i == 0:
        print(i)
    i += 1

print("120의 약수는 총 16개입니다.")

# 모범답안:
N = 120
i = 1
count = 0

while i <= N:
    if N % i == 0:
        print(i)
        count += 1
    i += 1

print(f"{N}의 약수는 총 {count}개입니다.")

# 결과: 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120, 120의 약수는 총 16개입니다.
# 해설: 약수를 세는 것은 일단 미루어 두고, 약수를 모두 출력하는 코드부터 작성해 봅시다.
# 120의 약수를 모두 찾아야 하는데요. 그러면 120이 1로 나누어 떨어지는지 확인하고, 2로 나누어 떨어지는지 확인하고, 3으로 나누어 떨어지는지 확인하고...
# 이런 식으로 120까지 나누어 떨어지는지 확인하면 됩니다.
# '나누어 떨어진다' 는 건 코드로 어떻게 나타낼까요? 변수 i가 4로 나누어 떨어진다면, i % 4 == 0은 True 가 나올 것입니다.

# N = 120
# i = 1

# while i <= N:
#     if N % i == 0:
#         print(i)
#     i += 1

# 참고로 i += 1은 if문 밖에 있어야 합니다. 그렇지 않으면 끝이 안 나는 "무한 루프"에 빠지게 됩니다. 주의해 주세요!
# 그런데 이 문제에서는 약수를 모두 출력하는 것뿐만 아니라 약수의 총 개수도 출력해야 합니다. 그러기 위해서는 개수를 세기 위한 변수를 하나 만들어야겠죠?
# 변수 이름은 count 같은 게 좋을 것 같습니다!
# 이 count 변수는 어떻게 활용해야 할까요? 120의 약수를 발견했을 때마다 1씩 늘려 주면 되겠죠?


# 예제5)
# 1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만원을 받았습니다. 하지만 바둑 외에는 아는 게 없으니, 이웃 어른들에게 이 돈으로 무엇을 해야 할지 물어보기로 하였습니다.
# 은행에서 근무하는 동일 아저씨는 은행에 돈을 맡겨서 매년 이자로 12%씩 받는 것을 추천하셨습니다.
# 1년 후인 1989년에는 5,000만원의 12% 이자인 600만원이 더해져 5,600만원이 된다고 하면서요.
# 이 이야기를 들은 미란 아주머니는 고작 12% 때문에 생돈을 은행에 넣느냐며, 얼마 전 지어진 은마아파트를 사라고 추천하셨습니다. 당시 은마아파트의 매매가는 5,000만원이었죠.
# 2016년 기준 은마아파트의 매매가는 11억원인데요. 1988년 은행에 5,000만원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여,
# 동일 아저씨와 미란 아주머니 중 누구의 말을 듣는 것이 좋았을지 판단해 보세요. 2016년 은행에 얼마가 있을지는 꼭 while 문을 사용해서 계산해 주세요!
# 2016년에 은행에 저축해 둔 금액이 더 크면, *원 차이로 동일 아저씨 말씀이 맞습니다.가 출력되도록 하세요. 반대로 은마아파트의 가격이 더 크면,
# *원 차이로 미란 아주머니 말씀이 맞습니다.가 출력되도록 하세요. 여기서는 꼭 if 문을 사용해 주세요!
# while :

# 결과: 94193324원 차이로 동일 아저씨 말씀이 맞습니다.
# 해설:


# 예제6)
# 피보나치 수열(Fibonacci Sequence)라고 들어 보셨나요?
#    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#    1,1,2,3,5,8,13,21,34,55,...
# 우선 피보나치 수열의 1번 항과 2번 항은 각각 1입니다. 3번 항부터는 바로 앞 두 항의 합으로 계산됩니다.
# 예를 들어서 3번 항은 1번 항(1)과 2번 항(1)을 더한 2이며, 4번 항은 2번 항(1)과 3번 항(2)을 더한 3입니다.
# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 프로그램을 작성해 보세요.
i = 1
j = 1
count = 0

print(i)
print(j)

while count <= 23:
    i = i + j
    print(i)
    j = j + i
    print(j)
    count += 1


# 모범답안1:
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous 를 임시 보관소 temp 에 저장
    previous = current
    current = current + temp  # temp 에 기존 previous 값이 저장
    i += 1


# 모범답안2:
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1

# 결과:1, 1, 2, 3, 5, 8, 13, 21, ..., 4807526976, 7778742049, 12586269025
# 해설: 먼저 10개의 항을 출력하는걸 목표로 한다면, 10개의 항을 출력하기 위해서는 반복문을 열 번 돌아야겠죠?
# 열 번 도는 반복문부터 작성해 봅시다.
i = 1

while i <= 10:
    i += 1

# 피보나치 수열의 항은 앞선 두 항의 합으로 계산되는데요. 따라서 피보나치 수열의 항들을 순서대로 출력하기 위해서는 늘 마지막 두 항을 변수에 보관해야 합니다.
# '현재 항'은 변수 current 에, 그리고 '직전 항'은 변수 previous 에 저장. 처음에는 current 를 1로 설정, previous 를 0으로 설정.

previous = 0
current = 1
i = 1

while i <= 10:  # 우리가 반복적으로 무엇을 해야할까요?
    i += 1
# 이제 while 반복문의 수행부분만 채워넣으면 됩니다.
# 수행부분에서 해야 할 일은 크게 두 가지입니다. 'current 출력 + previous, current 적절히 수정'
# 1번은 그냥 print(current)를 하면 되니까 먼저 채워넣겠습니다.

previous = 0
current = 1
i = 1

while i <= 10:
    print(current)  # previous, current 적절히 수정
    i += 1

# 2번이 약간 헷갈리는 부분. 수행부분에서 previous, current 를 어떻게 수정할 수 있을까요? 일단 단순하게 생각하면 이렇습니다.
# previous ← current
# current ← current + previous

# 그리고 위 로직을 코드로 나타내면 아래와 같습니다.
# previous = current
# current = current + previous

# 그런데 사실 위 코드처럼 하면 문제가 생깁니다. previous = current 면, previous, current 가 같은 값을 저장하게 됩니다.
# 그리고 기존의 previous 값은 잃어버리게 되죠. 예를들어 previous = 2, current = 3일 때.
# previous = current 를 하면? previous = 3으로 바뀌고, current = 3이죠? 기존 previous 에 있던 정수 2는 완전히 잃어버리게 됩니다.
# 이 문제를 해결하기 위해, 임시 보관소 역할을 할 변수를 만들어야 합니다.

temp = previous  # previous 를 임시 보관소 temp 에 저장
previous = current
current = current + temp  # temp 에는 기존 previous 값이 저장
# 그러면 문제없이 previous 와 current 를 수정할 수 있습니다. 여기까지 완성된 코드를 봅시다.

previous = 0
current = 1
i = 1

while i <= 10:
    print(current)
    temp = previous  # previous 를 임시 보관소 temp 에 저장
    previous = current
    current = current + temp  # temp 에 기존 previous 값이 저장
    i += 1
# 결과: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# 피보나치 수열의 10개 항이 잘 나오는 것 같죠? 이제 'while i <= 10:'을 'while i <= 50:'으로 수정하기만 하면 됩니다!


# 예제7)
# while 문을 사용해서 구구단 프로그램을 만들어 봅시다. 실행하면 아래와 같은 결과물이 출력되어야 합니다.

# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# .
# .
# .
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81

# 참고로 이 문제는 '중첩 while 문' 이라는 개념을 사용해야 하는데요. 중첩 while 문은 while 문의 수행부분 안에 또 다른 while 문을 넣는 것.
# 설명드리지 않은 개념이지만, 고민하다 보면 직접 알아내실 수도 있습니다.
i = 0
while i < 9:
    i = i + 1
    j = 1
    while j < 10:
        print(i, 'X', j, '=', i*j)  # = print(f"{i} * {j} = {i*j}")
        j = j + 1


# 해설: i가 10보다 작으면 i을 출력합니다. 작업할 때마다 i는 1씩 커지고, i가 10이 되면 while 문을 빠져나옵니다.


# 예제8)
# 'break' 를 넣으면, while 문을 빠져나옵니다. 다음은 input()으로 입력받은 수까지만 구구단을 출력하는 예제.

# x = int(input('Number : '))
# i = 1
# while i < 10:
#     i += 1
#     j = 1
#     while j < 10:
#         print(i, 'X', j, '=', i*j)  # print(f"{i} * {j} = {i*j})
#         j += 1
#     if i == x:
#         break

# 결과: Number : 4
# 2 X 1 = 2, 2 X 2 = 4, 2 X 3 = 6, 2 X 4 = 8, 2 X 5 = 10, 2 X 6 = 12, 2 X 7 = 14, 2 X 8 = 16, 2 X 9 = 18
# 3 X 1 = 3, 3 X 2 = 6, 3 X 3 = 9, 3 X 4 = 12, 3 X 5 = 15, 3 X 6 = 18, 3 X 7 = 21, 3 X 8 = 24, 3 X 9 = 27
# 4 X 1 = 4, 4 X 2 = 8, 4 X 3 = 12, 4 X 4 = 16, 4 X 5 = 20, 4 X 6 = 24, 4 X 7 = 28, 4 X 8 = 32, 4 X 9 = 36

# 해설: continue 를 만나면, 그 이후 구문은 실행하지 않고, while 문의 처음으로 돌아갑니다.


# 예제9)  # 출처: https://www.codingfactory.net/11753
# 10보다 작은 홀수를 출력하라.
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")

# 결과: 1 3 5 7 9
# 해설: 2로 나눈 나머지가 0이면, 즉 짝수면 print 문을 실행하지 하지않고 i의 값을 1 증가시킵니다.


#

