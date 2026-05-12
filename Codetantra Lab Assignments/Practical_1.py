#1.1.1 Calculate Momentum
m = float(input())
v = float(input())
momentum = m * v
print(f"{momentum:.2f}kgm/s")


#1.1.2 Conditional Calculation Based on the Number of Digits
n = int(input(""))
if 0<=n<10:
	print(n*n)
elif 10<=n<100:
	a = n**0.5
	print("{:.2f}".format(a),end = "\n")
elif 100<=n<1000:
	b = n**(1/3)
	print("{:.2f}".format(b),end = "\n")
else:
	print("Invalid\n")
	

#1.1.3. Days between Two Dates
from datetime import date
d1 = input()
d2 = input()

date1 = date(int(d1[0:4]),int(d1[5:7]),int(d1[8:10]))
date2 = date(int(d2[0:4]),int(d2[5:7]),int(d2[8:10]))

days = date2 - date1
print(days.days)

#1.1.4. Reverse a Number 
n = int(input())
print(int(str(n)[::-1]))


#1.1.5. Multiplication Table
n = int(input())
for i in range(1,11):
	result = n * i
	print(f"{n} x {i} = {result}")


#1.2.1. Pass or Fail
# Input number of courses
n = int(input())

# Input marks for the courses
marks = list(map(int, input().split()))

# Check if the number of marks matches the number of courses
if len(marks) != n:
    print("Invalid input")
else:
    # Check if student failed in any course
    if any(mark < 40 for mark in marks):
        print("Fail")
    else:
        # Calculate aggregate percentage
        aggregate = sum(marks) / n
        
        # Print aggregate formatted to two decimal places
        print(f"Aggregate Percentage: {aggregate:.2f}")
        
        # Determine grade
        if aggregate > 75:
            print("Grade: Distinction")
        elif 60 <= aggregate < 75:
            print("Grade: First Division")
        elif 50 <= aggregate < 60:
            print("Grade: Second Division")
        elif 40 <= aggregate < 50:
            print("Grade: Third Division")


#1.2.2. Fibonacci Series
def fibonacci(n):
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)

n= int(input())
for i in range(n):
	print(fibonacci(i),end=" ")
	
#1.2.3. Pattern - 1
a = int(input())
for i in range(1,a+1):
	print("* "*i)

	
#1.2.4. Pattern - 2
a = int(input())
for i in range (1,a+1):
	for j in range(1,i+1):
		print(j, end=" ")
	print()

