v = input().split(" ")
a = int(v[0])
b = int(v[1])

if a==b:
  print("O JOGO DUROU 24 HORA(S)")
elif a > b: 
  x = 24 - a + b
  print("O JOGO DUROU "+str(x)+" HORA(S)")
elif b > a:
  x = b - a
  print("O JOGO DUROU "+str(x)+" HORA(S)")