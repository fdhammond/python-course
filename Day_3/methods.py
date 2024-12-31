# upper Method
# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:

sentence = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(sentence.upper())

# join Method
# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
sentence_list = ["La","legibilidad","cuenta."]
print(" ".join(sentence_list))

# replace Method
#Reemplaza en la siguiente frase:
# "Si la implementación es difícil de explicar, puede que sea una mala idea."
# los siguientes pares de palabras:
# "difícil" --> "fácil"
# "mala" --> "buena"
# y muestra en pantalla la frase con ambas palabras modificadas.

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
result = frase.replace("difícil", "fácil").replace("mala", "buena")
print(result)

# multiply words
texto = "Repetición"
print(texto * 15)

# Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
# Tierra mojada,
# mis recuerdos de viaje
# entre las lluvias

haiku = "Tierra mojada, mis recuerdos de viaje entre las lluvias"
print("agua" not in haiku)

# Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
print(len("electroencefalografista"))
