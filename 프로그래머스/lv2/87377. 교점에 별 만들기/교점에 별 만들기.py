def solution(line):
    stars = []
    for i in range(len(line)):
        a,b,e = line[i]
        for j in range(i+1,len(line)):
            c,d,f = line[j]
            if a * d == b * c:
                continue
            x = (b * f - e * d)/(a * d - b * c)
            y = (e * c - a * f)/(a * d - b * c)    
            
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                stars.append([x,y])
                
    x_list = [i[0] for i in stars]
    y_list = [i[1] for i in stars]
    x_max,x_min = max(x_list),min(x_list)
    y_max,y_min = max(y_list),min(y_list)
    
    answer = [['.' for _ in range(x_max-x_min+1)] for _ in range(y_max-y_min+1)]
    for x,y in stars:
        answer[y_max-y][x-x_min] = '*'
        
    return [''.join(e) for e in answer]