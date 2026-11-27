# Guarda el primer texto completo en la variable parrafo1
parrafo1 = "Cada dia te quiero mas y nunca lo he olvidado."

# Guarda el segundo texto completo en la variable parrafo2
parrafo2 = "En el corazón de una historia de amor tecnológica, Lucas y Carla compartían su pasión por la programación. Cada día, mientras aprendían a programar, sus corazones se sincronizaban con cada línea de código."

# Guarda el tercer texto completo en la variable parrafo3
parrafo3 = "En cada amanecer, veo el brillo de tus ojos; en cada atardecer, siento el calor de tu abrazo; y en cada noche estrellada, me pierdo en el infinito de tu amor."

# Imprime el título principal en la consola
print("Mensajes Secretos Decodificados:")

# Imprime el encabezado del primer mensaje secreto
print("Mensaje secreto 1:")
# Extrae caracteres usando rebanado (slicing): empieza en el índice 1 y avanza de 18 en 18 hasta el final
print(parrafo1[1::18])

# Imprime el encabezado del segundo mensaje secreto
print("Mensaje secreto 2:")
# Extrae una subcadena desde el índice 138 hasta el 146 (el 147 no se incluye)
print(parrafo2[138:147])

# Imprime el encabezado del tercer mensaje secreto
print("Mensaje secreto 3:")
# Cada print siguiente obtiene y muestra un único carácter según su posición (índice) en parrafo3
print(parrafo3[125])
print(parrafo3[94])
print(parrafo3[35])
print(parrafo3[107])
print(parrafo3[20])
print(parrafo3[1])