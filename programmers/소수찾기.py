from itertools import permutations

# 1차 100
def solution(numbers):
    nums_case = []
    for i in range(1, len(numbers) + 1):
        tmp = permutations(numbers, i)
        for n in tmp:
            num_str = "".join(n)
            nums_case.append(int(num_str))
        nums_case = list(set(nums_case))
    return isPrime(nums_case)


def isPrime(nums):
    prime_list = []
    for num in nums:
        cnt = 0
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
                break
        if cnt == 0 and num > 1:
            prime_list.append(num)
    return len(prime_list)


# itertools를 사용하여 모든 조합을 구하였다.
