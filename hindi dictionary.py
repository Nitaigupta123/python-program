mydict={
    "aloo":"potato",
    "tamatar":"tomato",
    "pankha":"fan"
    

}
print("your option are",mydict.keys())
a=input("input the hindi word\n")
#print("the meaning of your world is",mydict[a])
#below line will not give anerreor if key is not present in the dictionary
print("the meaning of your word is",mydict.get(a))