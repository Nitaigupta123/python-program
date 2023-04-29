# this syntax will create an empty dictionary not a empty set
a={}
print(type(a))
# to create an empty set
b=set()
print(type(b))
b.add(8)
b.add(9)            #adding the value in the set
b.add((1,2,3))      # WE CAN ADD THE TUPPLE int the set
print(len(b))       #print the length in a set
b.remove(9)         #remove the element from the set
print(b)
print(b.pop())     #remove the random element from the set