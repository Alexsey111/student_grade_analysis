import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Имя': ['Александр', 'Мария', 'Дмитрий', 'Анна', 'Иван', 'Екатерина', 'Сергей', 'Елена', 'Михаил', 'Ольга'],
    'Математика': [5, 4, 3, 5, 4, 3, 4, 5, 4, 3],
    'Физика': [4, 5, 3, 4, 5, 3, 4, 4, 5, 4],
    'Химия': [3, 4, 5, 3, 4, 5, 3, 4, 4, 5],
    'Литература': [5, 4, 4, 5, 3, 4, 5, 4, 4, 3],
    'История': [4, 3, 5, 4, 5, 3, 4, 5, 3, 4]
}

df = pd.DataFrame(data)

print(df.head(2))

average_grades = {}
median_grades = {}

for subject in ['Математика', 'Физика', 'Химия', 'Литература', 'История']:
    average_grades[subject] = round(df[subject].mean(), 2)
    median_grades[subject] = round(df[subject].median(), 2)

print("\nСредние оценки по предметам:")
for subject, avg in average_grades.items():
    print(f'Средняя оценка по предмету {subject}: {avg}')

print("\nМедианные оценки по предметам:")
for subject, med in average_grades.items():
    print(f'Медианная оценка по предмету {subject}: {med}')

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR = Q3_math - Q1_math
print(f'\nQ1_math = {Q1_math}')
print(f'Q3_math = {Q3_math}')
print(f'IQR = {IQR}')

df.boxplot(column='Математика')
plt.show()