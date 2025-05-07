# n = int(input("entre no. of rows "))
# for i in range(1,n+1):
#     print("*"*i)

# O/P :
# *
# **
# ***
# ****
# *****
# ******
# n = int(input("enter no. of rows "))
# for i in range(1,n+1):
#     print("*  "*i)
# for i in range(n-1,0,-1):
#     print("*  "*i)

# O/p : 
# *  
# *  *  
# *  *  *  
# *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  *  
# *  *  *  *  *  *  *  
# *  *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  
# *  *  *  
# *  *  
# *  

# n = int(input("enter no. of rows "))
# for i in range(1,n+1):
#     print("  "*(n-i)+"* "*i)
# for i in range(n-1,0,-1):
#     print("  "*(n-i)+"* "*i)
# O/P:

#   	      * 
#           * * 
#         * * *
#       * * * *
#     * * * * *
#   * * * * * *
# * * * * * * *
#   * * * * * *
#     * * * * *
#       * * * *
#         * * *
#           * *
#             *

# n = int(input("enter no. of rows "))
# for i in range(1,n+1):
#     print("  "*(n-i)+" *  "*i)
# for i in range(n-1,0,-1):
#     print("  "*(n-i)+" *  "*i)
# O/p : 

#    	       *  
#            *   *  
#          *   *   *          
#        *   *   *   *        
#      *   *   *   *   *      
#    *   *   *   *   *   *    
#  *   *   *   *   *   *   *  
#    *   *   *   *   *   *    
#      *   *   *   *   *      
#        *   *   *   *        
#          *   *   *          
#            *   *  
#              *  

# n = int(input("enter no. of rows "))
# for i in range(1,n+1):
#     print("  "*(n-i)+" *  "*i)

# O/P:
#   	       *  
#            *   *  
#          *   *   *          
#        *   *   *   *        
#      *   *   *   *   *      
#    *   *   *   *   *   *    
#  *   *   *   *   *   *   *  

# n = int(input("enter no. of rows "))
# for i in range(n-1,0,-1):
#     print("  "*(n-i)+" *  "*i)
# O/P:
#   *   *   *   *   *   *  
#      *   *   *   *   *    
#        *   *   *   *      
#          *   *   *        
#            *   *          
#              *  
# n = int(input("enter no. of rows "))
# for i in range(1,n+1):
#     print("  "*(n-i)+"* "*i)
# O/P:
#  	          * 
#           * * 
#         * * * 
#       * * * * 
#     * * * * * 
#   * * * * * * 
# * * * * * * * 

# n = int(input("enter no. of rows "))
# for i in range(n-1,0,-1):
#     print("  "*(n-i)+"* "*i)
# O/P:
#   * * * * * * 
#     * * * * * 
#       * * * * 
#         * * * 
#           * * 
#             * 

# n = int(input("enter no. of rows "))
# for i in range(n,0,-1):
#     print("* "*i)
# O/P:
# * * * * * * * 
# * * * * * *   
# * * * * *     
# * * * *       
# * * *         
# * * 
# * 


# n = int(input("entre no. of rows  "))
# for i in range(n-1,0,-1):
#     print("  "*(n-i)+" *  "*i)
# for i in range(2,n+1):
#     print("  "*(n-i)+" *  "*i) 
# O/P:
#   *   *   *   *  *  
#    *   *   *   *    
#      *   *   *      
#        *   *        
#          *          
#        *   *        
#      *   *   *      
#    *   *   *   *    
#  *   *   *   *   *  

# n = int(input("entra no. of rows "))
# num = 1 
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(num , end=" ")
#         num = num+1
#     print()             # change for new line for rows

# O/P:
# entra no. of rows 5
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10       
# 11 12 13 14 15 


# n = int(input("entra no. of rows "))
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(col , end=" ")
#         col = col+1
#     print()             # change for new line for rows

# O/P:
# entra no. of rows 5
# 1         
# 1 2       
# 1 2 3     
# 1 2 3 4   
# 1 2 3 4 5 

# n = int(input("entre no. of rwos "))
# for row in range(n, 0, -1):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()

# O/P:
# entre no. of rwos 5
# 1 2 3 4 5 
# 1 2 3 4   
# 1 2 3     
# 1 2       
# 1       

# n = int(input("entre no. of rwos "))
# for row in range(n, 0, -1):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()

# O/P:

# entre no. of rwos 7
# 7 7 7 7 7 7 7 
# 6 6 6 6 6 6   
# 5 5 5 5 5     
# 4 4 4 4       
# 3 3 3         
# 2 2 
# 1 

# n = int(input("entre no. of rows "))
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(row,end=" ")
#         col = col + 1
#     print()

# O/P :- 
# 1 
# 2 2 
# 3 3 3         
# 4 4 4 4       
# 5 5 5 5 5     
# 6 6 6 6 6 6   
# 7 7 7 7 7 7 7 

# n = int(input("entre no. of rows "))
# for i in range(n-1,0,-1):
#     print(str(n)*i)
#     n = n+1
   
# O/P:-
# 5555
# 666 
# 77  
# 8   

# n = int(input("entre no. of rows "))
# for i in range(n-1,0,-1):
#     print(str(n)*i)
   
# O/P:-
# 5555
# 555 
# 55  
# 5  

# n = int(input("entre no. of rows "))
# for i in range(1,n+1):
#     print(" "*(n-i)+ str(n)*i)    
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+ str(n)*i)

# O/P:-  
#     5
#    55
#   555
#  5555
# 55555
#  5555
#   555
#    55
#     5

# n = int(input("entre no. of rows "))
# for i in range(1,n+1):
#     print(" "*(n-i)+"  "+str(n)*i)    
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"  "+str(n)*i)

# O/P:-
#       5
#      55
#     555
#    5555
#   55555
#    5555
#     555
#      55
#       5

# n = int(input("entre no. of rows "))
# for i in range(1,n+1):
#     print(str(n)*i)
# for i in range(n-1,0,-1):
#     print(str(n)*i)

# O/P:-
#   5    
#   55   
#   555  
#   5555 
#   55555
#   5555 
#   555  
#   55   
#   5    

# n = int(input("entre no. of rows ")) 
# for i in range(1,n+1):
#     print(str(n)*i)  

# O/P:- 
# 5    
# 55   
# 555  
# 5555 
# 55555

# n = int(input("entre no. of rows ")) 
# for i in range(1,n+1):
#     print(str(n)*i)  
#     n = n+1
# O/P:- 
# 5    
# 66   
# 777  
# 8888 
# 99999

# n = int(input("entre no. of rows ")) 
# for i in range(1,n+1):
#     print(" "*(n-i)+str(n)*i) 
# O/P:-
#     5
#    55
#   555
#  5555
# 55555

# n = int(input("entre no. of rows ")) 
# for i in range(n,0,-1):
#     print(" "*(n-i)+str(n)*i)  

# O/P:-
# 88888888
#  8888888
#   888888
#    88888
#     8888
#      888
#       88
#        8

# n = int(input("entre no. of rows ")) 
# for i in range(n,0,-1):
#     print(" "*(n-i)+str(n)*i)  
# O/P:-
# 1414141414141414141414141414
#  14141414141414141414141414 
#   141414141414141414141414  
#    1414141414141414141414   
#     14141414141414141414    
#      141414141414141414     
#       1414141414141414      
#        14141414141414       
#         141414141414        
#          1414141414
#           14141414
#            141414
#             1414
#              14


# n = int(input("entre no. of rows "))     
# for i in range(1,n+1):
#     print(" "*(n-i)+str(n)*i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+str(n)*i)
# n = int(input("entre no. of rows ")) 

# O/P:-
#            12
#           1212
#          121212
#         12121212        
#        1212121212       
#       121212121212      
#      12121212121212     
#     1212121212121212    
#    121212121212121212   
#   12121212121212121212  
#  1212121212121212121212 
# 121212121212121212121212
#  1212121212121212121212 
#   12121212121212121212  
#    121212121212121212   
#     1212121212121212    
#      12121212121212     
#       121212121212      
#        1212121212       
#         12121212        
#          121212
#           1212
#            12
# n = int(input("entre no. of rows "))     
# for i in range(1,n+1):
#     print(" "*(n-i)+str(i)*i)  
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+str(i)*i)  
# O/P:-
#       1
#      22
#     333
#    4444
#   55555
#  666666
# 7777777
#  666666
#   55555
#    4444
#     333
#      22
#       1

# n = int(input("entre no. of rows ")) 
# for i in range(1,n+1):
#     print(str(i)*i)  
# for i in range(n-1,0,-1):
#     print(str(i)*i)  
    
# O/P:-
# 1       
# 22      
# 333     
# 4444    
# 55555   
# 666666  
# 7777777 
# 88888888
# 7777777 
# 666666  
# 55555   
# 4444    
# 333     
# 22      
# 1     



# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ") 
#     for j in range(i+1):
#         print(j+1,end=" ") 
#     print()

# O/P:-
#     	    1 
#           1 2 
#         1 2 3 
#       1 2 3 4 
#     1 2 3 4 5 
#   1 2 3 4 5 6 
# 1 2 3 4 5 6 7 

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="") 
#     for j in range(i+1):
#         print(j+1,end=" ") 
#     print()

# O/P:-
#       1       
#      1 2      
#     1 2 3     
#    1 2 3 4    
#   1 2 3 4 5   
#  1 2 3 4 5 6  
# 1 2 3 4 5 6 7 

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()

# O/P:-
#             1 
#           2 1 
#         3 2 1 
#       4 3 2 1 
#     5 4 3 2 1 
#   6 5 4 3 2 1 
# 7 6 5 4 3 2 1 

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()
# O/P:-
#       1       
#      2 1      
#     3 2 1     
#    4 3 2 1    
#   5 4 3 2 1   
#  6 5 4 3 2 1  
# 7 6 5 4 3 2 1 

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ") 
#     for j in range(i+1):
#         print(n-j,end=" ") 
#     print()

# O/P:-
#             7 
#           7 6 
#         7 6 5 
#       7 6 5 4 
#     7 6 5 4 3 
#   7 6 5 4 3 2 
# 7 6 5 4 3 2 1 

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="") 
#     for j in range(i+1):
#         print(n-j,end=" ") 
#     print()
# O/P:-
#       7       
#      7 6      
#     7 6 5     
#    7 6 5 4    
#   7 6 5 4 3   
#  7 6 5 4 3 2  
# 7 6 5 4 3 2 1 

# n = int(input("entre no. or rows ")) 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()

# O/P:-
#   	      7 
#           6 7 
#         5 6 7 
#       4 5 6 7 
#     3 4 5 6 7 
#   2 3 4 5 6 7 
# 1 2 3 4 5 6 7 

# n = int(input("entre no. or rows ")) 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()

# O/P:-
#       7       
#      6 7      
#     5 6 7     
#    4 5 6 7    
#   3 4 5 6 7   
#  2 3 4 5 6 7  
# 1 2 3 4 5 6 7 

# n = int(input("entre no. or rows ")) 
# for i in range(n-1,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()

# O/P:-
# 1 2 3 4 5 6 7 
#  2 3 4 5 6 7  
#   3 4 5 6 7   
#    4 5 6 7    
#     5 6 7     
#      6 7      
#       7       


#     """ ------------------------------- part one video -----------------------------------------"""

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()
# O/P:-
# 1 
# 1 2 
# 1 2 3         
# 1 2 3 4       
# 1 2 3 4 5     
# 1 2 3 4 5 6   
# 1 2 3 4 5 6 7 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()

# O/P:-
# 1 
# 2 1 
# 3 2 1         
# 4 3 2 1       
# 5 4 3 2 1     
# 6 5 4 3 2 1   
# 7 6 5 4 3 2 1 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(i+1,end=" ")
#     print()
# O/P:-
# 1 
# 2 2 
# 3 3 3         
# 4 4 4 4       
# 5 5 5 5 5     
# 6 6 6 6 6 6   
# 7 7 7 7 7 7 7 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(n-i,end=" ")
#     print()
# O/P-
# 7 
# 6 6 
# 5 5 5         
# 4 4 4 4       
# 3 3 3 3 3     
# 2 2 2 2 2 2   
# 1 1 1 1 1 1 1 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()
# O/P:-
# 7 
# 6 7 
# 5 6 7         
# 4 5 6 7       
# 3 4 5 6 7     
# 2 3 4 5 6 7   
# 1 2 3 4 5 6 7 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()
# O/P:-
# 7 
# 6 7 
# 5 6 7         
# 4 5 6 7       
# 3 4 5 6 7     
# 2 3 4 5 6 7   
# 1 2 3 4 5 6 7 


# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(n-i-1):                  # use for space (n-i-1)
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()

# O/P:-
#             7 
#           6 7 
#         5 6 7 
#       4 5 6 7 
#     3 4 5 6 7 
#   2 3 4 5 6 7 
# 1 2 3 4 5 6 7 

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i):
#         print(j+1,end=" ")
#     print()
# O/P:-
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6   
# 1 2 3 4 5     
# 1 2 3 4       
# 1 2 3         
# 1 2 
# 1 

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i):
#         print(i+1,end=" ")
#     print()

# O/P:-
# 1 1 1 1 1 1 1 
# 2 2 2 2 2 2   
# 3 3 3 3 3     
# 4 4 4 4       
# 5 5 5         
# 6 6 
# 7 
# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i):
#         print(n-i,end=" ")
#     print()

# O/P-
# 7 7 7 7 7 7 7 
# 6 6 6 6 6 6   
# 5 5 5 5 5     
# 4 4 4 4       
# 3 3 3         
# 2 2 
# 1 

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i):
#         print(n-j,end=" ")
#     print()
# O/P:-
# 7 6 5 4 3 2 1 
# 7 6 5 4 3 2   
# 7 6 5 4 3     
# 7 6 5 4       
# 7 6 5         
# 7 6 
# 7 

# n= int(input("entre no. of rows "))
# for i in range(n):
#     for j in range(n-i-1,-1,-1):
#         print(j+1,end=" ")
#     print()

# O/P:-
# 7 6 5 4 3 2 1 
# 6 5 4 3 2 1   
# 5 4 3 2 1     
# 4 3 2 1       
# 3 2 1         
# 2 1 
# 1 
# n= int(input("entre no. of rows "))
# for i in range(n):
#     for j in range(n-i-1,-1,-1):
#         print(n-j,end=" ")
#     print()
# O/P:-
# 1 2 3 4 5 6 7 
# 2 3 4 5 6 7   
# 3 4 5 6 7     
# 4 5 6 7       
# 5 6 7         
# 6 7 
# 7 

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(j+1,end=" ")
#     print()

# O/P:-
# 1 2 3 4 5 6 7 
#   1 2 3 4 5 6 
#     1 2 3 4 5 
#       1 2 3 4 
#         1 2 3 
#           1 2 
#             1 

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(i+1,end=" ")
#     print()

# O/P:-
# 1 1 1 1 1 1 1 
#   2 2 2 2 2 2 
#     3 3 3 3 3 
#       4 4 4 4 
#         5 5 5 
#           6 6 
#             7 
# 			# alphabet pattern 

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     k = ord("a")+i
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-
#        a
#       b c
#      c d e
#     d e f g
#    e f g h i
#   f g h i j k
#  g h i j k l m

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ") 
#     for j in range(i+1):
#         print(j+1,end=" ") 
#     print()
# O/P:-
# 	1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 


# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i-1):          # piramid shape use [n-i-1] sidhe wala
#         print(" ",end="") 
#     for j in range(i+1):
#         print(j+1,end=" ") 
#     print()

# O/P:-
#     1     
#    1 2    
#   1 2 3   
#  1 2 3 4  
# 1 2 3 4 5 

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ") 
#     for j in range(i+1):
#         print(n-j,end=" ") 
#     print()

# O/P:-
# 	      5 
#       5 4 
#     5 4 3 
#   5 4 3 2 
# 5 4 3 2 1 

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="") 
#     for j in range(i+1):
#         print(n-j,end=" ") 
#     print()
# O/P:-
#     5     
#    5 4    
#   5 4 3   
#  5 4 3 2  
# 5 4 3 2 1 


# n = int(input("entre no. or rows ")) 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()

# O/P:-
#         5 
#       4 5 
#     3 4 5 
#   2 3 4 5 
# 1 2 3 4 5 

# n = int(input("entre no. or rows ")) 
# for i in range(n-1,-1,-1):              # opposite piramid use [n-1,-1,-1]
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()

# O/P:-
# 1 2 3 4 5 
#  2 3 4 5  
#   3 4 5   
#    4 5    
#     5  

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()
# O/P:-
# 1         
# 1 2       
# 1 2 3     
# 1 2 3 4   
# 1 2 3 4 5

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()

# 1         
# 2 1       
# 3 2 1     
# 4 3 2 1   
# 5 4 3 2 1 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(i+1,end=" ")
#     print()

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(n-i,end=" ")
#     print()

# 5         
# 4 4       
# 3 3 3     
# 2 2 2 2   
# 1 1 1 1 1 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()

# 5         
# 4 5       
# 3 4 5     
# 2 3 4 5   
# 1 2 3 4 5 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()

# 5         
# 4 5       
# 3 4 5     
# 2 3 4 5   
# 1 2 3 4 5 

# n = int(input("ente no. of rows "))
# for i in range(n):
#     for j in range(n-i-1):                  # use for space (n-i-1)
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(n-j,end=" ")
#     print()

#         5 
#       4 5 
#     3 4 5 
#   2 3 4 5 
# 1 2 3 4 5 

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i):
#         print(j+1,end=" ")
#     print()

# 1 2 3 4 5 
# 1 2 3 4   
# 1 2 3     
# 1 2       
# 1         

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i):
#         print(i+1,end=" ")
#     print()

# 1 1 1 1 1 
# 2 2 2 2   
# 3 3 3     
# 4 4       
# 5     

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i):
#         print(n-i,end=" ")
#     print()

# 5 5 5 5 5 
# 4 4 4 4   
# 3 3 3     
# 2 2       
# 1      

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     for j in range(n-i):
#         print(n-j,end=" ")
#     print()

# 5 4 3 2 1 
# 5 4 3 2   
# 5 4 3     
# 5 4       
# 5       

# n= int(input("entre no. of rows "))
# for i in range(n):
#     for j in range(n-i-1,-1,-1):
#         print(j+1,end=" ")
#     print()

# 5 4 3 2 1 
# 4 3 2 1   
# 3 2 1     
# 2 1       
# 1      

# n= int(input("entre no. of rows "))
# for i in range(n):
#     for j in range(n-i-1,-1,-1):
#         print(n-j,end=" ")
#     print()

# 1 2 3 4 5 
# 2 3 4 5   
# 3 4 5     
# 4 5       
# 5         

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(j+1,end=" ")
#     print()

# 1 2 3 4 5 
#   1 2 3 4 
#     1 2 3 
#       1 2 
#         1 

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(i+1,end=" ")
#     print()

# 1 1 1 1 1 
#   2 2 2 2 
#     3 3 3 
#       4 4 
#         5 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):
#     for j in range(i+1):
#         print(str1[i],end=" ")
#     print()

# a 
# b b         
# c c c       
# d d d d     
# e e e e e   
# f f f f f f 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):
#     for j in range(i+1):
#         print(str1[j],end=" ")
#     print()

# a 
# a b         
# a b c       
# a b c d     
# a b c d e   
# a b c d e f 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):
#     for j in range(length-i-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(str1[i],end=" ")
#     print()

# 	        a 
#         b b 
#       c c c 
#     d d d d 
#   e e e e e 
# f f f f f f 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):
#     for j in range(length-i-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(str1[j],end=" ")
#     print()

#           a 
#         a b 
#       a b c 
#     a b c d 
#   a b c d e 
# a b c d e f 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):
#     for j in range(length-i-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print(str1[i],end=" ")
#     print()

#      a      
#     b b     
#    c c c    
#   d d d d   
#  e e e e e  
# f f f f f f 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):
#     for j in range(length-i-1):		 # piramid space print use (n-i-1)
#         print(" ", end="")
#     for j in range(i+1):		 # piramid print use of column (i+1)
#         print(str1[j],end=" ")
#     print()

#      a      
#     a b     
#    a b c    
#   a b c d   
#  a b c d e  
# a b c d e f 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):   
#     for j in range(length-i):
#         print(str1[j],end=" ")
#     print()

# a b c d e f 
# a b c d e   
# a b c d     
# a b c       
# a b         
# a 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):   
#     for j in range(length-i):
#         print(str1[i],end=" ")
#     print()

# a a a a a a 
# b b b b b   
# c c c c     
# d d d       
# e e         
# f 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):   
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(length-i):
#         print(str1[i],end=" ")
#     print()

# a a a a a a 
#   b b b b b 
#     c c c c 
#       d d d 
#         e e 
#           f 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):   
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(length-i):
#         print(str1[j],end=" ")
#     print()

# a b c d e f 
#   a b c d e 
#     a b c d 
#       a b c 
#         a b 
#           a 

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):   
#     for j in range(i):
#         print(" ",end="")
#     for j in range(length-i):
#         print(str1[j],end=" ")
#     print()

# a b c d e f 
#  a b c d e  
#   a b c d   
#    a b c    
#     a b     
#      a      

# str1 = input("entre string ")
# length = len(str1)
# for i in range(length):   
#     for j in range(i):
#         print(" ",end="")
#     for j in range(length-i):
#         print(str1[i],end=" ")
#     print()

# a a a a a a 
#  b b b b b  
#   c c c c   
#    d d d    
#     e e     
#      f      

# str1 = input("entre string ") 
# length = len(str1)
# for i in range(length-1,-1,-1):
#     for j in range(length-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(str1[i],end=" ")
#     print()

# f f f f f f 
#   e e e e e 
#     d d d d 
#       c c c 
#         b b 
#           a 

# str1 = input("entre string ") 
# length = len(str1)
# for i in range(length-1,-1,-1):
#     for j in range(length-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(str1[j],end=" ")
#     print()

# a b c d e f 
#   a b c d e 
#     a b c d 
#       a b c 
#         a b 
#           a 

# str1 = input("entre string ") 
# length = len(str1)
# for i in range(length-1,-1,-1):
#     for j in range(length-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(str1[j],end=" ")
#     print()

# a b c e d f 
#  a b c e d  
#   a b c e   
#    a b c    
#     a b     
#      a      

# str1 = input("entre string ") 
# length = len(str1)
# for i in range(length-1,-1,-1):
#     for j in range(length-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(str1[j],end=" ")
#     print()

# f d e c b a 
#   d e c b a 
#     e c b a 
#       c b a 
#         b a 
#           a 

# n = int(input("entre no. of rows ")) 
# k = ord("a")
# for i in range(n):
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# a         
# b c       
# d e f     
# g h i j   
# k l m n o 


# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     k = ord("a")+i
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# a         
# b c       
# c d e     
# d e f g   
# e f g h i

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     k = ord('a')
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

#           a 
#         a b 
#       a b c 
#     a b c d 
#   a b c d e 
# a b c d e f 

# n = int(input("entre no. of rows ")) 
# for i in range(n):
#     k = ord('a')
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# a 
# a b         
# a b c       
# a b c d     
# a b c d e   
# a b c d e f 

# n = int(input("entre no. of rwos "))
# for i in range(n):
#     k = ord('a')
#     for j in range(n-i-1):		# piramid space print use (n-i-1)
#         print(" ",end="")
#     for j in range(i+1):		# piramid print use of column (i+1)
#         print(chr(k),end=" ")
#         k = k+1
#     print()

#      a      
#     a b     
#    a b c    
#   a b c d   
#  a b c d e  
# a b c d e f 

# n = int(input("entre no. of rows "))
# for i in range(n-1,-1,-1):
#     k = ord('a')
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# a b c d e f 
#  a b c d e  
#   a b c d   
#    a b c    
#     a b     
#      a      

# n = int(input("entre no. of rows "))
# for i in range(n):
#     k = ord('a')
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()
# for i in range(n-2,-1,-1):
#     k = ord('a')
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-
#       a       
#      a b      
#     a b c     
#    a b c d    
#   a b c d e   
#  a b c d e f  
# a b c d e f g 
#  a b c d e f  
#   a b c d e   
#    a b c d    
#     a b c     
#      a b      
#       a       

# n = int(input("entre no. of rows "))
# for i in range(n-1,0,-1):
#     k = ord('a')
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()
# for i in range(n):
#     k = ord('a')
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-

# a b c d e f g 
#  a b c d e f  
#   a b c d e   
#    a b c d    
#     a b c     
#      a b      
#       a       
#      a b      
#     a b c     
#    a b c d    
#   a b c d e   
#  a b c d e f  
# a b c d e f g 

# n = int(input("entre no. of rows ")) 
# k = ord('a')
# for i in range(n):   
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-
#     a     
#    b c    
#   d e f   
#  g h i j  
# k l m n o 

# n = int(input("entre no. of rows ")) 
# k = ord('a')
# for i in range(n):   
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-
# 	      a 
#       b c 
#     d e f 
#   g h i j 
# k l m n o 

# n = int(input("entre no. of rows ")) 
# k = ord('a')
# for i in range(n-1,-1,-1):   
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-
# a b c d e 
#   f g h i 
#     j k l 
#       m n 
#         o 

# n = int(input("entre no. of rows ")) 
# k = ord('a')
# for i in range(n-1,-1,-1):   
#     # for j in range(n-i-1):
#     #     print(" ",end=" ")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-

# a b c d e 
# f g h i   
# j k l     
# m n       
# o 

# n = int(input("entre no. of rows "))
# num = 1
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(num,end=" ")
#         num = num+1
#     print()

# O/P:-

#       1 
#      2 3 
#     4 5 6 
#    7 8 9 10 
#   11 12 13 14 15     
#  16 17 18 19 20 21   
# 22 23 24 25 26 27 28 

# n = int(input("entre no. of rows "))
# k = ord('a')
# for i in range(1,n+1):
#     # k = ord('a')
#     print(" "*(n-i)+str(chr(k))*i)
#     k = k+1
# for i in range(n-1,-1,-1):
#     print(" "*(n-i)+str(chr(k))*i)
#     k = k+1

# O/P:-
#     a
#    bb
#   ccc
#  dddd
# eeeee
#  ffff
#   ggg
#    hh
#     i

# n = int(input("entre no. of rows "))
# k = ord('a')
# for i in range(1,n+1):
#     # k = ord('a')
#     print(str(chr(k))*i)
#     k = k+1
# for i in range(n-1,-1,-1):
#     print(str(chr(k))*i)
#     k = k+1

# O/P:-
# a    
# bb   
# ccc  
# dddd 
# eeeee
# ffff 
# ggg  
# hh   
# i

# n = int(input("entre no. of rows "))
# k = ord('a')
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-
#         a
#       b c
#     d e f
#   g h i j
# k l m n o
#   p q r s
#     t u v
#       w x
#         y

# n = int(input("entre no. of rows "))
# k = ord('a')
# for i in range(n):
#     for j in range(n-i-1):
#         print(end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-
# a         
# b c       
# d e f     
# g h i j   
# k l m n o 
# p q r s   
# t u v
# w x
# y

# n = int(input("entre no. of rows "))
# k = ord('a')
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k+1
#     print()

# O/P:-
#     a     
#    b c    
#   d e f   
#  g h i j  
# k l m n o 
#  p q r s  
#   t u v
#    w x
#     y

# n = int(input("entre no. of rows "))
# # k = ord('a')
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
# 	#print(chr(k),end=" ")
#         print(i+1,end=" ")
#         # k = k+1
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
# 	#print(chr(k),end=" ")
#         print(i+1,end=" ")
#         # k = k+1
#     print()
# O/P:-
#  	      1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5 
#   4 4 4 4 
#     3 3 3 
#       2 2 
#         1 
# n = int(input("entre no. of rows "))
# num = 1
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(num,end=" ")
#         num = num + 1   
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(num,end=" ")
#         num = num + 1
#     print()
# O/P:-
#     1 
#    2 3         
#   4 5 6        
#  7 8 9 10      
# 11 12 13 14 15 
#  16 17 18 19   
#   20 21 22     
#    23 24       
#     25    

# n = int(input('enter no. of rows  ')) 
# for i in range(n):
#     k = ord('a')
#     for j in range(n-i-1):
#         print(" ",end="") 
#     for j in range(i+1):
#         print(chr(k),end=" ") 
#         k = k + 1
#     print() 
# for i in range(n-2,-1,-1):
#     k = ord('a')
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k = k + 1
#     print() 

# O/P:-

#     a     
#    a b    
#   a b c   
#  a b c d  
# a b c d e 
#  a b c d  
#   a b c   
#    a b    
#     a      

# n = int(input("entre no. of rows  ")) 
# for i in range((n+1)-1,0,-1):
#     print("  "*(n-i)+" *"*i)  
 
# O/P:-

#  * * * * * * * *
#    * * * * * * *
#      * * * * * *
#        * * * * *
#          * * * *
#            * * *
#              * *
#                *


# n = int(input("enter no. or rows ")) 
# for i in range(n):
# 	for j in range(n-i):
# 		print(" ",end="")
# 	for j in range(i+1):
# 		print(j+1,end=" ")
# 	print() 
# for i in range(n-2,-1,-1):
# 	for j in range(n-i):
# 		print(" ",end="")
# 	for j in range(i+1):
# 		print(j+1,end=" ")
# 	print() 

# O/P:- 

#        1       
#       1 2      
#      1 2 3     
#     1 2 3 4    
#    1 2 3 4 5   
#   1 2 3 4 5 6  
#  1 2 3 4 5 6 7 
#   1 2 3 4 5 6  
#    1 2 3 4 5   
#     1 2 3 4    
#      1 2 3     
#       1 2      
#        1

# 			OR 

# n = int(input("enter no. or rows ")) 
# for i in range(n):
# 	for j in range(n-i-1):
# 		print(" ",end="")
# 	for j in range(i+1):
# 		print(j+1,end=" ")
# 	print() 
# for i in range(n-2,-1,-1):
# 	for j in range(n-i-1):
# 		print(" ",end="")
# 	for j in range(i+1):
# 		print(j+1,end=" ")
# 	print()

# O/P:- 

#       1       
#      1 2      
#     1 2 3     
#    1 2 3 4    
#   1 2 3 4 5   
#  1 2 3 4 5 6  
# 1 2 3 4 5 6 7 
#  1 2 3 4 5 6  
#   1 2 3 4 5   
#    1 2 3 4    
#     1 2 3     
#      1 2      
#       1
 
# n = int(input('entre no. of rows  ')) 
# k = int(input('entre any number  ')) 
# for i in range(n):
# 	for j in range(n-i):
# 		print(" ",end="") 
# 	for j in range(i+1):
# 		print(k, end=" ") 
# 		k = k + 1 
# 	print() 

# O/P: - 

#      1 
#     2 3         
#    4 5 6        
#   7 8 9 10      
#  11 12 13 14 15 



# 				# Z shape pattern 
# i = 1 
# j = 4
# for row in range(0,6):
# 	for col in range(0,6):
# 		if row == 0 or row == 5:
# 			print('*',end="")
# 		elif row == i and col == j:
# 			print('*',end="")
# 			i = i + 1
# 			j = j - 1 
			
# 		else: 
# 			print(end=" ")
# 	print()



# 				# M shape pattern 



# for row in range(7):
# 	for col in range(7):
# 		if (col == 0 or col ==6) or ((row==col) and (col>0 and col<4)) or (row == 1 and col == 5) or (row == 2 and col == 4):
# 			print("*",end="  ")
# 		else:
# 			print(" ", end="  ")
# 	print()



# 					# shubh labh print shape 
# # for row in range(9):
# # 	for col in range(9):
# # 		if row == 4 or (col == 4 and row !=4) or (col == 0 and row <=3) or (col == 8 and row > 4) or (row == 0 and col > 4) or (row == 8 and col < 4):
# # 			print("*",end="  ")
# # 		else:
# # 			print(' ',end='  ')
# # 	print()


# # 						# hollow dimond program 

# # for row in range(7):
# # 	for col in range(7):
# # 		if row + col == 3 or col - row == 3 or row - col == 3 or row + col == 9:
# # 			print("*",end=' ')
# # 		else:
# # 			print(" ",end=" ")
# # 	print()


# 						# heart shape program 


# # for row in range(6):
# # 	for col in range(7):
# # 		if (row == 0 and col %3 !=0) or (row == 1 and col %3 == 0) or (row - col == 2) or (row + col == 8):
# # 			print("*",end="  ")
# # 		else:
# # 			print(" ",end="  ")
# # 	print() 
			

# n = int(input('enter no. of rows : ')) 
# for i in range(1,n+1):
# 	for j in range(1,n-i+1):
# 		print(' ',end=' ')
# 	for j in range(i,0,-1):
# 		print(j,end=' ')
# 	for j in range(2,i+1):
# 		print(j,end=' ')
# 	print()

# O/P:-  enter no. of rows : 7
#       1
#      212
#     32123
#    4321234
#   543212345        
#  65432123456       
# 7654321234567      


# 				# hollow triangle program 
# for row in range(5):
# 	for col in range(9):
# 		if row == 4 or (row+col == 4) or (col - row == 4):
# 			print('*',end=' ')
# 		else:
# 			print(' ',end=' ')
# 	print() 

# O/P:- 
#         *
#       *   *       
#     *       *     
#   *           *   
# * * * * * * * * * 


# n = int(input('enter number of rows  ')) 
# col = n + n - 5 
# mid = col // 2 
# for i in range(n):
# 	for j in range(col):
# 		if i == 2 or i == (n-3) or i + j == mid or j-i == mid or i - j == 2 or  i + j == col + 1:
# 			print('*', end= " ") 
# 		else:
# 			print(" ",end=" ")
# 	print()

# O/P:- 
#             *
#           *   *
# * * * * * * * * * * * * * 
#   *   *           *   *   
#     *               *     
#   *   *           *   *   
# * * * * * * * * * * * * * 
#           *   *
#             *

# 			# 2nd method 

# # for i in range(9):
# # 	for j in range(13):
# # 		if i == 2 or i == 6 or i + j == 6 or j - i == 6 or i-j == 2 or i + j == 14:
# # 			print('*',end=' ')
# # 		else:
# # 			print(' ',end=' ')
# # 	print()

# 				# sprial program in python 


# num = int(input("enter the number of rows  "))
# n_list = [[0 for x in range(num)] for y in range(num)] 
# n = 1 
# low = 0 
# high = num - 1
# count = int((num+1)/2) 
# for i in range(count):
# 	for j in range(low,high+1):
# 		n_list[i][j] = n 
# 		n = n + 1 
# 	for j in range(low + 1, high + 1):
# 		n_list[j][high] = n 
# 		n = n + 1
# 	for j in range(high-1,low-1,-1):
# 		n_list[high][j] = n 
# 		n = n + 1 
# 	for j in range(high-1,low,-1):
# 		n_list[j][low] = n 
# 		n = n + 1
# 	low = low + 1 
# 	high = high - 1 


# for i in range(num):
# 	for j in range(num):
# 		print(n_list[i][j],end="\t")
# 	print()		

# O/P:- enter the number of rows  5

# 1       2       3       4       5
# 16      17      18      19      6
# 15      24      25      20      7
# 14      23      22      21      8
# 13      12      11      10      9