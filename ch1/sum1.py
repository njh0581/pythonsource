def sum1(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 없습니다")
        return
    else:
        result = sum1(a, b)

    return result


# 모듈 안의 함수 테스트
if __name__ == "__main__":
    print(sum1(50, 70))
    print(safe_sum(50, "70"))
    print(safe_sum(50, 75))
