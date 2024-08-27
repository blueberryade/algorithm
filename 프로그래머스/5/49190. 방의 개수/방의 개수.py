def solution(arrows):
    answer = 0
    x,y = 0,0
    
    visited = set()
    visited.add((x,y))
    route = set()
    
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    
    for arrow in arrows:
        for _ in range(2):
            nx = x+dx[arrow]
            ny = y+dy[arrow]
            
            if (nx,ny) in visited and (x,y,nx,ny) not in route:
                answer+=1
            
            route.add((x,y,nx,ny))
            route.add((nx,ny,x,y))
            visited.add((nx,ny))
            x,y = nx,ny
    
    return answer