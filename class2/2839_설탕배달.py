# Problem
#   상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
#   상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
#   상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# Input 
#   첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

# Output
#   상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

n = int(input())
count_3kg = 0

if n == 5:
  print(1)
  exit()
elif n == 3:
  print(1)
  exit()
elif n < 5:
  print(-1)
  exit()
  

count_5kg = n // 5    # 18kg -> 3개
remain = n % 5        # 18kg -> 3kg

while True:
  if remain % 3 == 0:
    count_3kg = remain // 3
    print(count_5kg + count_3kg)
    break
  else:
    count_5kg -= 1
    remain += 5
  if count_5kg < 0:
    print(-1)
    break


# good
n = int(input())
count = 0
while n >= 0:
    if n % 5 == 0:
        count += (n//5)
        print(count)
        break
    n = n - 3
    count = count + 1
else:
    print(-1)