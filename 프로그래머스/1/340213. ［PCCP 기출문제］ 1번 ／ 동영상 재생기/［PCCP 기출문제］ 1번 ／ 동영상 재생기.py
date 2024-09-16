def solution(video_len, pos, op_start, op_end, commands):
    def change(time):
        temp = 0
        time = time.split(":")
        temp = int(time[0])*60 + int(time[1])
        
        return temp
    
    now = change(pos)
    end = change(video_len)
    op_start = change(op_start)
    op_end = change(op_end)
    
    for command in commands:
        if op_start <= now <= op_end:
            now = op_end
            
        if command == "prev":
            if now <10:
                now = 0
            else:
                now-=10
        
        if command == "next":
            if end-now <10:
                now = end
            else:
                now+=10
                
        if op_start <= now <= op_end:
            now = op_end

            
    minute = str(now//60)
    second = str(now%60)
    
    
    return minute.zfill(2)+":"+second.zfill(2)