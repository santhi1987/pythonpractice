n = int(input("Enter number : "))

while(n > 0):
    reminder = n % 10
    
    n = n // 10
    print(reminder,end= " ")
