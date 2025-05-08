import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic.csv")
print(df.head())
print(df.info)
print(df.describe())
print(df.columns)
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].median())
if 'Embarked' in df.columns:
    df['Embarked'].fillna(df['Embarked'].mode()[0])
else:
    print("Warning: 'Embarked' column not found. Skipping this step.")
if 'Cabin' in df. columns:
    df.drop('Cabin', axis=1, inplace= True)

df.drop_duplicates(inplace=True)

Survial_rate = df['Survived'].mean() * 100 if 'Survived' in df.columns else 'N/A'
print(Survial_rate)

if 'Sex' in df. columns and 'Survived' in df.columns:
    survival_gender = df.groupby('Sex')['Survived'].mean()
    print(survival_gender)

if 'Pclass' and 'Survived' in df.columns:
    Survived_pclass = df.groupby('Pclass')['Survived'].mean()
    print(Survived_pclass)

if 'Sex' in df.columns and 'Survived' in df.columns:
    sns.barplot(x='Sex', y='Survived', data=df)
    plt.title('Survival Rate by Gender')
    plt.show()

if 'Pclass' in df.columns and 'Survived' in df.columns:
    sns.barplot(x='Pclass', y='Survived', data=df)
    plt.title('Survival Rate by Passenger Class')
    plt.show()

# Age Distribution
if 'Age' in df.columns:
    sns.histplot(df['Age'], bins=30, kde=True)
    plt.title('Age Distribution of Passengers')
    plt.show()

