import requests

from core_apps.states.models import State


def run():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    response = requests.get(url)
    states = response.json()
    for state in states:
        result = {
            'sigla': state['sigla'],
            'nome': state['nome']
        }
        print(result['sigla'])
        print(result['nome'])
        State(**result).save()
        print('------------------')
