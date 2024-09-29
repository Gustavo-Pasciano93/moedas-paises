import requests
import base64

class ManipulaRepertorios:
    
    def __init__(self,username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token ='token secreto'
        self.headers = {'Authorization': 'Bearer ' + self.access_token}
        
        
    def cria_repo(self, nome_repo):
        data = {
            'name': nome_repo, 
            'description': 'Dados dos repositorios dos paises e suas moedas',
            'private': False
        }
        url = f'{self.api_base_url}/user/repos'
        response = requests.post(url, json=data, headers = self.headers)
        print(f'status da criação do repositorio: {response.status_code}')
        
        
    def add_arquivo(self,nome_repo, nome_arquivo, caminho_arquivo):
        #codificando
        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)
        
        #Fazendo Upload
        url = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{caminho_arquivo}'
        data = {
            "message": "Adicionando novo arquivo",
            "content": encoded_content.decode('utf-8')
        }
        
        response = requests.put(url,json=data, headers = self.headers)
