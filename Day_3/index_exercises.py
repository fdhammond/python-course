# Find "u" letter in word
word = "computer"
print(word[4])

# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

word_sentence = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(word_sentence.index("práctica"))

# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

word_new_sentence = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(word_new_sentence.rindex("práctica"))