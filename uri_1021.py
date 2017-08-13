a = input().split(".")
a[0] = int(a[0])
a[1] = int(a[1])
print("NOTAS:")
x=[]
g = [100,50,20,10,5,2]
for y in g:
  x.append(int(a[0]/y))
  a[0]=a[0]%y
if(a[0] == 1):
  a[1] = a[1] + 100

for h in range(0,len(x)):
  print(str(x[h])+" nota(s) de R$ "+str(g[h])+".00")
  
  
print("MOEDAS:")
s=[]
t = [100,50,25,10,5,1]
for u in t:
  s.append(int(a[1]/u))
  a[1]=a[1]%u


for v in range(0,len(s)):
  print(str(s[v])+" moeda(s) de R$ "+str('{:.2f}'.format(t[v]/100)))
  