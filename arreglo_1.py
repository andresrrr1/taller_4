import numpy as np
import matplotlib.pyplot as ptl
# a= np.array([5,10,15,25,7])
# print(a)
# b= np.array([3,4,7,9,56])
# print(b)

# c= a**2
# print(c)

""" a= np.array([5,10,15,20,25])
print(a)
b= np.array([3,4,7,9,56])
print(b)

c= a@b
print(c) """

""" a= np.array([5,10,15,20,25])
print(a)
b= np.array([3,4,7,9,56])
print(b)

b+=1
print(b) """

""" a= np.array([5,10,15,20,25])
print(a)
b= np.array([3,4,7,9,56])
print(b)

c= a/b
print(c) """
""" a= np.array([5,10,15,20,25],[3,6,4,8,12])
c=a.sum() #saca la suma todos los elementos del arreglo
b=a.min() #valor minimo de toda la matriz 
d=a.mean() # mediana de la matriz 
print(c)
print(b)
print(d) """
""" a= np.array([[5,10,15,20,25],[3,6,4,8,12]]) #primer eje 0 y segundo 1
print(a)
print(a.sum(axis=1))#suma de los ejes 1  """
""" a= np.array([[5,10,15,20,25],[3,6,4,8,12]]) 
print(a)
print(a.min(axis=0 ))#saca el min de el eje que le diga  """

""" a= np.array([[5,10,15,20,25],[3,6,4,8,12]]) 
print(a)
print(np.sqrt(a))#raiz """

# a= np.array([[5,10,15,20,25],[3,6,4,8,12]]) 
# print(a)
# print(np.exp(a))#exponencial
""" a= np.array([[5,10,15,20,25],[3,6,4,8,12]])
b= np.array([[1,2,3,4,5],[6,7,8,9,10]]) 
print(a)
print(b)
c= np.add(a,b)#suma las matraizes componente a componente 
print(c)
 """
# a=np.array([15.33332,20.8956,25.52636])
# print(a.round(decimals=2))#redondea al entero mas proximo

""" a=np.array([15.33332,20.8956,25.52636])
print(np.ceil(a))#redondea al entero mas proximo
a=np.array([15.33332,20.8956,25.52636])
print(np.floor(a))#redondea al entero anterior """

a=np.array([15.33332,20.8956,25.52636])
print(np.gradient(a))# almacena toda la información de la derivada parcial de una función multivariable.



