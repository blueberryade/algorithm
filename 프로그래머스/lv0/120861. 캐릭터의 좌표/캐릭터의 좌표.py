def solution(keyinput, board):
    answer = [0,0]
    a = board[0]//2
    b = board[1]//2
    for i in keyinput:
        if i == 'up' and answer[1]<b:
            answer[1]+=1
        elif i== 'down' and answer[1]>-b:
            answer[1]-=1
        elif i == 'right' and answer[0]<a:
            answer[0]+=1
        elif i == 'left' and answer[0]>-a:
            answer[0]-=1
    
    return answer            
            
            
    
    return answer