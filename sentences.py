sentence = ('El nombre del perro es Tomas')

#Mayusculas
print(sentence.upper())
#Minusculas
print(sentence.lower())
#Primer letra mayusculas
print(sentence.capitalize())
#Cuenta el numero de E en la oracion
print(sentence.count('e'))

# primer_nombre='Rene'
# segundo_nombre='Jimenez'
# print(primer_nombre + segundo_nombre)

primer_nombre = input('Introduce tu primer nombre')
segundo_nombre = input('Introduce tu apellido')
print('Hola,' + primer_nombre.capitalize() + ' ' + segundo_nombre.capitalize())