def greatest(n1,n2,n3):
    if n1>=n2 and n1>=3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3
k= greatest(12,34,56)    
print(k)

