v = input().split(" ")
a = float(v[0])
b = float(v[1])
c = float(v[2])

TRIANGULO = 0.5 * a * c
CIRCULO = 3.14159 * c ** 2
TRAPEZIO = ((0.5 * (a +b)) *c)
QUADRADO = b * b
RETANGULO = a*b
TRIANGULO  = '{:.3f}'.format(TRIANGULO )
CIRCULO  = '{:.3f}'.format(CIRCULO )
TRAPEZIO  = '{:.3f}'.format(TRAPEZIO )
QUADRADO  = '{:.3f}'.format(QUADRADO )
RETANGULO  = '{:.3f}'.format(RETANGULO )
#print("NUMBER = "+str(a))
print("TRIANGULO: "+str(TRIANGULO))
print("CIRCULO: "+str(CIRCULO))
print("TRAPEZIO: "+str(TRAPEZIO))
print("QUADRADO: "+str(QUADRADO))
print("RETANGULO: "+str(RETANGULO))