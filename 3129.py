N = int(input())
i = 0
f = 0
Album = [0] * 301
rep = 0
unic = 0

while(i < N):
  f = int(input())
  if(Album[f] == 0):
    Album[f] = Album[f] + 1
    unic = unic + 1
  else:
    Album[f] = Album[f] + 1
    rep = rep + 1
  i = i+1

print(unic)
print(rep)