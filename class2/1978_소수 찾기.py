# Problem
#   주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# Input 
#   첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# Output
#   주어진 수들 중 소수의 개수를 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
tf_lst = [True] * n
lst = [int(x) for x in input().split()]

for t, element in enumerate(lst):
  tmp = int(element**(1/2))
  for i in range(2,tmp+1):
    if element % i == 0:
      tf_lst[t] = False
      break

print(tf_lst.count(True)-lst.count(1))