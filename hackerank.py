# n=int(input("enter the number\n"))
# for i in range(1,n):
#     print(i*i)
#     i=i+1
# a=int(input("entert he amount\n"))
# s=a//2000
# print(s)
# l=a%2000                          #atm conversion
# print(l/500)
# f=l%500
# print(f/200)
# p=f%200
# print(p/100)
n=int(input("enter the number the subjects"))
sub=[]
for i in range(1,n+1):
    val=int(input("enter marks:"))
    sub.append(val)
i=i+1
for i in sub:
    print("marks in",sub.index(i),"subject",i)


