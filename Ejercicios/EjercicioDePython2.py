import pandas as pd
import matplotlib.pyplot as plt
ventas_df = pd.read_excel('C:/Users/LENOVO/6IV8_RamosRosasAntonio_AD/Ejercicios/proyecto1.xlsx', engine='openpyxl')  
sucursales_df = pd.read_excel('C:/Users/LENOVO/6IV8_RamosRosasAntonio_AD/Ejercicios/Catalogo_sucursal.xlsx',engine='openpyxl')  
# Ventas totales del comercio
ventas_totales = ventas_df['ventas_tot'].sum()
print(f"Ventas totales del comercio: {ventas_totales}")
# Socios con y sin adeudo
socios_con_adeudo = ventas_df[ventas_df['adeudo_actual'] > 0].shape[0]
socios_sin_adeudo = ventas_df[ventas_df['adeudo_actual'] == 0].shape[0]
total_socios = socios_con_adeudo + socios_sin_adeudo
porcentaje_con_adeudo = (socios_con_adeudo / total_socios) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / total_socios) * 100
print(f"Socios con adeudo: {socios_con_adeudo} ({porcentaje_con_adeudo:.2f}%)")
print(f"Socios sin adeudo: {socios_sin_adeudo} ({porcentaje_sin_adeudo:.2f}%)")
# Gráfica de barras: Ventas totales respecto del tiempo
ventas_df.groupby('fec_ini_cdto')['ventas_tot'].sum().plot(kind='bar', title='Ventas Totales vs Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Ventas Totales')
plt.show()
# Gráfica de desviación estándar de pagos respecto del tiempo
ventas_df.groupby('fec_ini_cdto')['pagos_tot'].std().plot(kind='bar', title='Desviación Estándar de Pagos vs Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Desviación Estándar')
plt.show()
# Deuda total de los clientes
deuda_total = ventas_df['adeudo_actual'].sum()
print(f"Deuda total de los clientes: {deuda_total}")
# Porcentaje de utilidad del comercio
utilidad_total = ventas_totales - deuda_total
porcentaje_utilidad = (utilidad_total / ventas_totales) * 100
print(f"Porcentaje de utilidad del comercio: {porcentaje_utilidad:.2f}%")
# Gráfico circular de ventas por sucursal
ventas_por_sucursal = ventas_df.groupby('id_sucursal')['ventas_tot'].sum()
ventas_por_sucursal.plot(kind='pie', autopct='%1.1f%%', title='Ventas por Sucursal')
plt.ylabel('')
plt.show()
# Gráfico de deudas totales por sucursal respecto del margen de utilidad
deudas_por_sucursal = ventas_df.groupby('id_sucursal')['adeudo_actual'].sum()
utilidad_por_sucursal = ventas_por_sucursal - deudas_por_sucursal
fig, ax = plt.subplots()
ax.bar(deudas_por_sucursal.index, deudas_por_sucursal, label='Deudas Totales')
ax.bar(utilidad_por_sucursal.index, utilidad_por_sucursal, bottom=deudas_por_sucursal, label='Utilidad')
ax.set_title('Deudas Totales y margen de Utilidad por Sucursal')
ax.set_xlabel('Sucursal')
ax.set_ylabel('Monto')
ax.legend()
plt.show()