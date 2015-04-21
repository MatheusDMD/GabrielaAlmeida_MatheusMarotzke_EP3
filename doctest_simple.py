# -*- coding: utf-8 -*-
import doctest

def esvazia_lista(lista):
    """ Esvazia uma lista em python
     >>> l = [1,2,"controle", 'x']
     >>> esvazia_lista(l)
     >>> len(l)
     0
    """
    lista.clear()

    
def soma(a,b):
    """
    Soma valores a e b
    >>> soma(4,5)
    9
    """
    return a + b
    
# O main é ativado quando o arquivo é executado diretamente
# Também pode ser usado como biblioteca
if __name__=="__main__":
    doctest.testmod(verbose="True")
