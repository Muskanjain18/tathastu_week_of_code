#Fibonacci series
num = int(input("Enter any number: "))
print("Fibonacci series: ")
print('0\n1')
a=0
b=1
c=a+b
print(c)
while c<num:
    a=b
    b=c
    c=a+b
    if(c<num):
        print(c)
