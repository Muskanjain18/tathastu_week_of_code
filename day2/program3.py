n=int(input("Enter the number:"))          #Get the input from the user
for i in range(0,n):                       
    for j in range(0,n):
        if(i==j or j==n-1-i):
            print("*",end=" ")             #print the stars
        else:
            print(" ",end=" ")             #corresponding spaces
    print()                                #next line
 
