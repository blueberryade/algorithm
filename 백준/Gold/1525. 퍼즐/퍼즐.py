from collections import deque

puzzle = ""
for i in range(3):
    puzzle+="".join(list(input().split()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs():
    q = deque([puzzle])
    visited = {puzzle:0}

    while q:
        p = q.popleft()
        cnt = visited[p]
        z = p.index("0")

        if p== "123456780":
            return cnt
        
        x = z // 3
        y = z % 3

        cnt+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<=2 and 0<=ny<=2:
                nz = nx*3+ny
                puzzle_list = list(p)
                puzzle_list[z],puzzle_list[nz] = puzzle_list[nz],puzzle_list[z]
                new_puzzle = "".join(puzzle_list)

                if visited.get(new_puzzle,0) == 0:
                    visited[new_puzzle] = cnt
                    q.append(new_puzzle)
    
    return -1

print(bfs())
