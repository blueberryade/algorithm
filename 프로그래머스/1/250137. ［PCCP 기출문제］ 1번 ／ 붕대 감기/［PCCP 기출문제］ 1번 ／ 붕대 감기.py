def solution(bandage, health, attacks):
    answer = health
    t,x,y = bandage
    
    now_time = 0
    attack_idx = 0
    skill_stack = 0
    
    while True:
        now_time += 1
        
        if answer <= 0:
            return -1
        
        if len(attacks) == attack_idx:
            break
        
        a_time, damage = attacks[attack_idx]
        
        if now_time == a_time:
            answer -= damage
            attack_idx+=1
            skill_stack = 0
        else:
            skill_stack +=1
            answer = min(health, answer+x)
            
            if skill_stack == t:
                skill_stack = 0
                answer = min(health,answer+y)
    
    
    return answer
    
    
    
