import sys

k, n = map(int,input().split())
elements = [int(sys.stdin.readline()) for _ in range(k)]

low = 1
high = max(elements)
max_n = 0
while low < high:
  max_n = 0
  mid = (high+low)//2+1
  for element in elements:
    max_n += element // mid
  if max_n >= n:
    low = mid
  elif max_n < n:
    high = mid-1
print(low)