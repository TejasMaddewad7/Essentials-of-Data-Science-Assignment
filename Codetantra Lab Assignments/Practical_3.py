#3.1.1. Numpy Array Operations
import numpy as np
def create_array():
	rows, cols = map(int, input().split())
	elements = []
	for _ in range(rows):
		row = list(map(int, input().split()))
		elements.extend(row)
	arr = np.array(elements).reshape(rows, cols)
	return arr
arr = create_array()
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)

#3.2.1. Numpy: Matrix Operations
import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
Add_result=np.add(matrix_a,matrix_b)
print("Addition (A + B):")
print(Add_result)
# Subtraction
Add_result=np.subtract(matrix_a,matrix_b)

print("Subtraction (A - B):")
print(Add_result)
# Multiplication (element-wise)
Add_result=np.multiply(matrix_a,matrix_b)
print("Element-wise Multiplication (A * B):")
print(Add_result)
# Matrix multiplication (dot product)
Add_result=np.dot(matrix_a,matrix_b)
print("A dot B:")
print(Add_result)
# Transpose
Add_result=np.transpose(matrix_a)
print("Transpose of A:")
print(Add_result)

#3.2.2. Numpy: Horizontal and Vertical Stacking of Arrays
import numpy as np

# Input matrices
print("Enter Array1:")
arr1 = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Array2:")
arr2 = np.array([list(map(int, input().split())) for i in range(3)])

# Perform horizontal stacking (hstack)
horizontal_stack=np.hstack((arr1,arr2))
print("Horizontal Stack:")
print(horizontal_stack)

# Perform vertical stacking (vstack)
vertical_stack=np.vstack((arr1,arr2))
print("Vertical Stack:")
print(vertical_stack)


#3.2.3. Numpy: Custom Sequence Generation
import numpy as np

# Take user input for the start, stop, and step of the sequence
start = int(input())
stop = int(input())
step = int(input())

# Generate the sequence using np.arange()
sequence = np.arange(start, stop, step)
# Print the generated sequence
print(sequence)

#3.2.4. Numpy: Arithmetic and Statistical Operations, Mathematical Operations, Bitwise Operators
import numpy as np

def array_operations(A, B):

	# Convert A and B to NumPy arrays
	A=np.array(A)
	B=np.array(B)
	# Arithmetic Operations
	sum_result = A+B
	diff_result = A-B
	prod_result = A*B

	# Statistical Operations
	mean_A = np.mean(A)
	median_A = np.median(A)
	std_dev_A = np.std(A)

	# Bitwise Operations
	and_result = np.bitwise_and(A,B)
	or_result = np.bitwise_or(A,B)
	xor_result = np.bitwise_xor(A,B)

    # Output results with one space between each element
	print("Element-wise Sum:", ' '.join(map(str, sum_result)))
	print("Element-wise Difference:", ' '.join(map(str, diff_result)))
	print("Element-wise Product:", ' '.join(map(str, prod_result)))
    
	print(f"Mean of A: {mean_A}")
	print(f"Median of A: {median_A}")
	print(f"Standard Deviation of A: {std_dev_A}")
    
	print("Bitwise AND:", ' '.join(map(str, and_result)))
	print("Bitwise OR:", ' '.join(map(str, or_result)))
	print("Bitwise XOR:", ' '.join(map(str, xor_result)))

A = list(map(int, input().split()))  # Elements of array A
B = list(map(int, input().split()))  # Elements of array B
array_operations(A, B)


#3.2.5. Numpy: Copying and Viewing Arraysimport numpy as np

inputlist = list(map(int,input().split(" ")))

# Original array
original_array = np.array(inputlist)

# Create a view
view_array =original_array.view()

# Create a copy
copy_array =original_array.copy()

# Modify the view
view_array[0] = 99
print("Original array after modifying view:", original_array)
print("View array:", view_array)

# Modify the copy
copy_array[1] = 88
print("Original array after modifying copy:", original_array)
print("Copy array:", copy_array)


#3.2.6. Numpy: Searching, Sorting, Counting, Broadcasting   
import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
search_result = np.where(array1 == search_value)
print(search_result[0])
# Count occurrences in array1
count_result=np.count_nonzero(array1 == count_value)
print(count_result)
# Broadcasting addition
broadcast_result = array1+broadcast_value
print(broadcast_result)
# Sort the first array
sorted_array1 = np.sort(array1)
print(sorted_array1)


#3.2.7. Student Data Analysis and Operations

import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)

# 1. Print all student details
print("All student Details:\n",a)

# 2. print total students

print("Total Students:", len(a))

# # 3. Print all student Roll numbers
print("All Student Roll Nos", a[:,0] )

# # 4. Print subject 1 marks
print("Subject 1 Marks", a[:,1])

# # 5. print minimum marks of Subject 2
print("Min marks in Subject 2", a[:,2].min()     )

# # 6. print maximum marks of Subject 3
print("Max marks in Subject 3", a[:,3].max()    )

# # 7. Print All subject marks
a1 = np.delete(a,0,1)
print("All subject marks:", a1      )

# # 8. print Total marks of students
print("Total Marks", a[:,1]+a[:,2]+a[:,3]       )

# # 9. print average marks of each student
a2 = np.array(a[:,1]+a[:,2]+a[:,3])
A =np.around(a2/3,1)
print(A)
# # 10. print average mass of each subject
s1 = (a[:,1]).mean()
s2 = (a[:,2]).mean()
s3 = (a[:,3]).mean()
A1 = np.array((s1,s2,s3))
print("Average Marks of each subject", A1      )

# # 11. print average marks of S1 and S2
A2 = np.array((s1,s2))
print("Average Marks of S1 and S2",    A2      )

# # 12. print average marks of S1 and S3
A3 = np.array((s1,s3))
print("Average Marks of S1 and S3",    A3            )

# # 13. print Roll number who got maximum marks in Subject 3
i = (a[:,3]).argmax()
r = a[i][0]
print("Roll no who got maximum marks in Subject 3",  r         )

# # 14. print Roll number who got minimum marks in Subject 2
I = (a[:,2]).argmin()
R = a[I][0]
print("Roll no who got minimum marks in Subject 2",  R    )
# # 15. print Roll number who got 24 marks in Subject 2
# i1 = np.argwhere(a == 24)
r1 = (a[(a[:,2])== 24 ,0]).reshape(-1,1)
print("Roll no who got 24 marks in Subject 2",     r1            )

# # 16. print count of students who got marks in Subject 1 < 40
count = np.argwhere(a[:,1]<40)
c = len(count)
print("Count of students who got marks in Subject 1 < 40",         c      )

# # 17. print count of students who got marks in Subject 2 > 90
count1 = np.argwhere(a[:,2]>90)
c1 = len(count1)
print("Count of students who got marks in Subject 2 > 90:",        c1      )

# # 18. print count of students in each subject who got marks >= 90
Count = [len(np.argwhere(a[:,1]>=90)),len(np.argwhere(a[:,2]>=90)),len(np.argwhere(a[:,3]>=90))]
Count = np.array(Count)
print("Count of students in each subject who got marks >= 90:",    Count          )

# # 19. print count of subjects in which each student got marks >= 90

print("Roll no:",  a[:,0]    )

count0 = []
# for i in a[:,0]:
# 	val = 0
# 	index = int(np.argwhere(a[:,0]==i))
# 	if a[index][1] >= 90:
# 		val = val + 1
# 	elif a[index][2] >= 90:
# 		val = val + 1
# 	elif a[index][3] >= 90:
# 		val = val +1
# 	count0.append(val)
# count0 = np.array(count0)
for i in range(len(a[:,0])):
	val = 0
	if a[i][1]>=90:
		val = val + 1
	elif a[i][2]>=90:
		val = val + 1
	elif a[i][3]>=90:
		val = val + 1
	count0.append(val)
count0 = np.array(count0)

print("Count of subjects in which student got marks >= 90:",    count0   )

# # 20. Print S1 marks in ascending order

asc = np.sort(a[:,1])
print(asc)


# # 21. Print S1 marks >= 50 and <= 90
print(a[a[:,1]>=50])
print(a[a[:,1]<=90])


# # 22. Print the index position of marks 79
print(np.where(a[:,1]==79))
