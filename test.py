# def security(num):
#   su = ((ord(num)+22)-65) % 26
#   return chr(su+65)

# sen = 'EOXH MHDQV'
# sen2 = ''
# for ch in sen:
#   if ch == ' ':
#     sen2 += ' '
#   else:
#     sen2 += security(ch)
# print(sen2)

def security(num, j):
  su = ((ord(num)+j)-65) % 26
  return chr(su+65)

sen = 'HDW GLP VXP'
sen2 = ''
j = 0
for _ in range(25):
  sen2 = ''
  j +=1
  for ch in sen:
    if ch == ' ':
      sen2 += ' '
    else:
      sen2 += security(ch,j)
  print(sen2)