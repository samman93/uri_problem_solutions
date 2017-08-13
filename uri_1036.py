v = input().split(" ")
a = float(v[0])
b = float(v[1])
c = float(v[2])


try:
  b1 = (-b + ((b ** 2)-(4 * a * c))**0.5)/(2 * a)
  b2 = (-b - ((b ** 2)-(4 * a * c))**0.5)/(2 * a)

  b1  = '{:.5f}'.format(b1 )
  b2  = '{:.5f}'.format(b2 )
  x = ((b ** 2)-(4 * a * c))
  if(x < 0):
    print("Impossivel calcular")
  else:
    print("R1 = "+str(b1))
    print("R2 = "+str(b2))
except:
  print("Impossivel calcular")