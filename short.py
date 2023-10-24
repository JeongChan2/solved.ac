# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")

# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print("||_/=\\\__|")

# n = int(input())
# nums = [int(x) for x in input().split()]
# print(min(nums), max(nums))

# input()
# a = [int(i) for i in input().split()]
# print(min(a), max(a))

# test = [1, 2, 3, 4]
# print(*test) # 1 2 3 4

# from sys import stdin
# _, *a = map(int, stdin.buffer.read().split())
# print(min(a), max(a))

# a, b = map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# a, b = map(int,input().split())
# li = [int(i) for i in input().split()]
# for i in li:
#   if i < b:
#     print(i, end=" ")

# import sys

# n, v = map(int, sys.stdin.readline().split(' '))
# lis = map(int, sys.stdin.readline().split(' '))
# result = []

# for num in lis:
#     if num < v:
#         result.append(str(num))

# print(*result) # print(' '.join(result))

# n = int(input())
# result = []
# for i in range(n):
#   a,b = map(int,input().split())
#   result.append(str(a+b))
# print('\n'.join(result))

# import sys
# for i in sys.stdin:
#     c = sum(map(int, i.split()))
#     print(c)
    
# import sys
# for i in sys.stdin:
#     a, b = map(int, i.split())
#     if a==0 and b==0:
#       break
#     print(a+b)

# import sys
# a, b = map(int,sys.stdin.readline().split())
# print(a*b)

# ch = input()
# print(ord(ch))

# sum = 0
# input()
# a = input()
# for i in a:
#   sum += int(i)
# print(sum)

# s = """         ,r'"7
# r`-_   ,'  ,/
#  \. ". L_r'
#    `~\/
#       |
#       |"""
# print(s)

print(input()[int(input())-1])