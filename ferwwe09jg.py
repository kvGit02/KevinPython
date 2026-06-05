claves = ["nombre", "edad", "ciudad", "profesion"]
valores = ["Carlos", 25, "Madrid", "Ingeniero"]
resultado = {}
for i in range(len(claves)):
    resultado[claves[i]] = valores[i]
print("Diccionario combinado:", resultado)