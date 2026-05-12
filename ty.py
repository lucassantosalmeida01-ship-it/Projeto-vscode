ola = input('olá:  ') # comprimento
if ola == 'vai toma no cu': # só pra ver se a pessoa vai falar isso
    print('que feio')
else:  # apresentação da minha calculadora
  print('seja bem vindo a gradiosa calculadora')
  print('feita por mim, Lucas Miguel')
  print('então, primeiramente: ')
  num1 = int(input('nessecito de que você escolha um primeiro número:  ')) # o primeiro número a ser colocado na operação matemática
  num2 = int(input('agora, preciso que você escolha um segundo número:  ')) # o segundo número a ser colocado na operação matemática
  print('')
  print('muito obrigado :)')
  print('agora, vamos para a parte da operação matemática')
 
  # apresentação de todas as operações que eu pude fazer kkkkkk
  print('-SOMA- ')
  print('-SUBTRAÇÃO- ')
  print('-MULTIPLICAÇÃO- ')
  print('-DIVISÃO- ')
  print('-POTÊNCIA- ')
  print('-RAÍZ QUADRADA- ')
  print('')
  print('ok, agora temos seis operações posíveis, ainda, nessa calculadora')
  print('qual você vai escolhar para ficar entre os dois números?')
  print('lembrando que: se você escolher a potência, o segundo valor será a potência')
  print('e se você escolher a raíz quadrada, o segundo número será a raíz')
 
while True:
  operação = input('agora... Pode escolher!  :  ').lower() # agora o usuário pode escolher a operação kkkkkk
  if operação == 'soma' or operação == 'Soma' or operação == 'SOMA': # soma
    print(f'a resposta de sua conta será {num1 + num2}')
    break
  elif operação == 'subtração' or operação == 'Subtração' or operação == 'SUBTRAÇÃO': # subtração
    print(f'a resposta de sua conta será {num1 - num2}')
    break
  elif operação == 'multiplicação' or operação == 'Multiplicação' or operação == 'MULTIPLICAÇÃO': # multiplicação
    print(f'a resposta de sua conta será {num1 * num2}')
    break
  elif operação == 'divisão' or operação == 'Divisão' or operação == 'DIVISÃO': # divisão
    print(f'a resposta de sua conta será {num1 / num2}')
    break
  elif operação == 'potência' or operação == 'Potência' or operação == 'POTÊNCIA': # potência
    print(f'a resposta de sua conta será {num1 ** num2}')
    break
  elif operação == 'raíz' or operação == 'Raíz' or operação == 'RAÍZ' or operação == 'raíz quadrada' or operação == 'Raíz Quadrada' or operação == 'RAÍZ QUADRADA': # raíz
    print(f'a resposta de sua conta será {num1 ** (1 / num2)}')
    break
  else:
    operação = input('a sua resposta não é correspondente a minha pergunta, poderia colocar outra resposta ? :), ok? : ')  # se a resposta não for correspondente, reiniciará.