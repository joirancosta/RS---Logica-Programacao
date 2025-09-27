# Tipos primitivos de dados em Python

# - int: números inteiros
# - float: números decimais (ponto flutuante)
# - str: cadeia de caracteres (texto)
# - bool: valores lógicos (True ou False)

"""
# Operadores aritméticos: 
+, -, *, **, /, //, %
# Operadores lógicos: 
and, or, not
# Operadores de strings: 
+, *

# Operadores de comparação: recebem valores de diversos tipos e retornam um bool

== igualdade
!= diferença
> maior que
< menor que
>= maior igual a
<= menor igual a

"""
# - Listas: conjunto de dados ordenados - mutável
lista = [1, 4, 3, 4]
frutas = ['banana', 'maçã']
mista = [1, 'texto', 5, True]

# - Tuplas: conjunto de dados ordenados - imutável
coordenada = (5, 6)
tupla = (5, 4, 3, 2)

# Dicionários (dict): conjunto de pares na forma chave e valor
pessoa = { 'nome': 'João', 'idade': 18 }
carro = {
    'marca': 'Volks',
    'modelo': 'Fusca',
    'cor': 'azul',
    'ano': 1970
}

# Conjuntos (sets): Conjunto de dados não ordenados e sem repetição
c1 = {1, 2, 3}
c2 = {3, 2, 1}
c3 = {1, 2, 2, 2, 2, 2, 3, 3, 2, 1, 2, 3}