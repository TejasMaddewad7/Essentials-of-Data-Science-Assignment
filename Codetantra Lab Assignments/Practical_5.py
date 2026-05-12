#5.1.1. Stacked Plot
import matplotlib.pyplot as plt
import pandas as pd

# Data for Months and Temperature for three cities
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'City_A_Temperature': [5, 7, 10, 13, 17, 20, 22, 21, 18, 12, 8, 6],
    'City_B_Temperature': [2, 3, 5, 6, 10, 14, 16, 17, 12, 9, 5, 3],
    'City_C_Temperature': [3, 4, 6, 8, 9, 12, 15, 14, 10, 7, 4, 2]
}

# Write your code...
df=pd.DataFrame(data)
plt.stackplot(df['Month'],df['City_A_Temperature'],df['City_B_Temperature'],df['City_C_Temperature'])
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Temperature Variation')
plt.show()


#5.2.1. Titanic Dataset
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset from the CSV file
df = pd.read_csv('titanic.csv')

# Set up the figure for 5 subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 12))

# Plot 1: Bar plot of Pclass
pclass_counts = df['Pclass'].value_counts()
axes[0, 0].bar(pclass_counts.index, pclass_counts.values, color='skyblue')
axes[0, 0].set_title('Passenger Class Distribution')
axes[0, 0].set_xlabel('Pclass')
axes[0, 0].set_ylabel('Count')

# Plot 2: Pie chart for Gender distribution
gender_counts = df['Gender'].value_counts()
axes[0, 1].pie(
    gender_counts,
    labels=gender_counts.index,
    autopct='%1.1f%%',
    colors=['lightblue', 'lightcoral']
)
axes[0, 1].set_title('Gender Distribution')

# Plot 3: Histogram for Age distribution
axes[1, 0].hist(df['Age'], bins=8, color='lightgreen', edgecolor='black')
axes[1, 0].set_title('Age Distribution')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Frequency')

# Plot 4: Countplot for Survived
survival_counts = df['Survived'].value_counts()
axes[1, 1].bar(
    survival_counts.index,
    survival_counts.values,
    color=['lightblue', 'lightcoral']
)
axes[1, 1].set_title('Survival Count')
axes[1, 1].set_xlabel('Survived (0 = No, 1 = Yes)')
axes[1, 1].set_ylabel('Count')

# Plot 5: Scatter plot for Fare vs Age
axes[2, 0].scatter(df['Age'], df['Fare'], color='orange')
axes[2, 0].set_title('Fare vs Age')
axes[2, 0].set_xlabel('Age')
axes[2, 0].set_ylabel('Fare')

# Adjust layout to avoid overlap
plt.tight_layout()

# Show plots
plt.show()

#5.2.2. Histogram of passenger information of Titanic
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Histogram
plt.hist(data['Age'], bins=30, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

#5.2.3. Bar plot of survival rate of passengers
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Bar Plot for Survival Rate
survival_counts = data['Survived'].value_counts()
survival_counts.plot(kind='bar')
plt.title('Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()


#5.2.4. Bar Plot for Survival by Gender
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)
# Write your code here for Bar Plot for Survival by Gender
# Group the data by 'Sex' and 'Survived', count occurrences, then unstack
survival_counts = data.groupby(['Sex', 'Survived']).size().unstack()

# Plot as a stacked bar chart
survival_counts.plot(kind='bar', stacked=True)

# Add title and labels
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')

# Customize the legend (0 = Not Survived, 1 = Survived)
plt.legend(['Not Survived', 'Survived'])

# Adjust x-axis ticks to show readable names if needed
plt.xticks(ticks=[0, 1], labels=['0', '1'], rotation=90)

plt.show()


#5.2.5. Bar Plot for Survival by Pclass
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)
# Write your code here for Bar Plot for Survival by Pclass
# Write your code here for Bar Plot for Survival by Pclass

# 1. Group the data by 'Pclass' and count survival statuses using value_counts()
survival_counts = data.groupby('Pclass')['Survived'].value_counts().unstack()

# 2. Use a stacked bar chart to display the survival counts
survival_counts.plot(kind='bar', stacked=True)

# 3. Add the title "Survival by Pclass"
plt.title('Survival by Pclass')

# 4. Label the x-axis as 'Pclass' and the y-axis as 'Count'
plt.xlabel('Pclass')
plt.ylabel('Count')

# 5. The legend should indicate 'Not Survived' and 'Survived'
plt.legend(['Not Survived', 'Survived'])

# Display the plot
plt.show()


#5.2.6. Bar Plot for Survival by Embarked
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

survival_embarked = data.groupby('Embarked_Q')['Survived'].value_counts().unstack()
survival_embarked.plot(kind='bar',stacked=True)
plt.title('Survival by Embarked')
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.legend(['Not Survived','Survived'])
plt.show()


#5.2.7. Box plot for Age Distribution
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Box Plot for Age by Pclass
# Write your code here for Box Plot for Age by Pclass
import matplotlib.pyplot as plt

# Create the boxplot using pandas.boxplot()
data.boxplot(column='Age', by='Pclass')

# Set the title and labels as specified
plt.title('Age by Pclass')
plt.suptitle('')  # Remove the default subtitle
plt.xlabel('Pclass')
plt.ylabel('Age')

# Display the plot
plt.show()


#5.2.8. Box Plot for Age by Survived
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Box Plot for Age by Survived
# Write your code here for Box Plot for Age by Survived

# 1. Use the Survived column to group data, 4. Label x and y axis
data.boxplot(column='Age', by='Survived')

# 2. Set the title of the plot
plt.title('Age by Survival')

# 3. Remove the default subtitle
plt.suptitle('')

# 4. Label the x-axis and y-axis
plt.xlabel('Survived')
plt.ylabel('Age')

plt.show()


#5.2.9. Box Plot for Fare by Pclass
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Box Plot for Fare by Pclass
# Write your code here for Box Plot for Fare by Pclass

# Create the boxplot grouped by Pclass
data.boxplot(column='Fare', by='Pclass')

# Set the title and labels
plt.title('Fare by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Fare')

# Remove the default subtitle
plt.suptitle('')

# Display the plot
plt.show()


#5.2.10. Scatter Plot for Age vs. Fare
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Box Plot for Fare by Pclass
# Write your code here for Scatter Plot for Age vs. Fare
plt.scatter(data['Age'], data['Fare'])
plt.title('Age vs. Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()


#5.2.11. Scatter Plot for Age vs. Fare by Survived

import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)
# Write your code here for Scatter Plot for Age vs. Fare by Survived

plt.figure()
colors = {0: 'red', 1:'blue'}
plt.scatter(data['Age'],data['Fare'],
c=data['Survived'].apply(lambda x: colors[x]))
plt.title('Age vs. Fare by Survival')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()