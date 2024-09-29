# Projeto de Extração de Dados - Países de Língua Portuguesa

Este projeto tem como objetivo extrair informações de países que falam a língua portuguesa usando a API **REST Countries** e realizar a manipulação desses dados para obter informações sobre os nomes dos países, as moedas e seus símbolos.

## Funcionalidades do Projeto

- Extração de dados da API REST Countries, com foco em países que têm o **português** como idioma.
- Manipulação de dados para obter:
  - Nomes comuns dos países.
  - Nomes das moedas de cada país.
  - Símbolos das moedas.
- Armazenamento das informações em um arquivo CSV.
- Automação do upload dos dados extraídos para um repositório do GitHub.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **Pandas**: Biblioteca utilizada para manipulação e análise de dados.
- **Requests**: Biblioteca usada para fazer requisições HTTP à API REST Countries.
- **GitHub API**: Utilizada para criar repositórios e adicionar arquivos remotamente no GitHub.

## Estrutura do Projeto

O projeto é dividido em três arquivos principais:

1. **`extraindo.py`**: Contém a classe `DadosRepositórios`, que é responsável por fazer as requisições à API, manipular os dados e gerar um DataFrame com as informações extraídas.

2. **`repositorios.py`**: Contém a classe `ManipulaRepertorios`, que se conecta à API do GitHub, cria repositórios e faz o upload dos arquivos gerados pela extração.

3. **`testes.py`**: Um arquivo de exemplo que demonstra como utilizar as classes `DadosRepositórios` e `ManipulaRepertorios` para realizar todo o processo de extração e upload.

## Como Funciona

### 1. Extração de Dados

A classe `DadosRepositórios` faz uma requisição para a API REST Countries e extrai os dados dos países que falam português.




### 2. Manipulação de Dados

O método cria_df_linguagens() combina três outras funções que extraem os nomes dos países, os nomes das moedas e os símbolos das moedas. O resultado é um DataFrame que organiza esses dados e facilita sua análise.


### 3. Envio de Dados para o Github

A classe ManipulaRepertorios é responsável por criar um repositório no GitHub e fazer o upload dos dados extraídos (em CSV) para esse repositório.

### Arquivos gerados

moedas_paises.csv: Contém os seguintes dados:
nomes-paises: Nome comum dos países que falam português.
nome-moeda: Nome da moeda de cada país.
simbolo: Símbolo da moeda.
