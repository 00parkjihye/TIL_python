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
def myself(name, age, nationality="영국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}".format(age))
    print("국적은 {}".format(nationality))


myself("해리 포터", 17)  # 옵셔널 파라미터 제공하지 않음 # 내 이름은 해리 포터 나이는 17 국적은 영국.
print()
myself("론 위즐리", 18, "미국") # 옵셔널 파라미터 제공 # 내 이름은 론 위즐리 나이는 18 국적은 미국.


# 7> Syntactic Sugar: 자주 쓰이는 표현을 더 간략하게 쓸 수 있게 해주는 문법.
x = 1
# 더하기 연산
x = x + 1  == 'x += 1'
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

