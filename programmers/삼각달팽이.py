# 첫번쨰 풀이 - 100 => 진짜 오랜만에 내힘으로 100점받았다!!
from itertools import chain

def solution(n):
    board = [ [0] * i for i in range(1, n+1) ]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    x, y = (0 , 0)
    num = 1
    
    for i in range(n):
        for _ in range(n-i):
            board[x][y] = num
            num += 1
            nx, ny = (x+dx[i%3]), (y+dy[i%3])
            if nx == n or ny == n or board[nx][ny] > 0:
                nx, ny = (x+dx[(i+1)%3]), (y+dy[(i+1)%3])
            x, y = nx, ny
    return list(chain.from_iterable(board))

