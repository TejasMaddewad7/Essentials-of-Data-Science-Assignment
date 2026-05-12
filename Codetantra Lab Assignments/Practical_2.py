#2.1.1. List operations
list = []
while True:
	print("1. Add\n2. Remove\n3. Display\n4. Quit")
	a = int(input("Enter choice: "))
	if(a==1):
		b = int(input("Integer: "))
		list.append(b)
		print("List after adding:",list)
	elif(a==2):
		if(len(list)==0):
			print("List is empty")
		elif(len(list)>0):
			c= int(input("Integer: "))
			if c in list:
				list.remove(c)
				print("List after removing:",list)
			else:
				print("Element not found")
	elif(a==3):
		if(len(list)==0):
			print("List is empty")
		else:
			print(list)
	elif(a==4):
		break
	else:
		print("Invalid choice")
		

#2.1.2. Dictionary Operations
# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}
print("Original Dictionary:",student)
a = int(input())
b = input()
student[a]=b
print("After Insertion:", student)
a = int(input())
b=input()
if a in student:
	student[a] = b 
print("After Update:",student)
a = int(input())
if a in student:
	student.pop(a)
print("After Deletion:", student)

print("Traversing Dictionary:")
for key, value in student.items():
	print(key,":",value)


#2.2.1. Linear search Technique
a = list(map(int,input().split()))
b = int(input())
found=False
for i in range(len(a)):
	if a[i] ==b:
		print(i)
		found=True
		break

if found == False:
	print("Not found")
	

#2.2.2. Captain of the Team
a = list(map(int,input().split()))
max = a[0]
for i in range(len(a)):
	if a[i]>max:
		max=a[i]
	i+=1
print(max)