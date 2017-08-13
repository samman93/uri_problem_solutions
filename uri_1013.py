v = input().split(" ")
a = int(v[0])
b = int(v[1])
c = int(v[2])

ab = (a + b + abs(a-b))/2
abc = (ab + c + abs(ab-c))/2

print(str(int(abc))+ " eh o maior")
