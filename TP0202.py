#TP1 Ejerc 2
'''2. Implemente un programa que a partir del ancho y alto de una pared calcule cuántos litros de 
pintura se necesitan para pintarla. Aclaración: 1 litro de pintura sirve para 10m cuadrados.'''

print("-----------------Programa Calculador de Pintura------------------")
print()
print ("Ingrese el ancho y el alto de su pared para calcular cuantos")
print ("litros de pintura seran necesarios.")
print()
ancho = (input("Ingrese el ancho de la pared: "))
alto = (input("Ingrese el alto de la pared: "))
LtPinturaNec = float (float(ancho) * float(alto) / 10)
print("Cantidad de pintura necesaria:", LtPinturaNec, "Lts.")

print("Test git")