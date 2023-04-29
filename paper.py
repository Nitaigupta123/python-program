# ls=[]
# x=int(input())
# for i in range(0,x):
#     y=int(input())
#     ls.append(y)
# print(ls)    
# a='harry'
# l=len(a)
# for i in range(l+1):
#    k=a[::-1]
# print(k)  
# n=int(input())  
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end='')
#     for j in range(i+1):
#         print(j+1,end='  ')
#     print()        
# out=print('hello')or print('python')
# print(out,type(out))
# a='aaabbc'
# for i in a:
#     l=ord(a[i])
#     k=ord(a[i+1])
#     if l==k:
#         pass
#     else:
#         l=k  
# n=int(input())
# ls =str(map(int,input().split()))
# input_string = input("Enter name separated by space: ")

# # Split string into words
# lst = input_string.split(" ")

# print(lst)
# st=input('')
# ls=st.split()
# ls1=[]
# k=len(ls)
# out=st.title
# for i in st:
#     if i == out:
#         ls1.append('true')
#     else:
#         ls1.append('false')     
# print(ls1)       
# n=input()
# ls=list(n) 
# for i in ls:
#     k=ls.count(i)
#     if k==1:
#         print(i)
#         break
# else:
#     print('none')    
# ls=list(map(int ,input().split('x')))
# m=ls[0]
# n=ls[1]
# count=0
# for i in range(n):
#     for j in range(m):
#         if (i+j)%2!=0:
#             count+=1
# print(count)            
# st=input()
# ls=list(st)
# print(ls)
# for i in ls:
#     if i=='R'and i=='G':
#         ls.replace('B')
#     if i=='B' and i=='R':
#         ls.replace('G')
#     if i=='B' and i=='G':
#         ls.replace('R')
# print(ls)                
# employee={}
# ls1=[]
# ls2=[]
# for i in range(4):
#     name=input()
#     age=int(input())
#     if age>40 and age<20:
#         ls1.append(name)
#     else:
#         ls2.append(age)    
# print(ls1)
# print(ls2)
# bar={}
# count=0
# for i in range(2):
#     index=int(input())
#     ls=list(map(int,input().split()))
#     bar[index]=ls
#     k=list(bar.values())
#     if k==i:
#         count+=1

# print(bar)
# print(k)
# print
# n=input()
# m=input()
# ls1=list(n)
# ls2=list(m)
# count=0
# k=ls1[::-1]
# l=ls2[::-1]
# if k==ls1:
#     count+=1
# else:
#     pass    
# dict={}
# for i in range(3):
#     name=input()
#     salary=int(input())
#     dict[name]=salary
#     sort=sorted(dict)
# print(sort)      
# dict={0:10,1:20}
# newdict={0:10,1:20,2:30}
# k=dict.update(newdict)
# print(dict)
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict={}
for d in(dict1,dict2,dict3):
    dict.update(d)
print(dict)
