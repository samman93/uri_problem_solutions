a = int(input())
print(a)
x=[]
g = [100,50,20,10,5,2,1]
for y in g:
  x.append(int(a/y))
  a=a%y


for h in range(0,len(x)):
  print(str(x[h])+" nota(s) de R$ "+str(g[h])+",00")