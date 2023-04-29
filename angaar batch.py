
# i=1
# while (i<=1000):
#     print(i)
#     i=i+3
# for i in range(1,101,3):
#     print(i)
# i=i+1
# n=int(input())
# sum=0
# while n>0:
#     r=n%10                               //palindrome of a number

#     sum=(sum*10)+r 
#     n=n//10
# print(sum)   
n=int(input("enter the number")) 
# i=1
# for i in range(1,11):
#     print(f'{n}*{i}={n*i}')
# i=i+1
if  n%2!=0:
    for i in range (1,n+1):
        print(i,end='#')
else:
    print("even")    

    

