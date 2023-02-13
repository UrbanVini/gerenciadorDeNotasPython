import pandas as pd

#Criando o Dataframe
tabelaAlunos_df = pd.DataFrame({'Marcos':[5.3, 4.4, 10, 2.1],
                   'Andre': [8.8, 6, 6.6, 4.4],
                   'Julia':[6.5, 7.6, 8.7, 2.2],
                    }, index = ['1Bimestre','2Bimestre','3Bimestre', '4Bimestre'])

#Criando variáveis para cada coluna do respectivo aluno
marcos = (tabelaAlunos_df['Marcos'])
andre = (tabelaAlunos_df['Andre'])
julia = (tabelaAlunos_df['Julia'])

#Variavel resp que armazena resposta do cliente
print('Alunos: marcos\nandre\njulia')
resp = input('Digite o nome do aluno que você deseja as notas: ')

#Condicionando a resposta do cliente às variáveis de coluna
if resp == 'marcos':
    display(marcos)
elif resp == 'andre':
    display(andre)
elif resp == 'julia':
    display(julia)
else:
  print('ERRO!!')
#Variavel que armazena resposta do cliente para saber se irá querer visualizar o gráfico
graf_resp = input('Deseja ver um gráfico anual de rendimento dos alunos? (S/N):')

#Condicionando 'print' do gráfico
if graf_resp == 'S' or 's':
  tabelaAlunos_df.plot()
elif graf_resp != 'S' or 's':
  print('Obrigado pela participação')