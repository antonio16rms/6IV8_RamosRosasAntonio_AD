import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Ejercicios/housing.csv')

columnas = ["longitude", "latitude", "housing_median_age", "total_rooms", 
            "total_bedrooms", "population", "households", "median_income", "median_house_value"]

print("\nAnálisis Estadístico:")
for columna in columnas:
    print(f"\n{columna}:")
    print("Media:", df[columna].mean())
    print("Mediana:", df[columna].median())
    moda = df[columna].mode()
    print("Moda:", moda[0] if not moda.empty else "No hay moda")
    print("Rango:", df[columna].max() - df[columna].min())
    print("Varianza:", df[columna].var())
    print("Desviación estándar:", df[columna].std())

print("\nTablas de Frecuencias:")
for columna in columnas:
    print(f"\nTabla de Frecuencia - {columna}")
    print(df[columna].value_counts(dropna=False))

plt.figure(figsize=(10, 5))
plt.hist(df["median_house_value"], bins=30, color='blue', alpha=0.5, label="Valor Medio")
plt.hist(df["total_bedrooms"], bins=30, color='red', alpha=0.5, label="Total Dormitorios")
plt.hist(df["population"], bins=30, color='green', alpha=0.5, label="Población")

plt.axvline(df["median_house_value"].mean(), color='black', linestyle='dashed', linewidth=2, label="Promedio Valor Medio")

plt.legend()
plt.title("Histograma Comparativo")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
