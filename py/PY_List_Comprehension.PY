x =  [1 , 2 , 3, 4, 5]
y = [i**2 for i in x] #Raiz quadrada
z = [i for i in x if i%2==1] #Números ímpa

print("Usando list comprehension")
print(x)
print(y)
print(z)
