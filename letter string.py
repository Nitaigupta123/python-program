letter='''Dear <|NAME|>,
you are selected!
i am happy that you are selected in AMAZON on
<|DATE|>
'''
name =input("enter your name\n")
date=input("enter the date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)

  