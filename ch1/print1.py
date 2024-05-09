# 함수: print(출력할 문장)
# 문자: '' or "" 가능
print('Hello python')
print("Hello python")
print(100)
print("100")
print(25.3)
print("25.3")
# type()
print(type("Hello python"))
print(type(100))
print(type(25.3))
print(type(True))

print("T","E","S","T")

# print() 에 사용하는 옵션
# sep: 문자열 출력시 기본 구분은 스페이스바 한번
print("T","E","S","T",sep="")
print("2024","05","09",sep="-")

# end: print() 줄바꿈 기본
print("Welcome to",end=" ")
print("안녕하세요")

# 포메팅 - %d, %s, %f, %c
# 포멧코드 + 숫자 : %5d - 전체자릿수 5(오른쪽 정렬)
print("%d" % 100)
print("%5d" % 100)
print("%05d" % 100)
print()
print("%s" % "hi")
print("%5s" % "hi")
print()
# 전체자릿수 : 8(소수점 자리수 2 포함)
print("%-8.2f" % 123.21) # - : 왼쪽정렬
print("%8.2f" % 123.21)
print("%8.2f" % 123.215678)

# 변수 : 타입없음(값을 담고 난 다음에 결정) / 키워드 없음(let, const X)
number = 4
print("I eat %d apples" % number)

print("%d : %s" % (1, "홍길동"))

# %s : 어떤형태의 값이든 문자열로 변환해 대입
print("I eat %s apples" % number)
print("I eat %s apples" % 3.1415)
print("I eat %s apples" % "three")

print("Error is %d%%" % 98)

print()
# format() : 포멧코드와 유사한 역할
print("I eat {} apples".format(3))
print("{} and {}".format("you","me"))
print("I eat {0} apples".format(3))
print("{0} and {1} and {0}".format("you","me"))

# format() + 인덱스 + 이름
print("{var1} are {var2}".format(var1="You", var2="niceman"))
print("I ate {0} apples, so I was sick for {day} days".format(10,day=3))

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776,6534.123))

# f 문자열 포매팅
name="홍길동"
age = 30
print(f"나의 이름은 {name} 입니다. 나이는 {age} 입니다")

print("\n줄바꿈\n연습")
print("\t탭\t연습")
print('글자가 "강조"되는 효과')
print("글자가 '강조'되는 효과")




