def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0:
                up_left = 0
            else:
                up_left = triangle[i-1][j-1]
            
            if j == i:
                up = 0
            else:
                up = triangle[i-1][j]
            
            triangle[i][j] = triangle[i][j]+max(up_left,up)
            
    return max(triangle[-1])