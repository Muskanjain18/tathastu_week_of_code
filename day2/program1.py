n = int(input("Enter any number: "))
#check for odd/even
if(n%2==0):
    print("It is even number")
else:
    print("It is odd number")
#check for prime number
count=0
i=2
while i<n:
    if n%i==0:
        count=count+1
    i=i+1
if(count==0):
    print("It is prime number")
else:
    print("Not a prime number")
#check for armstrong number
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if(sum==n):
    print("It is armstrong number")
else:
    print("Not an armstrong")
#check for palindrome number
temp=n
rev=0
while temp>0:
    d=temp%10
    rev=rev*10+d
    temp=temp//10
if(n==rev):
    print("It is palindrome nnumber")
else:
    print("Not a palindrome number")
