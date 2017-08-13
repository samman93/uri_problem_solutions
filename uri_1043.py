v = input().split(" ")
a = float(v[0])
b = float(v[1])
c = float(v[2])

if (a+b)>c and (b+c) > a and (a+c)>b:
  x  = '{:.1f}'.format(a+b+c )
  print("Perimetro = "+str(x))
  
else:
  x1  = '{:.1f}'.format(.5*(a+b)*c )
  print("Area = "+str(x1))