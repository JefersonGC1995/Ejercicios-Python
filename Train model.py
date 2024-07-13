import pandas as pd
from sklearn.model_selection import train_test_split

# Cargar el DataFrame desde un archivo CSV
df = pd.read_csv('datos_limpios_titanic.csv')

# Imprimir información del DataFrame (opcional)
print(df.info())

# Importar clases necesarias de scikit-learn
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Separar las características (X) y la variable objetivo (y)
x = df.drop('Survived', axis=1)  # datos del pasajero
y = df['Survived']  # variable objetivo

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
print('datos de entrenamiento x_train', x_train)
print('datos de entrenamiento x_test', x_test)
print('datos de entrenamiento y_train', y_train.size)
print('datos de entrenamiento y_test', y_test.size)

#Estandarizacion de valores, creando el escalador 

sc = StandardScaler()
x_train =sc.fit_transform(x_train)
x_test =sc.transform(x_test)

#Construimos el modelo y entrenando el modelo con tres vecinos cercanos

classifier = KNeighborsClassifier(n_neighbors= 3)
classifier.fit(x_train, y_train)

y_pred =classifier.predict(x_test)

print(y_pred)

percent = accuracy_score (y_test, y_pred)

print ((f"porcentaje de acierto: (percent = 100)"))

print(confusion_matrix(y_test, y_pred))