# O programa deve pegar um arquivo em CSV, consolidar em Excel e enviar uma atualização diária dessa planilha por e-mail.
import os # manipula arquivos do computador
from datetime import datetime # lidar com datas
import pandas as pd # lida com bases de dados
import win32com.client as win32 # permite disparo de e-mails automáticos

# r usado para expressões regulares, mas permite visualizar o caracter de escape
caminho = r"exercicios\automacao_de_planilhas\bases"

# Função listdir() recebe como parâmetro o caminho para um diretório e retorna uma lista com os nomes do que está contido nele.
arquivos = os.listdir(caminho)
print(arquivos)

# Cria uma tabela chamada tabela_consolidada através de um DataFrame vazio do Pandas
tabela_consolidada = pd.DataFrame()

for nome_arquivo in arquivos:
    tabela_vendas = pd.read_csv(os.path.join(caminho, nome_arquivo)) # lê os arquivos .csv dentro do caminho especificado 
    
    tabela_vendas["Data de Venda"] = pd.to_datetime("01/01/1900") + pd.to_timedelta(tabela_vendas["Data de Venda"] - 2, unit="d")

    tabela_consolidada = pd.concat([tabela_consolidada, tabela_vendas])

tabela_consolidada = tabela_consolidada.sort_values(by = "Data de Venda")
tabela_consolidada = tabela_consolidada.reset_index(drop = True)
tabela_consolidada.to_excel("Vendas.xlsx", index = False)

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)
email.To = "reginaldo0481@gmail.com"
data_hoje = datetime.today().strftime("%d/%m/%Y")
email.Subject = f'Relatório de vendas {data_hoje}'
email.body = """
Prezado,

Segue anexo o relatório de vendas de {data_hoje} atualizado.

Att.
Reggie 
"""