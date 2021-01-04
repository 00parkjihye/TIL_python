# PEP 8 -- Style Guide for Python Code (스타일 가이드)
# https://www.python.org/dev/peps/pep-0008/#inline-comments


# [기본용어]
# 프로그래밍(Programming): 계산할 수식을 컴퓨터에 알려주는 것.
# 토큰(Token): 공백이나 쉼표, 마침표 등으로 분리할 수 없는 가장 작은 단위.
# 토큰 > 식별자(Identifier): 함수, 변수 등. ex> my_name 처럼 공백이 아닌 언더스코어(_)로 구분.
# 코멘트(Comment): 복잡한 코드 설명 + 다른 개발자들과 소통
# 할당(지정)연산자(Assignment Operator): = 우측의 값을 좌측(변수)에 할당(지정)함.
# 비교연산자(Comparison Operator): == 값이 동일하다. / != 값이 동일하지 않다.


# [기본개념]
# 자료형(Data Type) > 숫자(Number) > 정수(Integer) '1' + 소수(Floating Point) '1.0'
#                  > 문자열(String) > " ", ' '로 감싸짐.
#                  > 불린(Boolean) > 참(True) / 거짓(False)

# 추상화(Abstraction): 복잡한 내용을 숨기고 주요 기능에만 신경쓰도록 함.
# 추상화 > 변수(Variable) / 함수(Function) / 객체(Object)


# PEP 8 / Style Guide 중요포인트
# 1> 이름: 모든 변수/함수 이름은 '소문자', 여러 단어일경우 '_(언더바)'로 연결.
some_variable_name = 1


def some_function_name():
    print("Hello!")


# 모든 상수 이름은 '대문자'
SOME_CONSTANT_NAME = 3.14

# '의미있는 이름' 사용.
radius = 2
PI = 3.14
print(PI * radius * radius)


def say_hello():
    print("Hello, Harry!")


# White space(화이트 스페이스): 들여쓰기는 무조건 '4스페이스' 사용.


def say_hello():
    print("Hello, Harry!")  # 들여쓰기 4번

# 함수 정의: 함수 정의 '위,아래로 빈 줄이 2개씩.' 파일의 첫 줄이 함수면 괜찮다.


def a():  # 위,아래 빈 줄 2줄씩.
    print('a')


# 괄호 안: 괄호 바로 안은 띄어쓰기 하지 말 것.
# spam( ham[ 1 ], { eggs: 2 } )  # 띄어쓰기의 안좋은 예.


# 함수 괄호: 함수 정의/호출시, 함수 이름과 골호 사이 띄어쓰기 하지 말 것.


# def spam  <함수명 <-> 괄호 사이 띄어쓰기 x> (a):


def spam(a):
    print(x + 2)


# 쉼표: 쉼표 앞은 띄어쓰기 하지 말 것.
print(a, a)  # good     print(a , b) >  # bad

# 지정연산자: 지정연산자 앞뒤로 띄어쓰기를 하나씩.
x = 1  # good

# 연산자: 기본적으로 연산자 앞뒤로 띄어쓰기를 하나씩.
x = x + 1
x += 1

# + 하지만 연산의 '우선순위' 강조를 위해서는 연산자 앞뒤로 띄어쓰기를 붙이는 것을 권장.
x = x*2 - 1
x = x*x + x*x
c = (x+x) * (x-x)

# 코멘트: 일반 코드와 같은 줄에 코멘트를 쓸 경우, 코멘트 앞 띄어쓰기를 최소 두 개.
x = x + 1  # 코멘트


# [핵심개념]
# [자료형(Data Type)]
# 1> 숫자형(정수) 연산
# 덧셈
print(4 + 6)  # 10

# 뺄셈
print(2 - 4)  # -2

# 곱셈
print(4 * 2)  # 8

# 나머지 연산
print(7 % 3)  # 1

# 거듭제곱
print(2 ** 3)  # 8


# 소수형 연산: 어느 하나라도 소수형이면 결과 역시 소수형.
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


# 나눗셈: 언제나 결과는 '소수형' 으로 나옴.
print(7 / 2)  # 3.5
print(6 / 2)  # 3.0
print(7.0 / 2)  # 3.5
print(6.0 / 2.0)  # 3.0

# 복합계산
print(2 + 3 * 2)  # 3 * 2 = 6 + 2 = 8 (일반 사칙연산과 같음)
print(2 * (2 + 3))  # 2 + 3 = 5 * 2 = 10 (괄호 계산)

# floor division(버림 나눗셈): 나누되 정수형으로 값을 변환.
print(7 // 2)  # 7 / 2에서 소숫점을 버리고 '3'만 출력.
print(8 // 3)  # 8 / 3에서 소숫점을 버리고 '2'만 출력.
print(8.0 // 3)  # 2.0 (역시 하나라도 소수면 결과는 소수형)
print(8 // 3.0)  # 2.0
print(8.0 // 3.0)  # 2.0

# round 함수(반올림 함수): 가장 가까운 정수형으로 반올림.
print(round(3.1415926535))  # 3
print(round(3.1415926535, 2))  # 3.14 (숫자, 반올림할 자릿수)
print(round(3.1415926535, 4))  # 3.1416


# 2> 문자열(String): "",'' 따옴표로 감싸줌.
print("해리포터")  # 해리포터
print("론위즐리")  # 론위즐리

# 문장 안 '따옴표'
print("I'm happy!")  # I'm happy!
print('I\'m happy!')  # I'm happy! # 역슬래쉬 '\'를 따옴표 앞에.

# 문자열 연결(String Concatenation): 문자열끼리 연결하는 연산.
print("Hello " + "Harry!")  # Hello Harry!
print("2" + "4")  # 24
print("프레드 " * 2)  # 프레드 프레드 # 옆으로 반복출력
print("헤르미온느\n" * 2)  # 헤르미온느 # 헤르미온느 # 밑으로 반복출력


# 3> 형 변환(Type Conversion/Casting): 값을 한 자료형에서 다른 자료형으로 변경.
print(int(3.8))  # 3 # 소수형 >정수형
print(float(3))  # 3.0 # 정수형 > 소수형
print(int("2") + int("5"))  # 2 + 5 = 7 # 문자열 > 정수형
print(float("1.1") + float("2.5"))  # 1.1 + 2.5 = 3.6 # 문자열 > 소수형
print(str(2) + str(5))  # "2" + "5" = "25" # 정수형 > 문자열

age = 17
print("제 나이는 " + str(age) + "살 입니다.")  # 제 나이는 17살 입니다. # 정수형 > 문자열
# print(int("Hello harry!"))  # 문자열을 정수형으로 형 변환 할 수 없는 경우.


# 4> 문자열 포맷팅(format)방법
year = 2020
month = 12
day = 29
# 기본적인 작성방법 # 오늘은 2020년 12월 29일 입니다.
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 입니다.")
# '.format' 을 이용한 문자열 작성 # 오늘은 2020년 12월 29일 입니다.
print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))
# '변수' 를 이용한 문자열 작성 # 오늘은 2020년 12월 30일 입니다.
date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day + 1))
# 'f-string' 을 이용한 문자열 작성 # 오늘은 2020년 12월 31일 입니다.
print(f"오늘은 {year}년 {month}월 {day + 2}일 입니다.")
# '%'를 이용한 문자열 작성 # 오래된 방법(잘 안씀) # 오늘은 2020년 12월 30일 입니다.
print("오늘은 %s년 %d월 %r일 입니다." % (year, month, day + 1))


# format: 어떤 자료형이든 문자열로 변환. # 난 해리, 론, 조지를(을) 좋아해!
print("난 {}, {}, {}를(을) 좋아해!".format("해리", "론", "조지"))
# 파라미터 순서변경(0,1,2순으로 원하는 순서 지정) # 난 조지, 해리, 론를(을) 좋아해!
print("난 {2}, {0}, {1}를(을) 좋아해!".format("해리", "론", "조지"))

# 1 나누기 3은 0.3333333333333333입니다.
num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1 / num_2))
# 반올림 표시: 원하는 파라미터 뒤에 ':.(n)f'  # 소숫점이하 몇자리 까지 표시 지정 # 1 나누기 3은 0.33입니다.
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))
# 소수형을 정수로 표시 할 때 ':.0f' # 1 나누기 3은 0입니다.
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1 / num_2))
# round 함수를 이용한 반올림 # 1 나누기 3은 0.33입니다.
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, round(num_1 / num_2, 2)))


# 5> 불린(Boolean): 따옴표 없이, 첫자는 대문자!
# 불 대수의 값: 진리값(True, False). 2가지 값만 존재.
# 불 대수의 연산 : AND, OR, NOT 연산.
# 명제 : 참, 거짓이 확실한 문장.

# 1) AND 연산: x와 y가 '모두 참'일 때만 x AND y가 참.
# ex) 대한민국의 수도는 서울이고, 2는 1보다 크다. # True AND True> True
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# 2) OR 연산: x 또는 y중 하나라도 참이면 x OR y는 참.
# ex) 대한민국의 수도는 서울이거나 제주도이다. # True OR False > True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# 3) NOT 연산: NOT x = y. NOT y = x. 반대로 바꿔줌.
# ex) NOT 대한민국의 수도는 서울이다. > 대한민국의 수도는 서울이 아니다. > False
print(not True)  # False
print(not(not True))  # True # (not(False)) > True
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


# 6> type 함수: 자료형을 확인하는 함수.
print(type(3))  # <class 'int'>
print(type(3.0))  # <class 'float'>
print(type("3"))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type("True"))  # <class 'str'>


def hello():
    print("Hello Harry!")


print(type(hello))  # <class 'function'> # 함수
print(type(print))  # <class 'builtin_function_or_method'> # 내장형 함수


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


# 2> 함수(Function): '명령' 을 저장. 내부적으로 복잡한 동작 과정을 몰라도 간편하게 사용가능.
# python 에서는 들여쓰기로 함수의 범위를 나타냄.
# 예시1)
print("Hello Harry!")  # Hello Harry!


# 예시2) 파라미터(Parameter,매개변수): 함수를 정의할때 쓰는 변수.(함수에 넘겨주는 값)
def hello(name):
    print("Hello!")
    print(name)  # 파라미터
    print("Welcome to Burrow!")


hello("Hermione")  # Hello! Hermione Welcome to Burrow!


# 예시3) 여러개의 파라미터
def print_sum(num1, num2, num3):
    print(num1 + num2 + num3)


print_sum(7, 3, 2)  # 7 + 3 + 2 = 12


# 3> 함수(function)의 실행 순서
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


# 4> 'return 문': 함수에 어떤 정보를 주면 특정 값을 반환.(돌려줌) + 함수를 즉시 종료시킴.
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


# 5> 'return' 과 'print' 의 차이
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


# 6> 옵셔널 파라미터(Optional Parameter): 필수로 값을 넘겨줄 필요가 없는 파라미터.
# 파라미터에는 '기본값(default value)'를 설정할 수 있다. 기본값을 설정하면 호출시 파라미터에 꼭 값을 넘겨줄 필요가 없음.
# 옵셔널 파라미터는 갯수는 상관없으며, 반드시 "마지막에 위치" 해야 함!
def myself(name, age1, nationality="영국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}".format(age1))
    print("국적은 {}".format(nationality))


myself("해리 포터", 17)  # 옵셔널 파라미터 제공하지 않음 # 내 이름은 해리 포터 나이는 17 국적은 영국.
print()
myself("론 위즐리", 18, "미국")  # 옵셔널 파라미터 제공 # 내 이름은 론 위즐리 나이는 18 국적은 미국.


# 7> Syntactic Sugar: 자주 쓰이는 표현을 더 간략하게 쓸 수 있게 해주는 문법.
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


# 8> scope(범위): 변수의 사용 가능한 범위.
# 함수에서 변수를 사용할때, 로컬 변수 > 글로벌 변수 순으로 사용함.
# 예시1) 로컬 변수(local variable): 함수 내에서 정의해, 함수 내에서만 사용.
def my_function():
    f = 3  # 로컬변수(local variable)
    print(f)


my_function()  # 함수호출 > x = 3 > print(x = 3) > '3' 출력
# print(f)  # 함수호출 > x = 3 > print(x = 3) > my_function()줄을 거쳐 print(x) 실행 > 오류발생
# > NameError: name 'f' is not defined('f'가 정의된적 없다) > 'f'는 로컬 변수이므로 유효하지 않은 범위에서 사용.

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


# 9> 상수 (Constant): 변하지 않고 항상 일정한 값을 가지는 수. 변수 이름의 모든 글자를 '대문자'!
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


# 10> 코딩 스타일: 이해하기 쉽고 가독성이 좋은 코드가 좋은 스타일을 가진 좋은 코드.
# 나쁜 스타일 예시> 코드의 목적이 뭔지, 숫자들이 뭘 의미하는지 알 수 없고, 가독성이 떨어짐.
print(6.28*4)  # 200.96
print(3.14*4*4)  # 50.24
print(6.28*8)  # 50.24
print(3.14*8*8)  # 200.96

# 좋은 스타일 예시> 숫자를 변수에 넣어 사용, 적절한 함수 사용 및 코멘트로 설명.
PI = 3.14  # 원주율(파이)


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
    return number % 2 ==  0


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

