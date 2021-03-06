# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("dados.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for indice in range(21):
    print(data_list[indice])
# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for line in data_list[:20]:
    print(line[6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """Adiciona as colunas de uma lista em uma nova lista
      Argumentos:
          data: Lista a ser verificada.
          index: Indice da coluna da lista.
      Retorna:
          Uma lista referente a coluna da lista."""
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for indice in range(len(data_list)):
        column_list.append(data_list[indice][index])                    
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 20, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------
input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0
nogenero = 0
genders_list = column_to_list(data_list,-2)
for gender in genders_list:
    if gender == "Male":
        male += 1
    elif gender == "Female":
        female += 1
    else:
        nogenero += 1    

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 12 and female == 3, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """Conta os gêneros e retorna em uma lista
      Argumentos:
          data_list: Lista a ser verificada.
      Retorna:
          Uma lista com a quantidade de cada gênero na lista."""
    male = 0
    female = 0
    nogenero = 0
    for indice in range(len(data_list)):
        if (column_to_list(data_list, -2)[indice] == "Male"):
            male += 1
        elif (column_to_list(data_list, -2)[indice] == "Female"):
            female += 1
        else:
            nogenero += 1  
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 12 and count_gender(data_list)[1] == 3, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """Mostra qual é o gênero mais popular na lista(amostragem)
      Argumentos:
          data_list: Lista a ser verificada.
      Retorna:
          Uma string informando qual o dado mais popular na lista."""
    answer = ""
    male, female = count_gender(data_list)
    if male > female:
        answer = "Masculino"
    elif male < female:
        answer = "Feminino"
    else:
        answer = "Igual"        
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Masculino", "Feminino"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_types(data_list):
    """Conta os tipos de usuários e retorna em uma lista
      Argumentos:
          data_list: Lista a ser verificada.
      Retorna:
          Uma lista com a quantidade de cada tipo de usuário na lista."""
    customer = 0
    subscriber = 0
    nogenero = 0
    for indice in range(len(data_list)):
        if (column_to_list(data_list, -3)[indice] == "Customer"):
            customer += 1
        elif (column_to_list(data_list, -3)[indice] == "Subscriber"):
            subscriber += 1
        else:
            nogenero += 1  
    return [customer, subscriber]
print(count_user_types(data_list))    

user_types_list = column_to_list(data_list, -3)
types = ["Cliente", "Assinante"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de Usuários')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipos de Usuários')
plt.show(block=True)

#Mesmo gráfico anterior no formato de pizza/torta (pie). 
input("Aperte Enter para continuar...")

user_types_list = column_to_list(data_list, -3)
labels = ["Cliente", "Assinante"]
size = count_user_types(data_list)
explode = (0, 0.1)
fig1, ax1 = plt.subplots()
ax1.pie(size, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title('Quantidade por Tipos de Usuários')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque só tem essas informações dos usuários que são assinantes, por isso essa inconsistência no resultado"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = float(trip_duration_list[0])
max_trip = 0.
mean_trip = 0.
median_trip = 0.
total = 0
float_trip = []
#Retornar o maior e o menor na lista
for indice in range(len(data_list)):
    if (float(trip_duration_list[indice]) > max_trip):
        max_trip = float(trip_duration_list[indice])
    elif (float(trip_duration_list[indice]) < min_trip):
        min_trip = float(trip_duration_list[indice])
    total+=float(trip_duration_list[indice])
    float_trip.append(float(trip_duration_list[indice]))
#Encontrar a média da lista    
mean_trip = total / len(trip_duration_list)
#Retornar a mediana da lista
float_trip.sort()
if len(float_trip) % 2 == 0:                                                                      
    n = len(float_trip)                                                                           
    median_trip = (float_trip[int(n/2-1)]+ float_trip[int(n/2)] )/2                                                      
else:                                                                                    
    median_trip =float_trip[len(float_trip)/2]   
    
print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 177, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 38781, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 2543, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 739, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 17, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""Função de exemplo com anotações.
    Argumentos:
        param1: O primeiro parâmetro.
        param2: O segundo parâmetro.
    Retorna:
        Uma lista de valores x."""
input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """Conta os tipos de usuários (dados) na lista
    Argumentos:
        column_list: Lista referente a coluna selecionada.
    Retorna:
        Duas listas uma informando os tipos e outra informando a quantidade."""
    item_types = list(set(column_list))
    count_items = []
    total_item = 0

    for i_item_type in range(len(item_types)):
        for i_column_list in range(len(column_list)):
            if item_types[i_item_type] == column_list[i_column_list]:
                total_item += 1
        count_items.append(total_item)
        total_item = 0      
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 20, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------        
