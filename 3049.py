B = 0
T = 0

B = int(input())
T = int(input())

F = ((B + T)*70)/2
M = (((160-B)+(160-T))*70)/2

if(F > M):
  print('1')
elif(M > F):
  print("2")
else: 
  print('0')