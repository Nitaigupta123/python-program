#ROCK PAPER SCISSOR

import random
l=['ROCK','PAPER','SCISSOR']
while(True):
    ans=random.choice(l)
    i=input('ENTER UR CHOICE ')
    print('\n')
    i=i.upper()
    if i==ans:
        print('DRAW')
    elif (i=='PAPER' and ans=='ROCK') or (i=='ROCK' and ans=='SCISSOR') or (i=='SCISSOR' and ans=='PAPER'):
        
        print('computer chose ',ans)
        print('u chose ',i)
        print("\nU WON")
        print()
    elif (ans=='PAPER' and i=='ROCK') or (ans=='ROCK' and i=='SCISSOR') or (ans=='SCISSOR' and i=='PAPER'):
        
        print('computer chose ',ans)
        print('u chose ',i)
        print("\nCOMPUTER WON")
        print()
    else:
        print('INVALID INPUT')
        print('PROBABLY U TYPED WRONG SPELLING')