n, m = map(int, input().split())
result = [i for i in range(1, n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    start, end = start - 1, end - 1
    result[start:end] = list(reversed(result[start:end]))
for i in result:
    print(i, end=" ")
