
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


# DIAMOND SHAPE 


# n = int(input("enter no. of rows !!  ")) 
# for i in range(n+1):
#     print('  '*(n-i) + ' *  '*i) 
# for i in range(n-1, -1,-1):
#     print('  '*(n-i) + ' *  '*i)



# triangle shape rotation 

# n = int(input("enter no. of rows !!  ")) 
# for i in range(n+1):
#     print('  '*(n-i) + '* '*i) 
# for i in range(n-1, -1,-1):
#     print('  '*(n-i) + '* '*i)


# n = int(input("enter no. of rows !!  ")) 
# for i in range(n+1):
#     print('* '*i) 
# for i in range(n-1, -1,-1):
#     print('* '*i)



# find maximum number in the list 


# l = [23,65,45,98,75,35] 
# d =l[-3]
# for i in range(len(l)):
#     if l[i] > d:
#         d = l[i] 
# print(d) 


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = int(input("Enter a number: ")) 
# print("The factorial of", n, "is", factorial(n)) 



# n = int(input("enter any number !  ")) 
# for i in range(1,11):
#     a = n * i 
#     print(n,"*",i,"=",a)



# a = lambda a, b : a + b 
# print(a(2,3))



# import datetime 
# from datetime import timedelta , date
# t = date.today() + timedelta(days=10)
# print(t) 


# import random 
# a = random.randint(000000,999999)
# print(f'{a:06d}')


# def kumar(mukesh):
#     def abc():
#         d = mukesh()
#         e = d * 10000
#         return e
#     return abc
# @kumar
        
# def mukesh():
#     a = 10 
#     b = 20
#     c = a + b 
# #     print(c)
#     return c 
# m = mukesh()
# print(m) 





# s = 'rohit shrama'
# v = ['a','e','i','o','u']
# for i in s:
#     if i in v:
#         print('vowel',i)
#     else:
#         print('consonant',i)


# s = 'rohit shrama'
# v = ['a','e','i','o','u']
# for i in s:
#     if i in v:
#         print('vowel',i) 
# for i in s:
#     if i not in v and i != ' ':
#         print('consonant',i)
 



# method overloading example in python 

# class Polymer:
#     def abc(self , a= None, b = None,c = None):
#        if a != None and b != None and c != None:
#            return a + b + c
#        elif a != None and b != None:
#            return a + b
#        else:
#            return a 
       
# p = Polymer()
# print(p.abc(2,3,4))
# print(p.abc(2,3))
# print(p.abc(2))
# print(p.abc())


# n = int(input("entre how many number rows : ")) 
# for i in range(n+1):
#     print('  '*(n-i) + '* '*i) 
# for i in range(n-1,-1,-1):
#     print('  '*(n-i) + '* '*i) 




# n = int(input("entre how many number rows : ")) 
# for i in range(n+1):
#     print('*'*(n-i)) 
# for i in range(n-1,-1,-1): 
#     print('*'*(n-i)) 



# a = 10 
# def add():
#     global a
#     a = 40  # change the value of global variable inside the function add()
#     print(a)
#     a = 20  # local variable 
#     print(a) 
# add() 




# class Abcde:
#     def __init__(self,a ,b):
#         self.a = a 
#         self.b = b 
#         print(a)
#         print(b)

# a = Abcde(10,20)



# class Abcde:
#     def __init__(self,a ,b):
#         print(a)
#         print(b)
# a = Abcde(10,20) 


# class Abcd:
#     def __init__(self):
#         self.a = 10   # a ,b is instance variable . 
#         self.b = 20   # instance method : - those function contains self as a parameter
#         print(self.a)
#         print(self.b)

# a = Abcd()




# class Computer:
#     def abcd(self):
#         print('I m fathor of computer ') 

# class Laptop(Computer):
#     def abc(self):
#         print('I m child of computer') 

# l = Laptop()
# l.abc()
# l.abcd()

# count = 0 
# for i in range(1,1000):
#     if i > 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 break 
#         else:
#             count = count + 1 
#             print(i , end= ' ')   
          
# print('total number of prime number : ' ,count) 




# s = 'india is great' 
# a = s.split()
# b = a[::-1]
# c = ' '.join(b)
# print(c)


# s = 'india is great'.split()
# for  i in s:
#     a = i[::-1]
#     b = a.title()
#     c = b[::-1]
#     d = ''.join(c)
#     print(d,end=' ')


# o/p : - indiA iS greaT 



# s = 'patna is beautifull place'
# a = s[::-1] 
# b = a.title()
# c = b[::-1]
# print(c,end=' ') 


# #  patnA iS beautifulL placE



s = 'patna is beatiful place'.title()
print(s,end=' ') 