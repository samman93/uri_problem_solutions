v = input().split(" ")
a = int(v[0])
b = int(v[1])
c = int(v[2])
d = int(v[3])

if a==c and b == d :
  print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif c > a and b >d:
  x = c - a -1
  m = 60-(b-d)
  print("O JOGO DUROU "+str(x)+" HORA(S) E "+str(m)+" MINUTO(S)")
elif c > a and d > b:
  x = c - a
  m = d - b
  print("O JOGO DUROU "+str(x)+" HORA(S) E "+str(m)+" MINUTO(S)")
elif a > c and b >d:
  m = 60-(b-d)
  x = 24-(a-c) - 1
  print("O JOGO DUROU "+str(x)+" HORA(S) E "+str(m)+" MINUTO(S)")
elif a > c and d > b:
  x = 24-(a-c)
  m = d - b
  print("O JOGO DUROU "+str(x)+" HORA(S) E "+str(m)+" MINUTO(S)")
 