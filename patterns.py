# for i in range (1,5):
#     for j in range(1,5):
#         print('*',end='')
#     print()    
# for i in range(1,5):
#     for j in range(1,5):
#         if j<=i:
#             print('*',end='')
#         else:
#             print('',end='') 
#     print()           
# for i in range(1,5):
#     for j in range(1,5):
#         if j>=5-i:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()            
# for i in range(1,5):
#     for j in range(1,5):
#         if j<=5-i:
#             print('*',end='')
#         else:
#             print(' ',end='')
# #     print()            
# for i in range(1,5):
#     for j in range(1,5):
#         if j>=i:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print() 
# for i in range (1,5):
#     for j in range(1,8):
#         if j>=5-i and j<=3+i:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
# for i in range (1,5):
#     for j in range(1,8):
#         if j>=i and j<=8-i:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()   
# for i in range (1,5):
#     for j in range(1,8):
#         if j<=5-i or j>=3+i:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print() 
# for i in range (1,5):
#     for j in range(1,5):
#         if j<=i:
#             print(j,end='')
#         else:
#             print(' ',end='')
#     print()   
# for i in range (1,6):
#     k=6-i
#     for j in range(1,6):
#         if j<=6-i:
#             print(k,end='')
#             k-=1
#         else:
#             print(' ',end='')
#     print()   
n=int(input())                         
# for i in range(n-1,-1,-1):
#     for j in range(n-i-1):
#         print(' ',end='')
#     for j in range(i+1):
#         print(j+1,end=' ')
#     print()    
for i in range(n):
    for j in range(n-i):
        print(n-i,end='')
    print()    
