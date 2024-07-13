import pandas as pd
df= pd.read_csv('titanic.csv')
print (df)

print (df.head())

print (df.groupby('Sex')['Survived'].mean()) 

print(df.pivot_table(index='Survived', columns='Pclass', values='Age', aggfunc='mean'))

df = df.drop('PassengerId', axis= 1)
df = df.drop('Name', axis= 1)
df = df.drop('Cabin', axis= 1)
df = df.drop('Ticket', axis= 1)

print (df.info())
print (df)

print (df.groupby('Embarked').value_counts())

#print(df['Embarked'].value_counts())

df['Embarked'].fillna('S', inplace = True)

print(df['Embarked'].value_counts())
df.info()

age_1 =df[df['Pclass'] == 1] ['Age'].median()
age_2 =df[df['Pclass'] == 2] ['Age'].median()
age_3 =df[df['Pclass'] == 3] ['Age'].median()

print(age_1)
print(age_2)
print(age_3)

def fill_age (row):
    if pd.isnull(row['Age'])== True:
        if row['Pclass'] == 1:
            return(age_1)
        elif row['Pclass'] ==2:
            return(age_2)
        elif row['Pclass'] ==3:
            return(age_3)
    return(row['Age'])
        
df['Age'] = df.apply(fill_age, axis=1)
print(df.info())

df['Sex'].replace({'male': 0, 'female': 1}, inplace=True)

df.info()
#print(pd.get_dummies(df['Embarked']))
df[list(pd.get_dummies(df['Embarked']).columns)]=pd.get_dummies(df['Embarked'], dtype=int)

df.drop(['Embarked'], axis=1, inplace=True)
print(df)

def is_alone(row):
    if row['SibSp'] + row['Parch'] ==0:
        return 1
    return 0

df['Alone'] = df.apply(is_alone, axis=1)

df.drop(['SibSp', 'Parch'], axis=1, inplace=True)


print(df.pivot_table(values= 'Age', columns= 'Alone' ,
                     index= 'Survived', aggfunc= 'count'))

df.to_csv('datos_limpios_titanic.csv', index=False)
