# Problem
#   N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# Input 
#   첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.


# Output
#   M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# limit
#   n (1 ≤ n ≤ 100,000)

import sys
input = sys.stdin.readline

input()
elements = [int(x) for x in input().split()]
elements.sort()
input()
elements2 = [int(x) for x in input().split()]

def binary_search(target, data):
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return 1 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return 0

for target in elements2:
  print(binary_search(target, elements))
  
# good
n,a,m=input(),set(input().split()),input()
print("\n".join((["1" if x in a else "0" for x in input().split()])))

## 풀어쓰면
n = input()
elements = set(input().split())
m = input()
elements2 = input().split()

for x in elements2:
  if x in elements:
    print(1)
  else:
    print(0)