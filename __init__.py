import requests


class Busca_cep:
    def __init__(self, cep):
        cep = str(cep)
        if self.verifica_cep(cep):
            self.cep = cep
        else:
            raise AttributeError('Cep inválido')

    def verifica_cep(self, cep: str):
        if len(cep) == 8:
            return True
        else:
            return False

    def acessa_cep(self):
        url_api = f'https://viacep.com.br/ws/{self.cep}/json/'
        read = requests.get(url_api)
        dados_cep = read.json()
        print('\nRua:', dados_cep['logradouro'],
              '\nBairro:', dados_cep['bairro'],
              '\nCidade:', dados_cep['localidade'],
              '\nEstado:', dados_cep['uf'])


cep01 = Busca_cep('04538132')
cep01.acessa_cep()


