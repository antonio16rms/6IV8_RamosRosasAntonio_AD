import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./ElementosBasicosEstadistica/housing.csv')


#Mostrar las primeras 5 filas
print(df.head())

#Mostrar las ultimas 5 filas
print(df.tail())

#Mostrar una fila especifica
print(df.iloc[7])

#Mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#Obtener la media de la columna total_rooms
mediadecuartos=df["total_rooms"].mean()
print('La media de cuartos por casa es: ' + str(mediadecuartos))


#Mediana
medianadecuartos=df['median_house_value'].median()
print('La mediana de valor de casa es: ' + str(medianadecuartos))

#Sumatoria 
salario_total=df['population'].sum()
print('La suma de salarios es: ' + str(salario_total))

#Filtrar
filtro=df[df['ocean_proximity'] == 'ISLAND']
print(filtro)

#Grafico de dispercion
plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])

plt.xlabel("Proximidad")
plt.ylabel("Precio")

plt.title("Grafico de dipercion Proximidad vs Precio")
plt.show()