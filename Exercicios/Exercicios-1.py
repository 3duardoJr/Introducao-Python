#Exercicios de fixação
import math

print("i)")
print ("------------------------------------------------------------------")
a = float(input('Entre com o primeiro numero: '))
b = float(input('Entre com o segundo numero: '))
adicao = a+b
print('A soma dos dois numeros dados é: ', adicao)
subtracao = a-b
print('A subtração do primeiro numero pelo segundo é: ', subtracao)
divisao = a/b
print('A divisao do primeiro numero pelo segundo é: ', divisao)
multiplicacao = a*b
print('A multiplicação dos dois numeros dados é: ', multiplicacao)
print ("------------------------------------------------------------------")
print("ii)")
print ("------------------------------------------------------------------")
tp = float(input('Entre com o tempo que foi gasto na viagem: '))
vm = float(input('Agora entre com a velocidade media que foi realizado o percurso: '))
dist = tp*vm
litros = dist/12
print(f'Você informou que o tempo da viagem foi de {tp}h e a velocidade média foi de {vm}km como seu automovel consome 1l a cada 12km, estimasse que...')
print(f'A distancia percorrida nesse tempo foi de {dist} e foram se consumidos {litros:.2f}L de combustivel')
print ("------------------------------------------------------------------")