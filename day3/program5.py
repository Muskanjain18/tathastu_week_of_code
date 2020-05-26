s1 = int(input("Enter the no of elemnets you want to enter in the list 1: "))
print("Enter the elments in List1 one by one")
list1 = []
for i in range(s1):
    list1.append(input())
size2 = int(input("Enter the no of elemnets you want to enter in the list 2: "))
print("Enter the elments in List2 one by one")
list2 = []
for i in range(size2):
    list2.append(input())
intersectionList = list(set(list1).intersection(set(list2)))
print("The intersection of List1 and List2 is:",",".join(intersectionList))
