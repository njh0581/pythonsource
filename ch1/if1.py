# %%
if True:
    print("True")
# %%
a = 200
# a가 100~200
if a > 100 and a <= 200:
    print("a는 100보다 크고 200보다 작거나 같다")
# %%
if 100 < a <= 200:
    print("a는 100보다 크고 200보다 작거나 같다")

# %%
# 세개의 숫자 중 가장 큰 수 출력
a, b, c = 12, 6, 8
max = a
if max < b:
    max = b
if max < c:
    max = c
print("abc중 가장 큰수는 {}".format(max))
# %%
if True:
    print("True")
else:
    print("False")
# %%
score, grade = 90, "A"
# score가 90이상이고 grade가 A => 합격
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")
# %%
# 숫자 입력받은후 짝/홀 출력
num = int(input("숫자입력 : "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# %%
# 중첩 if
a = 75
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50보다 작다")

# %%
# 다중if
# elif
num = 50
if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("F")

# %%
# age, height 입력받은 후
# age 가 20이상이고 height 170이상 : A 지망 지원 가능 출력
# age 가 20이상이고 height 160이상 : B 지망 지원 가능 출력
# age 가 20이상이고 height 160미만 : 지원불가 출력
# age 가 20미만 : 20세 이상 지원 가능
age = int(input("나이 입력 : "))
height = int(input("키 입력 : "))
if age >= 20 and height >= 170:
    print("A 지망 지원 가능")
elif age >= 20 and height >= 160:
    print("B 지망 지원 가능")
elif age >= 20 and height < 160:
    print("지원 불가")
elif age < 20:
    print("20세 이상 지원 가능")

# %%
# 점수 입력 받은 후
# 81 ~ 100 : A 학점
# 61 ~ 80 : B 학점
# 41 ~ 60 : C 학점
# 21 ~ 40 : D 학점
# 0 ~ 20 : E 학점
score = int(input("점수 입력 : "))
if 81 <= score <= 100:
    print("A 학점")
elif 61 <= score <= 80:
    print("B 학점")
elif 41 <= score <= 60:
    print("C 학점")
elif 21 <= score <= 40:
    print("D 학점")
elif 0 <= score <= 20:
    print("E 학점")

# %%
# 두 개의 숫자 입력받기, 연산자(+*/-,//,**,%)
# 연산 후 결과 출력(출력예시 5 + 3 = 8)
num1 = int(input("숫자입력 : "))
op = input("연산자 입력 : ")
num2 = int(input("숫자입력 : "))
if op == "+":
    print(f"{num1} + {num2} = {num1+num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1-num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1*num2}")
elif op == "/":
    print(f"{num1} / {num2} = {num/num2}")
elif op == "//":
    print(f"{num1} // {num2} = {num1//num2}")
elif op == "**":
    print(f"{num1} ** {num2} = {num1**num2}")
elif op == "%":
    print(f"{num1} % {num2} = {num1%num2}")


# %%
