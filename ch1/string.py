# %%
# 문자처리
# 문자, 문자열 구분 안함 - 쌍따옴표, 홑따옴표 허용, 3개
# "Life is too short, You need Python"
# 'Life is too short, You need Python'
# '''Life is too short, You need Python'''
# """Life is too short, You need Python"""
multiline = """
   Life is too short
   You need Python
"""
multiline
# %%
str1 = "python" + " is fun"
str1

# %%
# * : 문자열 반복
"python" * 2
# %%
print("=" * 50)
print("My Program")
print("=" * 50)
# %%
# 문자열 인덱싱과 슬라이싱
print(str1[3])
print(str1[5])
print(str1[-1])  # 오른쪽에서 인덱싱
# %%
# 슬라이싱 : [시작위치:끝위치] => 끝 위치 포함 안함
str1 = "Life is too short"
print(str1[0:1])
print(str1[0:4])
print(str1[4:])
print(str1[4:8])
print(str1[:17])
print(str1[0:-4])
# %%
# len() : 길이
len(str1)
# %%
str2 = "20240510Sunny"
print(f"년월일 출력 : {str2[0:8]}")
print(f"날씨 출력 : {str2[8:13]}")
# %%
date = str2[0:8]
year = date[:4]
month = date[4:6]
day = date[6:]
print(year, month, day, sep="-")
# %%
jumin = "901205-2234567"
# 주민번호에서 1 or 3 남자, 2 or 4 여자
no = int(jumin[7])
if no == 1 or no == 3:
    print("남자")
else:
    print("여자")
