# 1차 61.5
def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    for i in range(1, yellow + 1):
        width, height = (yellow // i) + 2, i + 2
        if (width * 2) + 2 * (height - 2) == brown:
            return [width, height]


# 2차 100
def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    for i in range(1, yellow + 1):
        if yellow % i != 0:
            continue
        else:
            width, height = (yellow // i) + 2, i + 2
            if (width * 2) + 2 * (height - 2) == brown:
                return [width, height]


# yellow를 몇 줄로 만들어서 할 것인지가 포인트인데, 이떄 나누는 수는 yellow의 약수여야만 한다.
# 따라서 if yellow % i !=0: 을 넣어 약수가 아니라면 다음으로 넘어가는 기능을 구현하였다.
