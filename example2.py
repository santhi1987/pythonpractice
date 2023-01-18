list1 = []
a = int(input("Enter number of elements : "))
for i in range(0, a):
	element = int(input())
	lst.append(element)
print(list1)
print("divisable by 5:")
for i in range(0, a):
    if (list1[i]%5==0):
        print (list1[i])
