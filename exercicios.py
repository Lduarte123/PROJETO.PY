# 1. Declaração e Impressão de variáveis
# 1. Escreva um código Python que declare uma variável inteira chamada "idade" e peça ao
# usuário para inserir sua idade. Em seguida, imprima a idade na tela.
# Exemplo de saída:
# ```
# Insira sua idade: 25
# Idade: 25

def inteira():
    idade = int(input("Insira sua idade: "))
    print("Idade: ", idade)


# 2. Crie uma variável do tipo double chamada "altura" e solicite ao usuário que digite sua
# altura. Depois, imprima a altura na tela.
# Exemplo de saída:
# ```
# Digite sua altura: 1.75
# Altura: 1.75
# ```
def altura():
    altura = float(input("Digite sua altura: "))
    print("Altura: ", altura)

# 3. Declare uma variável booleana chamada "verdadeiro" e peça ao usuário para responder
# com "sim" ou "não" se algo é verdadeiro. Em seguida, imprima a resposta na tela.
# Exemplo de saída:
# ```
# É verdadeiro? (sim/não): sim
# Verdadeiro: true
# ```
def verdadeiro():
    verdadeiro = input("É verdadeiro? (sim/não): ") == "sim"
    print("Verdadeiro: ", verdadeiro)


# 4. Escreva um código Python que crie uma variável do tipo String chamada "nome" e solicite
# ao usuário que insira seu nome. Depois, imprima o nome na tela.
# Exemplo de saída:
# ```
# Insira seu nome: João
# Nome: João
# ```
def nome():
    nome = input("Insira seu nome: ")
    print("Nome: ", nome)

# 5. Crie uma variável do tipo char chamada "letra" e peça ao usuário para digitar uma letra
# do alfabeto. Em seguida, imprima a letra na tela.
# Exemplo de saída:
# ```
# Digite uma letra do alfabeto: A
# Letra: A
# ```
def letra():
    letra = input("Digite uma letra do alfabeto: ")
    print("Letra: ", letra)

# 6. Declare uma variável do tipo float chamada "peso" e solicite ao usuário que insira seu
# peso. Depois, imprima o peso na tela.
# Exemplo de saída:
# ```
# Insira seu peso: 68.5
# Peso: 68.5
# ```
def peso():
    peso = float(input("Insira seu peso: "))
    print("Peso: ", peso)

# 7. Escreva um código Python que crie uma variável do tipo boolean chamada "ativo" e peça
# ao usuário para responder com "sim" ou "não" se algo está ativo. Em seguida, imprima a
# resposta na tela.
# Exemplo de saída:
# ```
# Está ativo? (sim/não): não
# Ativo: false
# ```
def ativo():
    ativo = input("Está ativo? (sim/não): ") == "sim"
    print("Ativo: ", ativo)

# 8. Crie uma variável do tipo int chamada "quantidade" e peça ao usuário para inserir a
# quantidade de itens. Depois, imprima a quantidade na tela.
# Exemplo de saída:
# ```
# Insira a quantidade de itens: 10
# Quantidade: 10
# ```
def quantidade():
    quantidade = int(input("Insira a quantidade de itens: "))
    print("Quantidade: ", quantidade)

# 9. Declare uma variável do tipo String chamada "cidade" e solicite ao usuário que digite o
# nome de sua cidade. Em seguida, imprima o nome da cidade na tela.

# Exemplo de saída:
# ```
# Digite o nome da cidade: São Paulo
# Cidade: São Paulo
# ```
def cidade():
    cidade = input("Digite o nome da cidade: ")
    print("Cidade: ", cidade)


# 10. Escreva um código Python que crie uma variável do tipo double chamada "saldo" e peça
# ao usuário que insira seu saldo bancário. Depois, imprima o saldo na tela.
# Exemplo de saída:
# ```
# Insira seu saldo bancário: 1000.50
# Saldo: 1000.50
# ```
def saldo():
    saldo = float(input("Insira seu saldo bancário: "))
    print("Saldo: ", saldo)

# 2. Estruturas Condicionais

# 1. Escreva um código Python que verifique se um número fornecido pelo usuário é positivo,
# negativo ou zero. Imprima uma mensagem correspondente para cada caso.
# Exemplo de saída:
# ```
def verificarNumero():
    numero = int(input("Insira um número: "))
    if numero > 0:
        print("Número positivo")
    elif numero < 0:
        print("Número negativo")
    else:
        print("Número zero")
    
# Insira um número: 5
# O número é positivo.
# ```
# 2. Crie um programa que solicite ao usuário dois números inteiros e verifique se o primeiro
# número é divisível pelo segundo número. Imprima uma mensagem adequada indicando o
# resultado.
# Exemplo de saída:
# ```
# Insira o primeiro número: 10
# Insira o segundo número: 2
# O primeiro número é divisível pelo segundo número.
# ```
def divisivel():
    numero1 = int(input("Insira o primeiro número: "))
    numero2 = int(input("Insira o segundo número: "))
    if numero1 % numero2 == 0:
        print("O primeiro número é divisível pelo segundo número.")
    else:
        print("O primeiro número não é divisível pelo segundo número.")
# 3. Escreva um código Python que verifique se um ano fornecido pelo usuário é bissexto ou
# não. Imprima uma mensagem indicando o resultado.
# Exemplo de saída:
# ```
# Insira um ano: 2020
# O ano é bissexto.
# ```
def bissexto():
    ano = int(input("Insira um ano: "))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("O ano é bissexto.")
    else:
        print("O ano não é bissexto.")
# 4. Crie um programa que solicite ao usuário três números e determine o maior entre eles.
# Imprima o resultado.
# Exemplo de saída:
# ```

# Insira o primeiro número: 10
# Insira o segundo número: 5
# Insira o terceiro número: 8
# O maior número é 10.
# ```]
def maior():
    numero1 = int(input("Insira o primeiro número: "))
    numero2 = int(input("Insira o segundo número: "))
    numero3 = int(input("Insira o terceiro número: "))
    if numero1 > numero2 and numero1 > numero3:
        print("O maior número é", numero1)
    elif numero2 > numero1 and numero2 > numero3:
        print("O maior número é", numero2)
    elif numero3 > numero1 and numero3 > numero2:
        print("O maior número é", numero3)
# 5. Escreva um código Python que receba um caractere do usuário e verifique se é uma
# vogal ou uma consoante. Imprima uma mensagem correspondente.
# Exemplo de saída:

# ```
# Insira um caractere: A
# É uma vogal.
# ```
def vogal():
    letra = input("Insira um caractere: ")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("É uma vogal.")
    else:
        print("Não é uma vogal.")
# 6. Crie um programa que solicite ao usuário o valor de um produto e verifique se ele está
# elegível para um desconto. Caso o valor seja maior ou igual a R$ 100,00, imprima uma
# mensagem informando que o produto está elegível para desconto.
# Exemplo de saída:
# ```
# Insira o valor do produto: 120.50
# O produto está elegível para desconto.
# ```
def desconto():
    produto = float(input("Insira o valor do produto: "))
    if produto >= 100:
        print("O produto está elegível para desconto.")
    else:
        print("O produto não está elegível para desconto.")
# 7. Escreva um código Python que solicite ao usuário a idade de uma pessoa e verifique se
# ela é maior de idade (idade maior ou igual a 18). Imprima uma mensagem correspondente
# para cada caso.
# Exemplo de saída:
# ```
# Insira a idade: 22
# A pessoa é maior de idade.
# ```
def maioridade():
    idade = int(input("Insira a idade: "))
    if idade >= 18:
        print("A pessoa é maior de idade.")
    else:
        print("A pessoa não é maior de idade.")

# 8. Crie um programa que solicite ao usuário uma senha e verifique se ela corresponde à
# senha correta. Imprima uma mensagem informando se a senha está correta ou incorreta.
# Exemplo de saída:
# ```
# Insira a senha: 12345
# Senha incorreta.
# ```
def senha():
    senha = input("Insira a senha: ")
    if senha == "12345":
        print("Senha correta.")
    else:
        print("Senha incorreta.")

# 9. Escreva um código Python que solicite ao usuário uma temperatura em graus Celsius e
# verifique se está acima, abaixo ou igual a 25 graus. Imprima uma mensagem
# correspondente para cada caso.
# Exemplo de saída:
# ```
# Insira a temperatura em graus Celsius: 30
# A temperatura está acima de 25 graus.
# ```
def transformeCelsius():
    temperatura = float(input("Insira a temperatura em graus Celsius: "))
    if temperatura > 25:
        print("A temperatura está acima de 25 graus.")
    elif temperatura < 25:
        print("A temperatura está abaixo de 25 graus.")
    else:
# 10. Crie um programa que solicite ao usuário um número e verifique se ele é par ou ímpar.
# Imprima uma mensagem informando o resultado.
# Exemplo de saída:

# ```
# Insira um número: 7
# O número é ímpar.
# ```
def parOuImpar():
    numero = int(input("Insira um número: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")


# 3. Manipulação de Strings

# 1. Escreva um código Python que declare duas variáveis do tipo String, "nome" e
# "sobrenome", e as inicialize com valores fornecidos pelo usuário. Em seguida, concatene as
# duas strings e imprima o nome completo resultante.
# Exemplo de saída:
# ```
# Insira seu nome: João
# Insira seu sobrenome: Silva
# Nome completo: João Silva
# ```
def nomeCompleto():
    nome = input("Insira seu nome: ")
    sobrenome = input("Insira seu sobrenome: ")
    print("Nome completo: " + nome + " " + sobrenome)

# 2. Crie uma variável do tipo String e atribua a ela uma palavra fornecida pelo usuário. Em
# seguida, converta essa palavra para maiúsculas e imprima o resultado.
# Exemplo de saída:
# ```
# Digite uma palavra: Python
# Palavra em maiúsculas: PYTHON
# ```
def palavraMaiuscula():
    palavra = input("Digite uma palavra: ")
    print(palavra.upper())


# 3. Declare uma variável do tipo String e atribua a ela uma frase fornecida pelo usuário. Em
# seguida, converta essa frase para minúsculas e imprima o resultado.
# Exemplo de saída:
# ```
# Digite uma frase: EU GOSTO DE PYTHON
# Frase em minúsculas: eu gosto de python
# ```
def fraseMinuscula():
    frase = input("Digite uma frase: ")
    print(frase.lower())


# 4. Escreva um código Python que declare uma variável do tipo String e atribua a ela uma
# frase fornecida pelo usuário. Substitua todas as ocorrências de uma determinada palavra
# nessa frase por outra palavra escolhida pelo usuário e imprima o resultado.
# Exemplo de saída:
# ```
# Insira uma frase: Eu gosto de Java
# Insira a palavra a ser substituída: Java
# Insira a palavra de substituição: Python
# Nova frase: Eu gosto de Python
# ```
def substituirPalavra():
    frase = input("Insira uma frase: ")
    palavra = input("Insira a palavra a ser substituída: ")
    novaPalavra = input("Insira a palavra de substituição: ")
    print(frase.replace(palavra, novaPalavra))


# 5. Crie uma variável do tipo String e atribua a ela um texto fornecido pelo usuário. Verifique
# e imprima o comprimento desse texto.

# Exemplo de saída:
# ```
# Digite um texto: Olá, mundo!
# Comprimento do texto: 12
# ```
def comprimentoTexto():
    texto = input("Digite um texto: ")
    print(len(texto))


# 6. Declare duas variáveis do tipo String, "palavra1" e "palavra2", e atribua a elas duas
# palavras fornecidas pelo usuário. Verifique se as duas palavras são iguais (ignorando
# maiúsculas ou minúsculas) e imprima o resultado.
# Exemplo de saída:
# ```
# Insira a primeira palavra: Python
# Insira a segunda palavra: Python
# As palavras são iguais: true
# ```
def iguaisPalavras():
    palavra1 = input("Insira a primeira palavra: ")
    palavra2 = input("Insira a segunda palavra: ")
    print(palavra1.lower() == palavra2.lower())


# 7. Escreva um código Python que declare uma variável do tipo String e atribua a ela uma
# frase fornecida pelo usuário. Verifique se essa frase começa com uma determinada palavra
# escolhida pelo usuário e imprima o resultado.
# Exemplo de saída:
# ```
# Insira uma frase: Olá, mundo!
# Insira a palavra de início: Olá
# A frase começa com a palavra fornecida: true
# ```
def comeceComPalavra():
    frase = input("Insira uma frase: ")
    palavra = input("Insira a palavra de início: ")
    print(frase.lower().startswith(palavra.lower()))

# 8. Crie uma variável do tipo String e atribua a ela um texto fornecido pelo usuário. Verifique
# se esse texto termina com uma determinada palavra escolhida pelo usuário e imprima o
# resultado.
# Exemplo de saída:
# ```
# Insira um texto: Olá, mundo!
# Insira a palavra de término: mundo
# O texto termina com a palavra fornecida: true
# ```
def terminaComPalavra():
    texto = input("Insira um texto: ")
    palavra = input("Insira a palavra de término: ")
    print(texto.lower().endswith(palavra.lower()))


# 9. Declare uma variável do tipo String e atribua a ela uma frase fornecida pelo usuário.
# Divida essa frase em palavras separadas e imprima cada palavra em uma linha diferente.
# Exemplo de saída:
# ```
# Insira uma frase: Eu gosto de programação em Python
# Palavras separadas:
# Eu
# gosto

# de
# programação
# em
# Python
# ```
def separarPalavras():
    frase = input("Insira uma frase: ")
    print(frase.split())


# 10. Escreva um código Python que declare uma variável do tipo String e atribua a ela uma
# frase fornecida pelo usuário. Verifique se essa frase contém uma determinada letra
# fornecida pelo usuário e imprima o resultado.
# Exemplo de saída:
# ```
# Insira uma frase: Olá, mundo!
# Insira uma letra: o
# A frase contém a letra fornecida: true
# ```
def contemLetra():
    frase = input("Insira uma frase: ")
    letra = input("Insira uma letra: ")
    print(frase.lower().find(letra.lower()) != -1)



# 4. Estruturas de Repetição

# 1. Escreva um programa que exiba os números de 1 a 10 usando um loop while.
# Exemplo de saída:
# ```
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ```
def exibirNumeros():
    numero = 1
    while numero <= 10:
        print(numero)


# 2. Crie um código Python que solicite ao usuário um número inteiro positivo e exiba todos os
# números pares de 0 até o número fornecido usando um loop for.
# Exemplo de saída:
# ```
# Insira um número: 8
# 0
# 2

# 4
# 6
# 8
# ```

def exibirNumerosPares():
    numero = int(input("Insira um número: "))
    for i in range(0, numero + 1, 2):
        print(i)


# 3. Escreva um programa que solicite ao usuário uma palavra e exiba cada caractere da
# palavra em uma linha separada usando um loop for-each.
# Exemplo de saída:
# ```
# Insira uma palavra: Python
# J
# a
# v
# a
# ```

def exibirCaracteresPalavra():
    palavra = input("Insira uma palavra: ")
    for i in palavra:
        print(i)

# 4. Crie um código Python que solicite ao usuário um número inteiro e calcule o fatorial
# desse número usando um loop while. Em seguida, exiba o resultado.
# Exemplo de saída:
# ```
# Insira um número: 5
# O fatorial de 5 é 120.
# ```

def exibirFatorial():
    numero = int(input("Insira um número: "))
    fatorial = 1
    while numero > 0:
        fatorial *= numero
        numero -= 1
        print(f"O fatorial de {numero} é {fatorial}.")

# 5. Escreva um programa que exiba os números pares de 10 a 0 em ordem decrescente
# usando um loop for.
# Exemplo de saída:
# ```
# 10
# 8
# 6
# 4
# 2
# 0
# ```

def exibirNumerosPares():
    for i in range(10, -1, -2):
        print(i)


# 6. Crie um código Python que solicite ao usuário um número inteiro e verifique se ele é um
# número primo usando um loop for. Em seguida, exiba uma mensagem informando o
# resultado.
# Exemplo de saída:
# ```
# Insira um número: 7
# O número 7 é primo.
# ```

def exibirNumerosPrimos():
    numero = int(input("Insira um número: "))
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            if primo:
                print(f"O número {numero} é primo.")
            else:
                print(f"O número {numero} não é primo.")



# 7. Escreva um programa que solicite ao usuário uma sequência de números inteiros
# (terminada por 0) e exiba a soma desses números usando um loop do-while.
# Exemplo de saída:
# ```

# Insira uma sequência de números (0 para sair): 5 3 2 0
# A soma dos números é 10.
# ```
def exibirSomaNumeros():
    soma = 0
    while True:
        numero = int(input("Insira uma sequência de números (0 para sair): "))
        if numero == 0:
            break
# 8. Crie um código Python que exiba a tabuada de multiplicação de um número fornecido
# pelo usuário usando um loop for.
# Exemplo de saída:
# ```
# Insira um número: 4
# Tabuada do 4:
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40
# ```
def exibirTabuada():
    numero = int(input("Insira um número: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# 9. Escreva um programa que exiba os números ímpares de 1 a 20, pulando de 3 em 3,
# usando um loop while.
# Exemplo de saída:
# ```
# 1
# 4
# 7
# 10
# 13
# 16
# 19
# ```

def exibirNumerosImpares():
    numero = 1
    while numero <= 20:
        print(numero)
        numero += 3

# 10. Crie um código Python que solicite ao usuário um número e exiba a sequência de
# Fibonacci até esse número usando um loop for.
# Exemplo de saída:
# ```

# Insira um número: 15
# Sequência de Fibonacci até 15:
# 0 1 1 2 3 5 8 13
# ```

def exibirFibonacci():
    numero = int(input("Insira um número: "))
    sequencia = [0, 1]
    for i in range(2, numero):
        sequencia.append(sequencia[i - 1] + sequencia[i - 2])
        print(sequencia)


# 5. Funções e Classes
# 1. Crie uma função em Python chamada `soma` que receba dois números inteiros como
# parâmetros e retorne a soma desses números. Em seguida, crie um programa que solicite
# ao usuário dois números e exiba a soma deles usando a função `soma`.
# Exemplo de saída:
# ```
# Insira o primeiro número: 5
# Insira o segundo número: 3
# A soma dos números é 8.
# ```

def soma(a, b):
    return a + b
soma(10, 70)
# 2. Declare uma classe chamada `Retangulo` que tenha os atributos `largura` e `altura`. Crie
# um método na classe chamado `calcularArea` que retorne a área do retângulo (largura
# multiplicada pela altura). Em seguida, crie um programa que solicite ao usuário a largura e a
# altura de um retângulo, crie um objeto da classe `Retangulo` com os valores fornecidos e
# exiba a área do retângulo usando o método `calcularArea`.
# Exemplo de saída:
# ```
# Insira a largura do retângulo: 4
# Insira a altura do retângulo: 6
# A área do retângulo é 24.
# ```


# 3. Crie uma função em Python chamada `ehPrimo` que receba um número inteiro como
# parâmetro e retorne `true` se o número for primo e `false` caso contrário. Em seguida, crie
# um programa que solicite ao usuário um número e use a função `ehPrimo` para verificar se
# o número fornecido é primo. Exiba uma mensagem informando o resultado.
# Exemplo de saída:
# ```
# Insira um número: 7
# O número 7 é primo.
# ```

# 4. Declare uma classe chamada `Produto` que tenha os atributos `nome` e `preco`. Crie um
# método na classe chamado `aplicarDesconto` que receba um percentual de desconto como
# parâmetro e atualize o preço do produto com o desconto aplicado. Em seguida, crie um
# programa que solicite ao usuário o nome e o preço de um produto, crie um objeto da classe

# `Produto` com os valores fornecidos e aplique um desconto de 10% usando o método
# `aplicarDesconto`. Exiba o nome e o novo preço do produto.
# Exemplo de saída:
# ```
# Insira o nome do produto: Laptop
# Insira o preço do produto: 2500.0
# Produto: Laptop
# Novo preço: 2250.0
# ```

# 5. Crie uma função em Python chamada `inverterString` que receba uma String como
# parâmetro e retorne a mesma String invertida. Em seguida, crie um programa que solicite
# ao usuário uma palavra e use a função `inverterString` para inverter a palavra fornecida.
# Exiba a palavra invertida.
# Exemplo de saída:
# ```
# Insira uma palavra: Python
# Palavra invertida: nohtyP
# ```
# 6. Declare uma classe chamada `Circulo` que tenha o atributo `raio`. Crie métodos na
# classe para calcular a área e o perímetro do círculo. Em seguida, crie um programa que
# solicite ao usuário o raio de um círculo, crie um objeto da classe `Circulo` com o raio
# fornecido e exiba a área e o perímetro do círculo usando os métodos da classe.
# Exemplo de saída:
# ```
# Insira o raio do círculo: 5
# Área do círculo: 78.54
# Perímetro do círculo: 31.42
# ```

# 7. Crie uma função em Python chamada `calcularFatorial` que receba um número inteiro
# como parâmetro e retorne o fatorial desse número. Em seguida, crie um programa que
# solicite ao usuário um número e use a função `calcularFatorial` para calcular o fatorial do
# número fornecido. Exiba o resultado.
# Exemplo de saída:
# ```
# Insira um número: 6
# Fatorial de 6: 720
# ```

# 8. Declare uma classe chamada `Aluno` que tenha os atributos `nome` e `nota`. Crie um
# método na classe chamado `verificarAprovacao` que retorne `true` se a nota do aluno for

# maior ou igual a 7 e `false` caso contrário. Em seguida, crie um programa que solicite ao
# usuário o nome e a nota de um aluno, crie um objeto da classe `Aluno` com os valores
# fornecidos e use o método `verificarAprovacao` para verificar se o aluno foi aprovado. Exiba
# o nome do aluno e uma mensagem informando se ele foi aprovado ou não.
# Exemplo de saída:
# ```
# Insira o nome do aluno: João
# Insira a nota do aluno: 8.5
# Aluno: João
# Aprovado? Sim