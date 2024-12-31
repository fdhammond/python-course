# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
# "Controlar la complejidad es la esencia de la programación"
# Pista: "Controlar" tiene un largo de 9 caracteres.

sentence = "Controlar la complejidad es la esencia de la programación"
print(sentence[0:9])

# Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
# "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

sentence_two = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(sentence_two[8::3])

# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
# "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

sentence_three = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(sentence_three[::-1])
