# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:10:24 2019

@author: Arnoldo
"""

def posicoesQueIniciamCom(lista, letra):
    result = []
    for i, palavra in enumerate(lista):
        if palavra.startswith(letra):
            result.append(i)
    return result

def posicoesQueTerminamCom(lista, letra):
    result = []
    for i, palavra in enumerate(lista):
        if palavra.endswith(letra):
            result.append(i)
    return result
"""
#ponts=['.',',','!']
pos=posicoesQueTerminamCom(tokens, '.')

while(len(pos)!=0):
    for i in pos:
        tokens[i]=tokens[i][0:len(tokens[i])-1]
    pos=posicoesQueTerminamCom(tokens, '.')
   
pos=posicoesQueIniciamCom(tokens, '@')
for i in pos:
    tokens[i]='user'
    
pos=posicoesQueIniciamCom(tokens, '#')
for i in pos:
    tokens[i]='hash'
    
pos=posicoesQueIniciamCom(tokens, 'http')
for i in pos:
    tokens[i]='link'
    
#for i in pos:
#    tokens.remove(tokens[i])
"""