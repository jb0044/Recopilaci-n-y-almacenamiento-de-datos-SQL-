#!/usr/bin/env python
# coding: utf-8

# # Hola Jorge! <a class="tocSkip"></a>
# 
# Mi nombre es Oscar Flores y tengo el gusto de revisar tu proyecto. Si tienes algún comentario que quieras agregar en tus respuestas te puedes referir a mi como Oscar, no hay problema que me trates de tú.
# 
# Si veo un error en la primera revisión solamente lo señalaré y dejaré que tú encuentres de qué se trata y cómo arreglarlo. Debo prepararte para que te desempeñes como especialista en Data, en un trabajo real, el responsable a cargo tuyo hará lo mismo. Si aún tienes dificultades para resolver esta tarea, te daré indicaciones más precisas en una siguiente iteración.
# 
# Te dejaré mis comentarios más abajo - **por favor, no los muevas, modifiques o borres**
# 
# Comenzaré mis comentarios con un resumen de los puntos que están bien, aquellos que debes corregir y aquellos que puedes mejorar. Luego deberás revisar todo el notebook para leer mis comentarios, los cuales estarán en rectángulos de color verde, amarillo o rojo como siguen:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
#     
# Muy bien! Toda la respuesta fue lograda satisfactoriamente.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Existen detalles a mejorar. Existen recomendaciones.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Se necesitan correcciones en el bloque. El trabajo no puede ser aceptado con comentarios en rojo sin solucionar.
# </div>
# 
# Cualquier comentario que quieras agregar entre iteraciones de revisión lo puedes hacer de la siguiente manera:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta estudiante.</b> <a class="tocSkip"></a>
# </div>
# 

# ## Resumen de la revisión 1 <a class="tocSkip"></a>

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Excelente! Está casi todo correcto, tan solo falta que revises la existencia de outliers antes de realizar los tests estadísticos.
#     
# Saludos!    
# </div>

# ----

# # Introduccion

# 
# Para este proyecto se va a trabajar con unas bases de datos de la empresa Zuber, que contienen información de viajes que se llevaron a cabo en Chicago, la empresa busca saber si hay relación entre el clima y los viajes, y en base a esto tratar de crear una mejor tarifa para este tipo se escenario.
# 
# El objetivo del proyecto es analizar y limpiar los datos para poder preparar un estudio sobre los patrones de viaje de los clientes. Se deben separar los datos y ejecutar su analisís, con la info proporcionada del 2017, además de crear gráficos para hacer una representación clara de los resultados. La siguiente parte consistirá en comprobar las hipótesis para observar si hay algun factor externo que influya en los viajes de los clientes para esta zona y con lo anterior darle una mejor propuesta de servicio al cliente.
# 
# 
# 

# # Importación de librerías y carga de archivos.

# In[1]:


# Se importan las librerias que se trabajaran
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats as st
import numpy as np
import seaborn as sns


# In[2]:


#Se cargan los archivos
company_df = pd.read_csv('/datasets/project_sql_result_01.csv')
location_df = pd.read_csv('/datasets/project_sql_result_04.csv')
trip_chg = pd.read_csv('/datasets/project_sql_result_07.csv') 


# # Exploración de datos

# In[3]:


#Descripción de data frames
company_df.describe()


# In[4]:


location_df.describe()


# In[5]:


trip_chg.describe()


# In[6]:


company_df.head()


# In[7]:


location_df.head()


# In[8]:


trip_chg.head()


# In[9]:


company_df.info()


# In[10]:


location_df.info()


# In[11]:


trip_chg.info()


# En el inicio del analisís de datos de las 3 datasets presentes, se observa que los datos de las tablas se encuentran correctamente preparados, tanto en la estructura como con el tipo de datos que se necesitan para trabajar con las columnas.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Muy bien con la descripción inicial!
# </div>

# #Continuación del analisís de datos

# In[12]:


#Se comprueban valores ausentes y duplicados
company_df.isnull().sum()


# In[13]:


company_df.duplicated().sum()


# In[14]:


location_df.isnull().sum()


# In[15]:


location_df.duplicated().sum()


# In[16]:


trip_chg.isnull().sum()


# In[17]:


trip_chg.duplicated().sum()


# 1.- En esta segunda parte del analisís de datos, se observa que ninguno de los 3 dataframes tienens valores nulos
# 
# 2.- En cuanto a valores duplicados, las 2 primeras tablas no cuentan con alguno, mientras la otra tabla sí tiene, esto debido a que se pueden repetir cuando se terminan los viajes, no es recomendable eliminarlos, ya que se estaría perdiendo información necesaria para el tratamiento de datos.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Muy bien
# </div>

# # Gráfico para representar el top10 de los barrios con más viajes.

# In[18]:


#top 10 barrios
top_10_neighborhoods = location_df.groupby('dropoff_location_name')['average_trips'].mean().sort_values(ascending=False).head(10)
print(top_10_neighborhoods.head())


# In[19]:


#Gráfica de viajes que lleva a cabo cada compañia de taxis
trip_total = company_df.groupby('company_name')['trips_amount'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(15,10))
trip_total.plot(kind='bar')
plt.title('Amount of Trips by Company')
plt.xlabel('Company')
plt.ylabel('Amount of Trips')
plt.show()


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto!
# </div>

# La gráfica muestra que 'Flash cab' es la compañia que más viajes hace, seguido por 'Affiliation services' y 'Medallion', lo anterior se puede deber a que estas compañias ofrecen un buen servicio y tarifas para sus clientes.

# In[20]:


#grafico en donde se representa los barrios mas concurridos

plt.figure(figsize=(12, 6))
top_10_neighborhoods.plot(kind='barh')
plt.title('Top 10 Neighborhoods by amount of ending trips')
plt.ylabel('Neighborhood')
plt.xlabel('Number of ending trips')
plt.show()


# Loop, River north y Streeterville son los barrios en donde más terminan los viajes los clientes, debido a que en estas zonas es donde mayormente se concentra la mancha urbana, si se busca obtener mayores ganancia, es recomendable concentrarse en estas zonas urbanas.

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto!
# </div>

# In[24]:


trip_sec = trip_chg['duration_seconds']


# In[26]:


sns.boxplot (trip_sec)


# In[28]:


#Calcular quartil 3 y quartil 1
q3 = trip_sec.quantile(.75)
q1 = trip_sec.quantile(.25)
#Calcular el rango intercuartilico q3-q1
iqr = q3 - q1
#Calcular limite superior q3+(1.5*iqr)
lim_sup = q3+(1.5*iqr)
#Calcular limite inferior q1-(1.5*iqr)
lim_inf = q1-(1.5*iqr)
#Filtrar datos para conservar lo que este por debajo del limite superior y por encima del limite inferior
trip_chg = trip_chg[(trip_chg['duration_seconds'] > lim_inf)&(trip_chg['duration_seconds'] < lim_sup)]

sns.boxplot (trip_chg['duration_seconds'])


# # Prueba de hipótesis (Python)

# # Hipótesis nula = La duración promedio del viaje desde el Loop hasta el aeropuerto cambia en sábados lluviosos
# 
# # Hipotesis alternativa = La duración promedio del viaje desde el Loop hasta el aeropuerto no cambia en sábados lluviosos"

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Antes de realizar los test, revisa la existencia de outliers. Remuévelos de ser necesario.
# </div>

# In[29]:


#Valor de alpha
alpha = 0.05
#Se extraen las condiciones climatológicas de los viajes
rainy_sat = trip_chg['duration_seconds'][trip_chg["weather_conditions"] == "Bad"]
sunny_sat = trip_chg['duration_seconds'][trip_chg["weather_conditions"] == "Good"]

result_airport_levene = st.levene(rainy_sat, sunny_sat)
if (result_airport_levene.pvalue < alpha): 
    print('Se realizará la prueba t test con equalvar False según la prueba levene')
else:
    print("Se realizará la prueba t test con equalvar True según la prueba levene")


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Excelente, es mejor revisar ese parámetro con un test.
# </div>

# In[30]:


#Se calcula el tiempo promedio de los viajes por tipo de clima
rainy_mean_1 = rainy_sat.mean()
sunny_mean_2 = sunny_sat.mean()


# In[31]:


print("Promedio de los días lluviosos:", rainy_mean_1)
print("Promedio de los días soleados:", sunny_mean_2)


# In[32]:


#Se calcula la varianza de los dias lluviosos y soleados
rainy_var = np.var(rainy_sat)
sunny_var = np.var(sunny_sat)
print("Varianza de los días lluviosos:", rainy_var)
print("Varianza de los días soleados:", sunny_var)


# In[33]:


#Se realiza un t-test para poder determinar si hay diferencia
t_stat, p_value = st.ttest_ind(rainy_sat, sunny_sat, equal_var = True)


# In[35]:


if p_value < alpha:
    print("Rechazamos la hipotesis nula")
else:
    print("No podemos rechazar la hipotesis nula")


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Muy bien, correcto!
# </div>

# # Conclusiones

# - Se procedió a cargar los 3 datasets, a continuación se comenzó con el analisís de datos.
# - Una vez que se han analizado los valores nulos y duplicados de todas las tablas, se detectó que no existen valores nulos, se encontraron valores duplicados en la tabla trip_chg, los cuales se dejaron como estaban, ya que esta información es necesaria para los cálculos posteriores.
# - Se elaboraron los gráficos para identificar cuales compañias fueron las que tuvieron mayor solicitud de viajes por parte de los clientes, además de observar el top de barrios en Chicago donde se terminan los viajes.
# - En la parte del tratamiento de las hipótesis se aceptó la nula que menciona; 'La duración promedio del viaje desde el Loop hasta el aeropuerto cambia en sábados lluviosos', debido a que sí hay una diferencia entre los viajes en días soleados y lluviosos. Lo anterior significa que cuando hay un clima lluvioso la duración de los viajes obviamente será más larga, ya que implica un mayor volumén de tráfico. A los conductores de taxis les conviene más trabajar durante el clima lluvioso, debido que tienen mayores ganancias porque aumenta el tiempo de los viajes.
# 
# 

# In[ ]:




