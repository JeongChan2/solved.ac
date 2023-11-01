n = int(input())
lst = list(range(n,0,-1))

for _ in range(n-1):
  lst.pop()
  lst = [lst.pop()] + lst
print(lst[0]) 