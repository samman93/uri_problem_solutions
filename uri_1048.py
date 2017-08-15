v = float(input())

if v <= 400.00: 
  x = v * (15/100)
  y = v + x
  z = 15
  x  = '{:.2f}'.format(x )
  y  = '{:.2f}'.format(y )
  print("Novo salario: "+str(y))
  print("Reajuste ganho: "+str(x))
  print("Em percentual: "+str(z)+" %")
elif v <= 800.00:
  x = v * (12/100)
  y = v + x
  z = 12
  x  = '{:.2f}'.format(x )
  y  = '{:.2f}'.format(y )
  print("Novo salario: "+str(y))
  print("Reajuste ganho: "+str(x))
  print("Em percentual: "+str(z)+" %")
elif v <= 1200.00:
  x = v * (10/100)
  y = v + x
  z = 10
  x  = '{:.2f}'.format(x )
  y  = '{:.2f}'.format(y )
  print("Novo salario: "+str(y))
  print("Reajuste ganho: "+str(x))
  print("Em percentual: "+str(z)+" %")
elif v <= 2000.00:
  x = v * (7/100)
  y = v + x
  z = 7
  x  = '{:.2f}'.format(x )
  y  = '{:.2f}'.format(y )
  print("Novo salario: "+str(y))
  print("Reajuste ganho: "+str(x))
  print("Em percentual: "+str(z)+" %")
else:
  x = v * (4/100)
  y = v + x
  z = 4
  x  = '{:.2f}'.format(x )
  y  = '{:.2f}'.format(y )
  print("Novo salario: "+str(y))
  print("Reajuste ganho: "+str(x))
  print("Em percentual: "+str(z)+" %")