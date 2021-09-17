a = 2
b = 0

#Try é utilizado como exceção( ou seja caso o valor for 0 ele não nós permitirá efetuar a divisão
try:
    print(a/b)
except:
    print("Não é permitido divisão por 0")
print(a/a)


#Try recebendo o valor digitado pelo usuário
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))

v1 = x
v2 = y

try:
    print(v1/v2)
except :
    print("Não é permitido divisão por 0")

