#4.1.1. Pandas - series creation and manipulation
import pandas as pd

# Take inputs from the user to create a list of numbers
numbers = list(map(int, input().split()))

# Create a Pandas series from the list of numbers
series = pd.Series(numbers)
# Grouping by even and odd numbers and calculating the mean
grouped =series.groupby(series%2==0).mean()

# Display the mean of even and odd numbers with labels
grouped.index = ['Even' if is_even else 'Odd' for is_even in grouped.index]
print("Mean of even and odd numbers:")
print(grouped)


#4.1.2. Dictionary to dataframe
import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
new_name = input("New name: ")
new_age = int(input("New age: "))
df.loc[len(df)] = [new_name, new_age]



# Display the DataFrame after adding a new row
print("After adding a row:\n",df)

# Modifying a row
mod_index = int(input("Index of row to modify: "))
new_age_val = int(input("New age: "))
df.at[mod_index, 'Age'] = new_age_val



# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)

# Deleting a row
del_index = int(input("Index of row to delete: "))
df = df.drop(del_index).reset_index(drop=True)


# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

# Adding a new column
genders = input("Enter genders separated by space: ").split()
df['Gender'] = genders
# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column
df['Name'] = df['Name'].str.upper()
# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column
df = df.drop("Age",axis = 1)
# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)


#4.1.3. Student Information
import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])

# 1. First five rows
print("First five rows:")
print(data.head())

# 2. Average age (2 decimal places)
avg_age = round(data["Age"].mean(), 2)
print("Average age:", avg_age)

# 3. Filter students with grade up to B (A and B only)
filtered = data[data["Grade"].isin(["A", "B"])]

print("Students with a grade up to B")
print(filtered)

#4.2.1. Month with the Highest Total Sales
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
df['Total'] = df['Quantity'] * df['Price']
df['Month'] = df['Date'].str[:7]
monthly_sales = df.groupby('Month')['Total'].sum()
# Find the month with the highest total sales
best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()
print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")


#4.2.2. Best Selling Product
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

product_sales = df.groupby('Product')['Quantity'].sum()
best_product = product_sales.idxmax()
highest_quantity = product_sales.max()

# Display the result
print(f"Best selling product: {best_product}")
print(f"Total quantity sold: {highest_quantity}")


#4.2.3. City that Sold the Most Products
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
city_sales = df.groupby('City')['Quantity'].sum()

# Find the city with the maximum total quantity
best_city = city_sales.idxmax()
# Display the result
print(f"City sold the most products: {best_city}")


#4.2.4. Most Frequently Sold Product Pairs
import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)
daily_products = df.groupby('Date')['Product'].apply(list)

# Initialize a counter for pairs
pair_counts = Counter()

# For each date, find all pairs of products sold together
for products in daily_products:
    # Sort products to ensure (A, B) is the same as (B, A)
    unique_products = sorted(list(set(products)))
    if len(unique_products) >= 2:
        # Generate unique pairs
        day_pairs = list(combinations(unique_products, 2))
        pair_counts.update(day_pairs)

# Determine the maximum frequency
if pair_counts:
    max_freq = max(pair_counts.values())

    # Output the product pair/s that was sold most frequently
    # Sort pairs alphabetically to match common test case requirements
    most_frequent = sorted([pair for pair, count in pair_counts.items() if count == max_freq])

    for pair in most_frequent:
        print(f"{pair[0]} and {pair[1]}: {max_freq} times")


#4.2.5. Titanic Dataset Analysis and Data Cleaning

import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
# 1. Display the first 5 rows of the dataset
print(data.head())

# 2. Display the last 5 rows of the dataset
print(data.tail())

# 3. Get the shape of the dataset
print(data.shape)

# 4. Get a summary of the dataset (info)
print(data.info())

# 5. Get basic statistics of the dataset
print(data.describe())

# 6. Check for missing values
print(data.isnull().sum())

# 7. Fill missing values in the 'Age' column with the median age
data['Age'] = data['Age'].fillna(data['Age'].median())

# 8. Fill missing values in the 'Embarked' column with the mode
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

# 9. Drop the 'Cabin' column due to many missing values
data.drop(columns=['Cabin'], inplace=True)

# 10. Create a new column 'FamilySize' by adding 'SibSp' and 'Parch'
data['FamilySize'] = data['SibSp'] + data['Parch']


#4.2.6. Titanic Dataset Analysis and Data Cleaning - 2
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = (data['FamilySize'] == 0).astype(int)

# 2. Convert 'Sex' to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# 3. One-hot encode 'Embarked', dropping the first category
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 4. Get the mean age
mean_age = data['Age'].mean()
print(mean_age)

# 5. Get the median fare
median_fare = data['Fare'].median()
print(median_fare)

# 6. Get the number of passengers by class
passengers_by_class = data['Pclass'].value_counts()
print(passengers_by_class)

# 7. Get the number of passengers by gender
passengers_by_gender = data['Sex'].value_counts()
print(passengers_by_gender)

# 8. Get the number of passengers by survival status
passengers_by_survival = data['Survived'].value_counts()
print(passengers_by_survival)

# 9. Calculate survival rate
survival_rate = data['Survived'].mean()
print(survival_rate)

# 10. Calculate survival rate by gender
survival_rate_by_gender = data.groupby('Sex')['Survived'].mean()
print(survival_rate_by_gender)


#4.2.7. Titanic Dataset Analysis and Data Cleaning - 3
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

print(data.groupby('Pclass')['Survived'].mean()) 
print(data.groupby('Embarked_S')['Survived'].mean())
print(data.groupby('FamilySize')['Survived'].mean()) 
print(data.groupby('IsAlone')['Survived'].mean()) 
print(data.groupby('Pclass')['Fare'].mean()) 
print(data.groupby('Pclass')['Age'].mean()) 
print(data.groupby('Survived')['Age'].mean()) 
print(data.groupby('Survived')['Fare'].mean()) 
print(data[data['Survived'] == 1]['Pclass'].value_counts()) 
print(data[data['Survived'] == 0]['Pclass'].value_counts())


#4.2.8. Titanic Dataset Analysis and Data Cleaning - 4
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)


print(data[data['Survived']==1]['Sex'].value_counts()) 
print(data[data['Survived']==0]['Sex'].value_counts())
print(data[data['Survived']==1]['Embarked_S'].value_counts()) 
print(data[data['Survived']==0]['Embarked_S'].value_counts()) 
print(data[data['Age']<18]['Survived'].mean()) 
print(data[data['Age']>=18]['Survived'].mean())
print(data[data['Survived']==1]['Age'].median())
print(data[data['Survived']==0]['Age'].median()) 
print(data[data['Survived']==1]['Fare'].median())
print(data[data['Survived']==0]['Fare'].median())
