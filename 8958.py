# Problem
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# Input 
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

# Output
# 각 테스트 케이스마다 점수를 출력한다.

# limit
#  0 < question < 80, consist of 'O','X'

noq = int(input())

questions = [input() for _ in range(noq)]
for question in questions:
  plus = 0 # 기본점수
  score = 0 # 최종점수
  for element in question:
    if element == 'O':
      plus += 1
      score += plus
    elif element == 'X':
      plus = 0
  print(score)
  
# good
import sys

n = int(input())
for _ in range(n):
    l = sys.stdin.readline().rstrip().split('X')
    s = 0
    for i in range(len(l)):
        s += sum(range(len(l[i]) + 1))
    print(s)

# What I learned
# split('X')와 len(l[i]) + 1 방법을 쓰는 방법도 있었다.
# input()과 sys를 import하여 사용 한 sys.stdin.readline() 차이점
#   속도측면 input < sys.stdin.readline()
#   종종 입력 값에서 prompt message가 필요 없는 BOJ에서 시간 초과 문제가 
#   발생할 경우 sys.stdin.readline()를 사용하면 시간 초과 문제를 해결할 수 있다. 출처 https://blog.sungmin.dev/102