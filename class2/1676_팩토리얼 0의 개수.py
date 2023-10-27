# Problem
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# Input 
#   첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)


# Output
#   첫째 줄에 구한 0의 개수를 출력한다.

# limit
#   (0 ≤ N ≤ 500)

def factorial(n):
    if(n > 1):
        return n * factorial(n - 1)
    else:
        return 1
      
n = factorial(int(input()))
hab = 0
while True:
  if n%10 == 0:
    hab += 1
  else:
    break
  n //= 10
print(hab)

# good
a = int(input())

summing = 1
count = 0
tt = -1

for i in range(1, a+1):
    summing *= i

while True:
    summing = str(summing)
    if summing[tt] == '0':
        count += 1
        tt -= 1

    else:
        break

print(count)