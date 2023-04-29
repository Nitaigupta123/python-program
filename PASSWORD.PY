import random
password='ABCDEFGHIJKLMOPQRSTUVWXYZ0123456789abcdefghijklmopqrstuvwxyz!@#$%^&*()'
len=int(input('enter the lenghth of paasword\n'))
a=''.join(random.sample(password,len))
print(a)
