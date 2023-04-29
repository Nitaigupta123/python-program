# # a=lambda r:3.14*r**2
# # r=int(input())
# # # print(a(r))
# # b=lambda x,y: max(x,y)
# # x=int(input())
# # y=int(input())
# # print(b(x,y))
# # lst=['vehicle','object','human','water']
# # slc=lst[-1:-1:6]
# # print(slc)
# ls=list(map(int,input().split()))
# ls1=[i*i for i in ls if i%2!=0]
# print(*ls1)
# def sep(x):
#     if x%2==0:
#         return True
#     else:
#         return False
    
# ls=[21,34,2,1,4,]
# ls1=list(filter(sep,ls))
# print(ls1)
def prime(n):
   
    c=0
    for i in range(2,100):
        if n%i==0:
            c+=1
            return True
        else:
            return False
        
x=int(input())
print(prime(x))                


    
        
     





