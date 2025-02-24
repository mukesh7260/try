# s = 'rohit shrama'
# d = {}
# for i in s:
#     if i in " ":
#         continue
#     d[i] = d.get(i,0)+1
# for k , v in d.items():
#     print(f'{k} - {v}')


s = 'rohit shrama'
d = {}
for i in s:
    if i in ' ':
        continue 
    elif i in d:
        d[i] = d[i]+1
    else:   
        d[i] = 1
for k , v in d.items():
    print(f'{k} - {v}')