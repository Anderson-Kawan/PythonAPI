import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('https://www.receitaws.com.br/v1/cnpj/' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro no Sistema')
        return None

def printar_detalhes(consulta):
    print('CNPJ:',consulta['cnpj'])
    print('Nome:', consulta['nome'])
    print('Status:', consulta['situacao'])
    print('Empresa:', consulta['fantasia'])
    print('Serviços:', consulta['atividade_principal'])
    print('CEP:', consulta['cep'])
    print('Abertura-da-Empresa:', consulta['abertura'])
    print('Telefone:', consulta['telefone'])
    print('Email:', consulta['email'])
    print('Rua:', consulta['logradouro'])
    print('Bairro:', consulta['bairro'])
    print('Casa:', consulta['numero'])
    print('Municipio:', consulta['municipio'])
    print('Complemento:', consulta['complemento'])
    print('UF:', consulta['uf'])
    print('Porte:', consulta['porte'])
    print('Natureza-Juridica:', consulta['natureza_juridica'])
    print('Capital-Social:', consulta['capital_social'])
    print('Atividades-Secundarias:', consulta['atividades_secundarias'])
    print('Diretores:', consulta['qsa'])













sair = False
while not sair:
    oposicao = input('ESCREVA O CNPJ OU ESCREVA *SAIR* PARA FECHAR: ')
    if oposicao == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        consulta = requisicao(oposicao)
        if consulta['status'] == 'ERROR':
            print('CNPJ INVALIDO...')
        else:
            print('CONSULTA FEITA: ')
            printar_detalhes(consulta)


