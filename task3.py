a=int(input())
if (a > 4) and (a < 21):
  print('Вам ', a, ' лет.')
elif a>120:
  print('Ошибка.')
elif a<1:
  print('Ошибка')
elif a>109:
    print('Вам ', a, ' лет.')
elif a==100:
    print('Вам ', a, ' лет.')
else:
  i = a % 10
  if i==1:
    print('Вам ', a, ' год.')
  elif i < 5:
    print('Вам ', a, ' года.')
  else:
    print('Вам ', a, ' лет.')