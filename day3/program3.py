def duplicate(string) :
    dupstr =""
    for x in string:
        if x not in dupstr:
            dupstr += x
    return dupstr
string=input("Enter the string: ")
print("String after removing the duplicates is:",duplicate(string))
