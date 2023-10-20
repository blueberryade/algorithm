from string import ascii_lowercase
alph_list = list(ascii_lowercase)

s = input()
for i in alph_list:
    print(s.find(i),end=' ')
  
