x=int(input("Введите х: ")) 
y=int(input("Введите y: ")) 
if (1<=x<=y and x<10000 and y<10000):  
  if (x-1)%(y-x+1)==0: 
    print("YES") 
  else: 
    print("NO") 
else: 
  print("Ошибка")
  
plus = int(input("Количество плюсов в выражении"))
res = 1 + 1
for i in range(plus - 1):
  res = 1 + 1 / res
result_round = str(round(res % 1, 5))
print("L1#" + result_round)

a = int(input())
b = int(input())
for i in range(a, b+1):
  if i // 1000 == i % 10 and i // 100 % 10 == i % 100 // 10:
    print(i)

a = int(input())
serebro = 0
zoloto = 0
while a > 0:
  a = a - 1
  b = int(input())
  if b > zoloto:
    zoloto = b
  elif b > serebro and b < zoloto:
    serebro = b
print(serebro)
