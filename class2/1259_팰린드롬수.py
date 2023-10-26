while True:
  n = input()
  if n=='0': break
  else:
    rev_n = n[::-1]
    if n == rev_n:
      print('yes')
    else:
      print('no')