import pandas as pd

data = pd.read_csv('Employee_Dataset.csv')


print(data.head())

# basic statistics on numeric columns
print("\Basic Statistics:")
print(data.describe())


# Count of employee by gender
gender_counts = data['Gender'].value_counts()
print("\nGender Distribution:")
print(gender_counts)


# Average salary by department
avg_salary_by_department = data.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(avg_salary_by_department)


#Calaculate the highest and lowset salaries
highest_salary = data['Salary'].max()
lowest_salary = data['Salary'].min()
print("Highest Salary", highest_salary)
print("Lowest Salary", lowest_salary)


#Calculate the average salary of male and female employee
avg_salary_by_gender = data.groupby('Gender')['Salary'].mean()
print("\nAvearage Salary by Gender")
print(avg_salary_by_gender)


#Total salary expenditure
total_salary_expenditure=data['Salary'].sum()
print("\nTotal Salary Expenditure", total_salary_expenditure)



# calcualte the numbe employyee in each departement
dept_employee_counts = data['Department'].value_counts()
print("\nNumber of Employee in Each Department:")
print(dept_employee_counts)



# Analyze employee age distribution by department
age_distribution_by_dept = data.groupby('Department')['Age'].describe()
print("\nDistribution by Department", age_distribution_by_dept)




import matplotlib.pyplot as plt
import seaborn as sns




# Set style for Seaborn plots
sns.set(style="whitegrid")

# Gender Distribution Bar Plot
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=data)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()



# Age Distribution Histogram
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=10, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()



# Salary Distribution by Gender Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Salary', data=data)
plt.title('Salary Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.show()



# Salary Distribution by Department Violin Plot
plt.figure(figsize=(12, 8))
sns.violinplot(x='Department', y='Salary', data=data)
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.show()



# Correlation Heatmap
corr_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

