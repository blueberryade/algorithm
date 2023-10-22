word = input().upper()
lst = list(set(word))
cnt_lst = []
for w in lst:
    cnt = word.count(w)
    cnt_lst.append(cnt)
if cnt_lst.count(max(cnt_lst)) > 1:
    print('?')
else:
    idx = cnt_lst.index(max(cnt_lst))
    print(lst[idx])