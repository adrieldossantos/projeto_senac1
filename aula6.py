'''
def fatorial (a):
    if a == 0: 
       return 1 
    else:
        fat = 1 
        for i in range (1, a+1): 
            fat *=i 
        return fat 
    
x = int(input("digite um numero inteiro: "))
print("o fatorial de", x, "é: ", fatorial(x))

'''

'''
def fatorial (a):
    if a == 0: 
       return 1 
    else:
        fat = 1 
        for i in range (1, a+1): 
            fat *=i 
        return fat 
    
x = int(input(": "))
print("o fatorial de", x, "é: ", fatorial(x))

a = input("digite seu nome: ")
b = int(input("digite seu numero: "))
c = float(input("digite seu ponto flutuante: ")) 

soma = c + b 

subtracao = c + b 

'''
'''
# nome, idade, altura, tem_carro

nome = input("digite seu nome: ") 
idade = int(input("digite sua idade "))
altura = float(input("digite sua altura: "))
tem_carro = input("vocé possui algum carro? (sim/não): ")

tem_carro = tem_carro.lower() == "sim"

print("informações digitadas: ")
print("nome: ", nome)
print("idade: ", idade)
print("altura: ", altura)
print("tem_carro? ", "sim" if tem_carro else "não")

'''

'''

def contagem_regressiva()
    numero = int(input("digite um número inteiro positivo: "))

    if numero <= 0:
        print("pro favor, digite um número inteiro positivo.")
        contagem_regressiva 
    else:
        while numero >= 0:
            print(numero)
            numero -= 1

contagem_regressiva

'''

'''

# soma, subtracao, multiplicaçãõ, divisão
def culculadora():
    soma = 1 

    print(if ("digite o nume: 1", ))


    soma = print("soma: 1")
    subtracao = print ("subtracao: 2")
    multiplicação = print("multiplicação: 3")
    divisão = print("divisão: 4")

'''








def soma (a, b): 
    return a +b
def subtracao(a, b):
    return a -b
def multiplicação (a, b):
    return a *b
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "divisão inválida"
    
def calculadora():
    print("bem-vindo a calculadora em python!")
    print("selecione a a operaçao desejada: ")
    print("1: adisao")
    print("2: subtracao")
    print("3: multiplicacao")
    print("4: divisao")

    escolha = input("digite sua escolha 1/2/3/4: ")
    if escolha in ('1', '2', '3', '4',):
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input( "digite o segundo numero: "))
        
        if escolha == '1':
            print("")










