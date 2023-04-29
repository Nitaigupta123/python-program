def sum_recursive(n):
    if n<=1:
        return n
    else:
        return n+sum_recursive(n-1)
f=(sum_recursive(5))
print(f)


# def rsum(n):
#     if n <= 1:
#         return n
#     else:
#         return n + rsum(n-1)

# num = int(input("Enter a number: "))
# ttl=rsum(num)
# print("The sum is",ttl)