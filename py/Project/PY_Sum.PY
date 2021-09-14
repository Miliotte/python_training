result = None
n1 = float(input("Primeiro numero:"))

n2 = float(input("Segundo numero:"))

opc = input("\nInforme o tipo de operação que você deseja:")

if opc == "+":
   print ("Você escolheu a adição")
   print ("'{}' + '{}'" .format(n1,n2))
   result=float(n1+n2)

elif opc == "-":
   print ("Você escolheu a subtração")
   print ("'{}' - '{}'" .format(n1,n2))
   result=float(n1-n2)

elif opc == "*":
   print ("Você escolheu a multiplicação")
   print ("'{}' * '{}'" .format(n1,n2))
   result=float(n1*n2)

elif opc == "/" and n2 == 0:
   print("Não é possivel realizar a divisão por zero")
   sys.exit(1)

elif opc == "/":
   print ("Você escolheu a divisão")
   print ("'{}' / '{}'" .format(n1,n2))
   result=float(n1/n2)

else:
   print("Opção invalida!")

if result:

   print ("Resultado = " '{}' .format(result))
