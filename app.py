base = input('Digite a base da sua senha: ')
senha = ''

for letra in base:
  if letra in 'aA': senha = senha + '8'
  elif letra in 'Bb': senha = senha + '3'
  elif letra in 'Cc': senha = senha + '7'
  elif letra in 'Dd': senha = senha + '12'
  elif letra in 'Ee': senha = senha + '2'
  elif letra in 'Ff': senha = senha + '1'
  elif letra in 'Uu': senha = senha + '!'
  elif letra in 'Ll': senha = senha + '*'
  elif letra in 'Oo': senha = senha + '$'
  elif letra in 'Pp': senha = senha + '@'
  elif letra in 'Ii': senha = senha + '%'
  elif letra in 'Ss': senha = senha + '&'
  else: senha = senha + letra
  
print(senha)