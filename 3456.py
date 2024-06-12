I = input()
print(I)

V = []
aux = 0
k = 0


for i in I:
    if i.isdigit():  # Verifica se o caractere é um dígito
        V.append(int(i))
res = 0

while(1):

  Ultimo = int(V[-1])
  V3 = V[:-1]
  if (len(V3) == 0):
    break
  cont = 0
  for x in V3:
    if (cont == 0):
      k = str(x)
    else:
      aux = str(x)
      k = k + aux
    cont+=1

  num = int(k)
  res = num*3 + Ultimo
  print(res)


  I = str(res)
  V = []

  for a in I:
    if a.isdigit():  # Verifica se o caractere é um dígito
      V.append(int(a))