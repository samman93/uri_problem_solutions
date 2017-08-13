v = input().split(" ")
a = float(v[0])
b = float(v[1])
c = float(v[2])
d = float(v[3])

avg = ((a*2)+(b*3)+(c*4)+(d*1))/(2+3+4+1)
kutta='{:.1f}'.format(avg)
print("Media: "+str(kutta))

if avg >= 7:
  print("Aluno aprovado.")
elif avg < 5:
  print("Aluno reprovado.")
else:
  print("Aluno em exame.")
  h = float(input())
  kutta1='{:.1f}'.format(h)
  print("Nota do exame: "+str(kutta1))
  avg1 = (avg+h)/2
  kutta2='{:.1f}'.format(avg1)
  if avg1 >= 5:
    print("Aluno aprovado.")
  elif avg <= 4.9:
    print("Aluno reprovado.")
  else:
    print("Aluno em exame.")
  print("Media final: "+str(kutta2))