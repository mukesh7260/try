
# find largest number in the list without using bultin method and function 

# l = [23,45,64,34,98,76]
# lmax = l[3]
# for i in range(len(l)):
#     if l[i] > lmax:
#         lmax = l[i]
# print(lmax)



# l = [23,65,45,98,75,35] 
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i] > l[j]:
#             l[i],l[j] = l[j],l[i] 
# print(l)

        # Diamond shape 


# n = int(input("enter number of rows : ")) 
# for i in range(n+1):
#     print('  '*(n-i) + ' *  '*i) 
# for i in range(n-1, -1,-1):
#     print('  '*(n-i) + ' *  '*i) 

# import re 
# s = input('Enter mobile number : ') 
# f = re.match(r"(\+91|91|0)?[\s]?[7-9][0-9]{9}",s) 
# if f: 
#     print('valid') 
# else: 
#     print('invalid')


# for i in range(1,1000):
#     if i > 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 break 
#         else:
#             print(i, end=' ')


#  program for reverse number 

# n = int(input("enter any number : "))
# sum = 0 
# while n > 0:
#         r = n % 10 
#         sum = sum * 10 + r 
#         n = n // 10 
# print(sum)


# n = int(input("enter any number !   ")) 
# for i in range(n+1):
#         if i % 2 == 0:
#                 print("buzz") 
#         elif i % 2 == 1:
#                 print("fuzz")
#         else:
#                 print('buzz fuzz')



# n = int(input("Enter any number! "))
# for i in range(n + 1):
#     if i % 4 == 0:
#         print("buzz fuzz")  # Special case for multiples of 4
#     elif i % 2 == 0:
#         print("buzz")
#     else:
#         print("fuzz")                