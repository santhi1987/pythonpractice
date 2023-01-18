number=int(input("Enter a number:"))
t=number
rev=0
while(number>0):
    dig=number%10
    rev=rev*10+dig
    number=number//10
if(t==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
