import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Load dataset


df = pd.read_csv("cleaned_Maths.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())


#  Descriptive Statistics


print("\nDescriptive Statistics:")
print(df.describe())

print("\nImportant Statistics:")
print(df[['age', 'studytime', 'failures',
          'absences', 'G1', 'G2', 'G3']].describe())


#  Average Grades


print("\nAverage G1:", df['G1'].mean())
print("Average G2:", df['G2'].mean())
print("Average G3:", df['G3'].mean())


#  Final Grade Distribution


plt.figure(figsize=(8,5))
plt.hist(df['G3'], bins=10)
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.title("Distribution of Final Grades")
plt.show()


#  Absence Distribution


plt.figure(figsize=(8,5))
plt.hist(df['absences'], bins=15)
plt.xlabel("Absences")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Absences")
plt.show()


#  Study Time Distribution


plt.figure(figsize=(8,5))
sns.countplot(x='studytime', data=df)
plt.xlabel("Study Time")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Time")
plt.show()


#  Study Time vs Final Grade


plt.figure(figsize=(8,5))
sns.boxplot(x='studytime', y='G3', data=df)
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.title("Study Time vs Final Grade")
plt.show()


#  Absences vs Final Grade


plt.figure(figsize=(8,5))
plt.scatter(df['absences'], df['G3'])
plt.xlabel("Absences")
plt.ylabel("Final Grade")
plt.title("Absences vs Final Grade")
plt.show()


#  G1 vs G3


plt.figure(figsize=(8,5))
plt.scatter(df['G1'], df['G3'])
plt.xlabel("G1")
plt.ylabel("G3")
plt.title("G1 vs Final Grade")
plt.show()


#  Correlation


correlation = df[['age', 'studytime', 'failures',
                  'absences', 'G1', 'G2', 'G3']].corr()

print("\nCorrelation:")
print(correlation.round(2))


#  Correlation Heatmap


plt.figure(figsize=(10,7))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()


#  Outlier Detection


plt.figure(figsize=(8,5))
sns.boxplot(y=df['absences'])
plt.ylabel("Absences")
plt.title("Absence Outliers")
plt.show()


#  Average Grade by Gender


print("\nAverage G3 by Gender:")
print(df.groupby('sex')['G3'].mean().round(2))


#  Average Grade by School


print("\nAverage G3 by School:")
print(df.groupby('school')['G3'].mean().round(2))


#  Average Grade by Study Time


print("\nAverage G3 by Study Time:")
print(df.groupby('studytime')['G3'].mean().round(2))


#  Average Grade by Failures


print("\nAverage G3 by Previous Failures:")
print(df.groupby('failures')['G3'].mean().round(2))