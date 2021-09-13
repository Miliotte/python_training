file = open("file.txt")

#imprimir as lines
lines = file.readlines()

print(lines)

#Imprimir todos as linhas
for line in lines:
    print(line)

texto_completo = file.read()

print(texto_completo)
