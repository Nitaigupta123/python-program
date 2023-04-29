# n=4
# for i  in range(4):
#   print("*"*i)
n=4
for i in range(4):
    print(" " *(n-i-1),sep="")
    print("*" *(2*i+1),sep="")
    print(" " *(n-i-1))