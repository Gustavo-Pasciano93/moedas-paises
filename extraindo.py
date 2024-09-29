import requests
import pandas as pd

class DadosRepositórios:
    
    def __init__(self, argument):
        self.argument = argument
        self.api_base_url = 'https://restcountries.com/v3.1/lang'
        
        
    def extraindo_dados(self):
        endpoint = self.argument
        response = requests.get(f'{self.api_base_url}/{endpoint}')
        response.status_code
        countries = response.json()
        return countries
    
    def nomes_paises(self, countries):
        nomes_paises = []
        for country in countries:
            try:
                nomes_paises.append(country['name']['common'])
            except:
                pass
        return nomes_paises
    
    def nomes_moedas(self, countries):
        nomes_moedas = []
        for country in countries:
            try:
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    nomes_moedas.append(currency_info['name'])
            except:
                pass
        return nomes_moedas
    
    def simbolos_moedas(self,countries):
        simbolos_moedas = []
        for country in countries:
            try:
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    simbolos_moedas.append(currency_info['symbol'])
            except:
                pass
        return simbolos_moedas
    
    
    def cria_df_linguagens(self):
        
        dados = self.extraindo_dados()
        nomes = self.nomes_paises(dados)
        moedas = self.nomes_moedas(dados)
        simbolos = self.simbolos_moedas(dados)
        
        data = pd.DataFrame()
        data['nomes-paises'] = nomes
        data['nome-moeda'] = moedas
        data['simbolo'] = simbolos
        
        return data
    
    
        
        
        
        
        
        
    