import pandas as pd

##Escribir una funcion que reciba un diccioario con las notas de los estudiantes del curso y devuelve una serie con minimo, maximo, media, desviacion tipica

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index = ['Min', 'Max', 'Media', 'Desviacion estandar'])
    return estadisticas

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 6].sort_values(ascending = False)

notas = {'Juan': 9, 'Juanita': 5, 'Pedro': 5.9, 'Fabian': 8.5, 'Maxi': 7.5, 'Sandra': 9.8, 'Rosario': 9}

print(aprobados(notas))
print(estadistica_notas(notas))