def paridade(numero):
    if numero%2 == 0:
        return "par"
    else:
        return "ímpar"
        
def fatorial(numero):
    fatorial = 1
    
    while (numero > 1):
        fatorial = fatorial * numero
        numero = numero - 1
        
    return fatorial
