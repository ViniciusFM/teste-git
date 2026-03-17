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
    print(f'Resultado: { fatorial(n) }') # string template
except ValueError:
    print('Erro! Você deve entrar com um número')
