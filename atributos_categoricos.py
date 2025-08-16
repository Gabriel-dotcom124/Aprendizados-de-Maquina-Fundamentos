Definição
  
  Atributos categóricos são aqueles que apresentam valores discretos numéricos (int float, etc.) ou não (strings) para representar categorias. Como os modelos trabalham (em sua grande maioria) apenas com valores numéricos, os atributos com valores do tipo strings precisam passar por um processo de codificação ou conversão para valores numéricos. • Exemplos: sexo, perguntas de sim/não, cidade/estado/país etc.


%%writefile exam.csv
ethnicity,parental_education,lunch,preparation_course,math,reading,writing,gender
group B,bachelor's degree,standard,none,0.72,0.72,0.74,F
group C,some college,standard,completed,0.69,0.9,0.88,F
group B,master's degree,standard,none,0.9,0.95,0.93,F
group A,associate's degree,free/reduced,none,0.47,0.57,0.44,M
group C,some college,standard,none,0.76,0.78,0.75,M
group B,associate's degree,standard,none,0.71,0.83,0.78,F
group B,some college,standard,completed,0.88,0.95,0.92,F
group B,some college,free/reduced,none,0.4,0.43,0.39,M
group D,high school,free/reduced,completed,0.64,0.64,0.67,M
group B,high school,free/reduced,none,0.38,0.6,0.5,F



import pandas as pd


data = pd.read_csv('exam.csv')
data.head()


Nominal


data[['ethnicity', 'lunch', 'gender']].head()


data['gender_m'] = data['gender'].apply(lambda gender: 1 if gender == "M" else 0)
data['gender_F'] = data['gender'].apply(lambda gender: 1 if gender == "F" else 0)

data.head()


Ordinal

    Atributos categóricos ordinais são aqueles em que os valores apresentam relação de ordem.


data[['parental_education', 'preparation_course']].head()

data['parental_education'].drop_duplicates()

parental_education_mapper = {
    "master's degree": 6,
    "bachelor's degree": 5,
    "associate's degree": 4,
    "some college": 3,
    "high school": 2,
    "some high school": 1,
}

data['parental_education_encoded'] = data['parental_education'].apply( lambda level: parental_education_mapper[level] )

data.head()


