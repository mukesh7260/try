
# find largest number in the list without using bultin method and function 

l = [23,45,64,34,98,76]
lmax = l[3]
for i in range(len(l)):
    if l[i] > lmax:
        lmax = l[i]
print(lmax)