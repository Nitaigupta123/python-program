# r=int(input())
# c=int(input())
# ls=[]
# for i in range(r):
#     ls1=[]
#     for j in range(c):
#         y=int(input())
#         ls1.append(y)
#     ls.append(ls1)
# for i in range(r):
#     for j in range(c):
#         if i==j:
#             print(ls[i][j],end='')
#         else:
#             print('',end='')  
# print()        
            
r=int(input())
c=int(input())
ls=[]
for i in range(r):
    ls1=[]
    for j in range(c):
        y=int(input())
        ls1.append(y)
    ls.append(ls1)
for i in range(r):
    for j in range(c):
        if ((i+j)>r-1):
            print(ls[i][j],end='')
        else:
            print('',end='')
print()                    
