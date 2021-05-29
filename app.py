#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PF008

Objetivos:
Desenvolver um bot para desempenhar as seguintes funções:
- Acompanhar a rentabilidade das aplicações do fundo, e as porcentagens em cada tipo de investimento (ex: 60% em FI, 20% em RV, 10 em Cripto e etc).
- Armazenar as ações dos “traders” e rapidamente atualizasse a plataforma em detrimento das mudanças (ex: 5% de FI para RV).
- Monitorar os investimentos e ações do fundo constantemente para oferecer os dados aos clientes
- Monitorar os serviços e ter noção de como o seu dinheiro está sendo administrado.
- Disponibilizar as informações por meio de mensagens a um grupo de telegram ou whatsapp.

"""

import ast
import pandas as pd
import pandas_datareader.data as web 

clientes = pd.read_excel('programação.xlsx')
# listaAcoes = clientes['ação'].loc[0]
listaAcoes = []
acoes = clientes['ação']
[listaAcoes.append(ast.literal_eval(i)) for i in acoes]

all_data =[]
for atual in listaAcoes:
    [print(i) for i in atual]
    # all_data.append({ticker: web.get_data_yahoo(ticker) for ticker in atual})
print(all_data)
# price = pd.DataFrame({ticker : data['Adj Close'] for ticker, data in all_data.items()}) 
# volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()}) 
# returns = price.pct_change()

# print(returns.corr())
# print(returns.cov())
# print(returns['MSFT'].corr(returns['IBM']))
# print(returns.corrwith(returns.IBM))