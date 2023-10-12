meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict:
    # Si se encuentra la palabra en el diccionario, imprime la definición
    definition = meme_dict[word]
    print("La definición de", word, "es:", definition)
else:
    # Si no se encuentra la palabra en el diccionario, muestra un mensaje de error
    print("No se encontró la palabra", word, "en el diccionario.")
