#Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido

print('\t-----Tabuada-----')
numero = int(input('informe um numero para ver a tabuada: '))

print('\nTabuada de', numero, ':')

for i in range(1,11):
    print(numero, 'X', i, '=', (numero * i))
print("\n")



#----------------------------------------------#

print('\t-----Caulculo do novo salario-----')
salario_atual = float(input('Informe os salario atual'))

if (salario_atual<500):
    salario_novo=salario_atual+(salario_atual*0.15)
    print('Salario com reajuste = ', salario_novo)

if ((salario_atual>=500) and (salario_atual <=1000)):
    salario_novo=salario_atual+(salario_atual*0.10)
    print('Salario com reajuste = ', salario_novo)

if (salario_atual>1000):
    salario_novo=salario_atual+(salario_atual*0.05)
    print('Salario com reajuste = ', salario_novo)
print("\n")


#03 Escreva um programa que mostre todos os numeros entre 5 e 100 que são divisiveis por 7, mas não são multiplos de 5. os numeros obtidos devem ser impressos em sequencia.

print('\t--Numeros entre 5 e 100 que são diviseis por 7--')
for num in range(5, 100):
    if (num % 7 == 0 and num % 5 != 0):
        print(num)
print("\n")



#04 Faça um programa que receba um numero digitado pelo usuario e caucule a soma de todos os numeros de 1 ate ao numero digitado. Por exemplo, se o usuario digitpou o numero 4, a saida deve ser 10 -> (1+2+3+4=10).

print('\t-----Soma de 1 ate o valor digitado-----')
soma_numeros = 0
numero = int(input("Por favor, insira o numero: "))
for i in range(1, numero + 1, 1):
    soma_numeros += i
print("A soma é = ", soma_numeros)
print("\n")

#05 Faça um programa que recebendo um valor inteiro, informe se o numero é positivo, negativo ou neutro

print('\t-----A dança dos numeros-----')
x = int(input("Informe um numero para bricar: "))
if x < 0:
        print('É um numero negativo ')
elif x == 0:
          print('É um numero neutro ')
elif x > 0:
          print('É um numero positivo ')
print("\n")



#06 crie um algoritimo que receba um numero, conte o numero de total de digitos e mostre o resultado. Por exemplo, se o numero é 2021, então a saida deve ser 4

print('\t-----Contagem dos digitos-----')
digitos = int(input("Digite um numero para contar seus digitos: "))
contador = 0
while digitos != 0:
  digitos //= 10
  contador += 1
print("Total de digitos = ", contador)
print("\n")
        