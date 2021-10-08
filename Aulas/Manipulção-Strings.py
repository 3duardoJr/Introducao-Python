print('i')
a = 'casaco'
print(a)
print(' ')

print('ii')
maiscula = a.upper()
print(maiscula)
print(' ')

print('iii')
minuscula = maiscula.lower()
print(minuscula)
print(' ')

print('iv')
capital = a.capitalize()
print(capital)
print(' ')

print('v')
metade = a[0:4]
print(metade)
print(' ')

print('vi')
ultimas = a[2:]
print(ultimas)
print(' ')

print('vii')
b = a.replace('aco', 'tor')
print('Antes de mudar: ', a)
print('Depois de mudar: ', b)
print(' ')

print('viii')
#Para encontrar a primeira que ele encontrar, ou seja,
#se tiver dois vai retornar apenas a primeira.
print(b.find('a'))
print(' ')

print('ix')
#Se você fizer uma busca de algo que nao existe vai acontecer isso.
print(b.find('t'))
print(' ')

print('x')
#Para printar o tamanho e otimo para ver que os espaços em Python
#tambem são considerados caracteres.
e = ' casaco '
print(e)
print(len(e))
print(' ')

print('xi')
#Para tirar os espaços, como vemo abaixo, o número de caracteres diminuiu.
f = e.strip()
print(f)
print(len(f))
print(' ')

print('xii')
n1 = 8
n2 = 2
#Ao usar essa propriedade de 'f' pode-se acessar os valores dessas
#variaveis e as concatenalas pelo meio da frase.
print(f'O número {n1} dividio por {n2} é {n1/n2}')