""" Importar extrado Bradesco """
import pandas as pd

# Caminho do extrato
URL = 'Bradesco_11032024_084106.xls'

def le_extrato(url):
    """ 
        Recebe um xls ok
        Limpar os dados ok
        Separar as informações por documento ok
        Retorna um array ok
    """

    # Converter extrato em data frame
    df = pd.read_excel(url)

    # Renomear Colunas
    colunas = ['Data',	'Histórico',	'Docto.',	'Crédito (R$)',	'Débito (R$)',	'Saldo (R$)']
    df.columns = colunas

    # Limpando linhas do topo do dataframe
    for index in df.index:
        if isinstance(df['Data'].loc[index], str):
            df = df.drop(df.index[:index])
            df = df.drop(df.index[0])
            break

    # Limpando final do dataframe
    cont = 0
    for index in df.index:
        if isinstance(df['Histórico'].loc[index], float):
            index = index-1
            df = df.drop(df.index[cont:])
            break
        cont += 1

    # Separar informações por doc:
    dados = []
    for index in df.index:
        if isinstance(df['Docto.'].loc[index], str):
            # Criar Sub conjunto
            sub_dados = []
            # # Checar se proxima linha é vazia
            if isinstance(df['Docto.'].loc[index+1], str):
                # Não é vazia Criar sub conjunto com Histórico de uma linha só
                for coluna in colunas:
                    sub_dados.append(df[coluna].loc[index])
                dados.append(sub_dados)
            else:
                # É vazia Cria sub conjunto com histórico de duas linhas
                for coluna in colunas:
                    if coluna == 'Histórico':
                        sub_dados.append(df[coluna].loc[index]+' '+df[coluna].loc[index+1])
                    else:
                        sub_dados.append(df[coluna].loc[index])
                dados.append(sub_dados)

    return df


extrato = le_extrato(URL)
