part_num = int(input())

table = sorted([list(map(int, input().split())) for _ in range(part_num)], key=lambda row: -row[2])

print(str(table[0][0]) + ' ' + str(table[0][1]))
print(str(table[1][0]) + ' ' + str(table[1][1]))
if table[0][0] == table[2][0]:
    print(str(table[3][0]) + ' ' + str(table[3][1]))
else:
    print(str(table[2][0]) + ' ' + str(table[2][1]))
