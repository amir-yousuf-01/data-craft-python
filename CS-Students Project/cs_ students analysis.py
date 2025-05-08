
import pandas as pd

df = pd.read_csv("cs_students.csv")
print(df)
print(df.info)
print(df.describe())
df. columns =["Student_ID", "Name", "Gender", "Age", "GPA", "Major",
    "Interested_Domain", "Projects", "Future_Career", "Python", "SQL", "Java"]
print(df)
df = df.iloc[1:].reset_index(drop=True)
print(df)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["GPA"] = pd.to_numeric(df["GPA"], errors="coerce")
num_students = len(df)
print(f"Total number of students: {num_students}")
unique_majors = df["Major"].unique()
print(f"Unique majors: {unique_majors}")
average_age = df["Age"].mean()
print(f"Average age of students: {average_age:.2f}")
highest_gpa = df["GPA"].max()
lowest_gpa = df["GPA"].min()
print(f"Highest GPA: {highest_gpa}")
print(f"Lowest GPA: {lowest_gpa}")
data_science_students = df[df["Interested_Domain"] == "Data Science"].shape[0]
print(f"Number of students interested in Data Science: {data_science_students}")
strong_python_students = df[df["Python"] == "Strong"].shape[0]
print(f"Number of students with Strong Python skills: {strong_python_students}")
avg_gpa_by_career = df.groupby("Future_Career")["GPA"].mean()
print("Average GPA by Future Career:")
print(avg_gpa_by_career)
gender_count = df["Gender"].value_counts()
print("Gender distribution:")
print(gender_count)