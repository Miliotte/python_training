def imprime(n):
    print(n)

imprime("Imprime deste tezxto")



def potencia(n):
    return n * n
x = potencia(4)
print(x)


def intervalo(inic=1, fim=10):
    for inic in range(1,fim+1):
        print(inic)

intervalo(1,10)

#Variable sum e mult

def soma (x,y):
    return x+y
    
def mult(x,y):
    return x*y

s = soma(2,5)
m =  mult(2,5)
print(s)
print(m)

