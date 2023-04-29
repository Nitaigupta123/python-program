import random
l=[1,2,3,4,5,6]
ans=random.choice(l)
if ans==1:
    print('[*]')
elif ans==2:
    print('[**]')
elif ans==3:
    print('[***]')
elif ans==4:
    print('[****]')
elif ans==5:
    print('[*****]')
else:
    print('[******]')                    