import requests
from requests.api import request

def main():
    print()
    print('####Consulta CEP###')
    print()
    
    cep_input = input('Digite o CEP que deseja consultar: ')
    while len(cep_input) != 8:
        cep_input = input('CEP INVÁLIDO, DIGITE NOVAMENTE: ')
    
    request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
    values_request = request.json()
    if 'erro' in values_request:
        print('CEP INVÁLIDO!')
        main()
    else:
        print('==> CEP ENCONTRADO <==')
        print(values_request)
        nova_consulta = input('Deseja fazer uma nova consulta? [y/n]: ')
        
        while nova_consulta == 'y':
            main()
            if nova_consulta != 'y':
                print('finished.')

if  __name__ == '__main__':
    main()
    
        