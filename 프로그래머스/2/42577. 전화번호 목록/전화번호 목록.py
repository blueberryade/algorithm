def solution(phone_book):
    hash_map = {}
    for p in phone_book:
        hash_map[p] = 1
    
    for num in phone_book:
        s = ''
        for n in num:
            s+=n
            if s in hash_map and s != num:
                return False
    return True