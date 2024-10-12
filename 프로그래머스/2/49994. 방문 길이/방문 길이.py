def solution(dirs):
    answer = set()
    x,y = 0,0
    direction = {'U':(1,0), 'R':(0,1), 'L': (0,-1),'D':(-1,0)}
    
    
    for d in dirs:
        dx,dy = direction[d]
        nx,ny = x+dx, y+dy

        if -5<=nx <=5 and -5<=ny <=5:
            answer.add((x,y,nx,ny))
            answer.add((nx,ny,x,y))

            x,y = nx,ny
            
            
        
    return len(answer)//2