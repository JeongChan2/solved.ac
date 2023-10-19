su = int(input())
if (su % 4 == 0 and su % 100 != 0) or (su % 400 == 0):
  print(1)
else:
  print(0)