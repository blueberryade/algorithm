import sys
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
command = list(map(int,input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0,0,0,0,0,0]

def turn(dice,direction):
    if direction == 1:
        return [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif direction == 2:
        return [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif direction == 3:
        return [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    elif direction == 4:
        return [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    

for i in command:
    nx = x+dx[i-1]
    ny = y+dy[i-1]
    if not (0<=nx<n and 0<=ny<m):
        continue
    
    dice = turn(dice,i)
    
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[-1]
    else:
        dice[-1] = graph[nx][ny]
        graph[nx][ny] = 0
    
    print(dice[0])
 
    x = nx
    y = ny

