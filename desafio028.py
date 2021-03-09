#esse programa gera um numero de 0 a 5, pede para o usuario advinhar, e retorna com menssagem de erro ou acerto.

#importa da biblioteca random a função randrange
from random import randrange
from time import sleep
#através da função randrange, atribui um numero aleatorio de 1 até 5 ao naleatorio
naleatorio = randrange(1, 5)
sorte =int(input('Bom dia meu amigo(a).\nEstou pensando em um numero de 1 a 5!\nSerá que você acerta? '))
print('Pensando aqui como te trapacear...  ... ...')
sleep(4)
if sorte == naleatorio:
    print('parabens você é foda mesmo')
else:
    print(f'Eu tinha pensado em {naleatorio}')
    print('Continue tentando um dia voce consegue hahahaha!')

if sorte > 5:
    print(f'Você é burro? eu disse de 0 a 5, {sorte} é maior que 5, é cada doido que me aparece.')