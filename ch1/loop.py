# %%
# while / for
# ++, -- (x)

i = 1
while i < 11:
    print(i)
    i = i + 1
# %%
# 1 ~ 100짝수만 출력
i = 1
while i < 101:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1

# %%
# 1 ~ 100 합계 구한 후 출력
sum1 = 0
i = 1
while i < 101:
    sum1 += i
    i = i + 1
print(f"1 ~100 까지의 합 : {sum1}")
# %%
# 6단 구구단 출력
i = 1
while i < 10:
    print("%d * %d = %2d" % (6, i, (6 * i)))
    i += 1

# %%
# 사용자로부터 입력을 받은 후 화면출력
# q라는 문자 입력시 입력받는것 중단
while True:
    data = input("데이터입력")
    print(data)
    if data == "q":
        break

# %%
# for 변수명 in 범위
range(5)
print(list(range(1, 10)))  # 1~4
print(list(range(1, 11, 2)))  # 1,3,5,7,9
# %%
for i in range(10):
    print(i, end=" ")

# %%
for i in range(1, 11):
    print(i, end=" ")
# %%
for i in range(1, 101, 2):
    print(i, end=" ")
# %%
sum1 = 0
for i in range(1, 101):
    sum1 += i
sum1
# %%
# sum()
sum(range(1, 101))

# %%
range(10, 1)
print(list(range(10, 0, -1)))
# %%
# 사용자로부터 숫자를 입력받은 후 1~ 사용자 입력 숫자까지 합계 구한뒤 출력
num1 = int(input("숫자 입력"))
hap = 0
for i in range(1, num1 + 1):
    hap += i
print("1~{} 숫자 합 = {}".format(num1, hap))
# %%
num1 = int(input("숫자 입력"))
del sum
print("1~{} 숫자 합 = {}".format(num1, sum(range(1, num1 + 1))))

# %%
for s in "dreams":
    print(s, end=" ")
# %%
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()
# %%
# 구구단 2~9단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print("%d x %d = %2d" % (i, j, i * j), end="\t")
    print()

# %%
# 리스트
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    print(num)
# %%
# break
i = 1
while i < 11:
    if i == 5:
        break
    print(i, end=" ")
    i += 1
# %%
i = 1
while i < 11:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")
