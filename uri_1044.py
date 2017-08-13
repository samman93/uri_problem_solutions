v = input().split(" ")
a = int(v[0])
b = int(v[1])

if a%b ==0 or b%a==0:
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")