mydict={
    "fast":"to walk in a fast manner ",
    "nitai":"a fast a coder",
    "marks":[1,3,4],
    "anotherdict":{"nitai":"handsome"},
    1:2

}
print(mydict.keys())       #printing the keys of dictionary
print(list(mydict.keys())) #print the list in the form of keys
print(mydict.values())     #to print value of keys
print(mydict.items())      #print keys value of all in dictionar
updatedict={
    "pranjal":"best friend"
}
mydict.update(updatedict)       #update the value in dictionary
print(mydict)
print(mydict.get("nitai2"))    #it will not throw a error it will return none
print(mydict["nitai2"])       #differnce is that it will give error as[] means you know this present in the dictonary
