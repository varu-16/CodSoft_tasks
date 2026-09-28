
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style("whitegrid")



# Load the Cleaned Dataset


df = pd.read_csv("cleaned_Maths.csv")

print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())



# BAR CHART
# Average Final Grade by School


school_grade = df.groupby('school')['G3'].mean()

plt.figure(figsize=(8, 5))

bars = plt.bar(
    school_grade.index,
    school_grade.values,
    color=['steelblue', 'orange']
)

plt.title("Average Final Grade by School", fontsize=16)
plt.xlabel("School", fontsize=12)
plt.ylabel("Average Final Grade (G3)", fontsize=12)

# Display values on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f'{height:.2f}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()



# LINE CHART
# Average G1, G2 and G3


average_grades = df[['G1', 'G2', 'G3']].mean()

plt.figure(figsize=(8, 5))

plt.plot(
    average_grades.index,
    average_grades.values,
    marker='o',
    linewidth=2,
    color='royalblue',
    label='Average Marks'
)

plt.title("Average Student Grades: G1, G2 and G3", fontsize=16)
plt.xlabel("Grade Period", fontsize=12)
plt.ylabel("Average Marks", fontsize=12)

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()



# PIE CHART
# Gender Distribution


gender_counts = df['sex'].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    gender_counts.values,
    labels=gender_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightblue', 'lightpink']
)

plt.title("Gender Distribution", fontsize=16)

plt.tight_layout()
plt.show()



# HISTOGRAM
# Distribution of Final Grades


plt.figure(figsize=(8, 5))

plt.hist(
    df['G3'],
    bins=10,
    color='skyblue',
    edgecolor='black'
)

plt.title("Distribution of Final Grades", fontsize=16)
plt.xlabel("Final Grade (G3)", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)

plt.tight_layout()
plt.show()



# SCATTER PLOT
# Absences vs Final Grade


plt.figure(figsize=(8, 5))

plt.scatter(
    df['absences'],
    df['G3'],
    color='purple',
    alpha=0.6
)

plt.title("Absences vs Final Grade", fontsize=16)
plt.xlabel("Number of Absences", fontsize=12)
plt.ylabel("Final Grade (G3)", fontsize=12)

plt.grid(True)

plt.tight_layout()
plt.show()



#  SCATTER PLOT
# G2 vs Final Grade


plt.figure(figsize=(8, 5))

plt.scatter(
    df['G2'],
    df['G3'],
    color='green',
    alpha=0.6
)

plt.title("G2 vs Final Grade", fontsize=16)
plt.xlabel("G2 Grade", fontsize=12)
plt.ylabel("Final Grade (G3)", fontsize=12)

plt.grid(True)

plt.tight_layout()
plt.show()



#  STUDY TIME vs FINAL GRADE


study_grade = df.groupby('studytime')['G3'].mean()

plt.figure(figsize=(8, 5))

bars = plt.bar(
    study_grade.index,
    study_grade.values,
    color='teal'
)

plt.title("Average Final Grade by Study Time", fontsize=16)
plt.xlabel("Study Time", fontsize=12)
plt.ylabel("Average Final Grade (G3)", fontsize=12)

# Display values
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f'{height:.2f}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()



#  CORRELATION HEATMAP


correlation = df[
    [
        'age',
        'studytime',
        'failures',
        'absences',
        'G1',
        'G2',
        'G3'
    ]
].corr()

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Heatmap", fontsize=16)

plt.tight_layout()
plt.show()



#  BOX PLOT
# Detect Outliers in Absences


plt.figure(figsize=(8, 5))

sns.boxplot(
    y=df['absences'],
    color='orange'
)

plt.title("Box Plot of Student Absences", fontsize=16)
plt.ylabel("Number of Absences", fontsize=12)

plt.tight_layout()
plt.show()



#  BOX PLOT
# Final Grade Distribution


plt.figure(figsize=(8, 5))

sns.boxplot(
    y=df['G3'],
    color='lightgreen'
)

plt.title("Box Plot of Final Grades", fontsize=16)
plt.ylabel("Final Grade (G3)", fontsize=12)

plt.tight_layout()
plt.show()



#  PRINT IMPORTANT STATISTICS


print("\n========================================")
print("       TASK 3 SUMMARY STATISTICS")
print("========================================")

print("\nAverage G1:", round(df['G1'].mean(), 2))
print("Average G2:", round(df['G2'].mean(), 2))
print("Average G3:", round(df['G3'].mean(), 2))

print("\nAverage Absences:", round(df['absences'].mean(), 2))

print("\nAverage Final Grade by School:")
print(school_grade.round(2))

print("\nAverage Final Grade by Study Time:")
print(study_grade.round(2))

print("\nAverage Final Grade by Gender:")
print(df.groupby('sex')['G3'].mean().round(2))

print("\nAverage Final Grade by Previous Failures:")
print(df.groupby('failures')['G3'].mean().round(2))



#  CORRELATION WITH FINAL GRADE


print("\n========================================")
print(" Correlation with Final Grade (G3)")
print("========================================")

g3_correlation = df[
    [
        'age',
        'studytime',
        'failures',
        'absences',
        'G1',
        'G2',
        'G3'
    ]
].corr()['G3'].sort_values(ascending=False)

print(g3_correlation.round(2))


