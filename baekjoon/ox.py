n = int(input())
case_arr = [str(input()) for _ in range(n)]
result, add_num = 0, 1
for case in case_arr:
    for answer in case:
        if answer == "X":
            add_num = 1
        elif answer == "O":
            result += add_num
            add_num += 1
    print(result)
    result, add_num = 0, 1
