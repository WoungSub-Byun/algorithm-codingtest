# 첫번 쨰 풀이 - 정확성: 69.2 효율성: 15.4
def solution(phone_book):
    if len(phone_book) == 1:
        return False
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True

