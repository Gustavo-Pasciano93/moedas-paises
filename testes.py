from extraindo import DadosRepositórios

from repositorios import ManipulaRepertorios

moedas_lusitanas = DadosRepositórios('portuguese')
tabelas_moedas_lusitanas = moedas_lusitanas.cria_df_linguagens()

tabelas_moedas_lusitanas.to_csv('moedas_paises.csv')



novo_repo = ManipulaRepertorios('Gustavo-Pasciano93')

nome_repo = 'moedas-paises-lingua-portuguesa'

novo_repo.cria_repo(nome_repo)

novo_repo.add_arquivo(nome_repo, 'moedas_paises.csv')