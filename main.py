def fatorial_rec(n: int) -> int:
    '''
        algoritmo recursivo para resolver fatorial
        input:
            n:int - Um valor inteiro qualquer >0
        output:
            result - Um valor inteiro >0
    '''
    # caso base
    if(n <= 1):
        return 1
    else:
        return n * fatorial_rec(n-1)
    
def fatorial(n: int) -> int:
    '''
        algoritmo iterativo para resolver fatorial
        input:
            n:int - Um valor inteiro qualquer >0
        output:
            result - Um valor inteiro >0
    '''
    res = 1
    for i in range(1, n+1):
        res *= i # mesmo que res = res * i
    return res

try:
    print('===== Fatorial =====')
    n = int(input('Digite um número: '))
    print(f'Resultado iterativo: { fatorial(n) }') # string template
    print(f'Resultado recursivo: { fatorial_rec(n) }') # string template
except ValueError:
    print('Erro! Você deve entrar com um número')
