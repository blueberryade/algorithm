import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

def move(board,direction):
    if direction == 0:
        for i in range(n):
            top = n-1
            for j in range(n-2,-1,-1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp*2
                        top-=1
                    else:
                        top-=1
                        board[i][top] = tmp

    elif direction == 1:
        for i in range(n):
            top = 0
            for j in range(1,n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp*2
                        top+=1
                    else:
                        top+=1
                        board[i][top] = tmp   
    elif direction == 2:
        for j in range(n):
            top = n-1
            for i in range(n-2,-1,-1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp*2
                        top-=1
                    else:
                        top-=1
                        board[top][j] = tmp    
    else:
        for j in range(n):
            top = 0
            for i in range(1,n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp*2
                        top+=1
                    else:
                        top+=1
                        board[top][j] = tmp                                                                      
    return board


def dfs(board,depth):
    global result
    if depth == 5:
        for i in range(n):
            for j in range(n):
                result = max(result,board[i][j])
        return
    
    for i in range(4):
        new_board = move(deepcopy(board),i)
        dfs(new_board,depth+1)
        
result = 0
dfs(graph,0)
print(result)

