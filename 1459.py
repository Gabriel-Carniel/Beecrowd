def interseção_intervalos(intervalo1, intervalo2):
    # Desempacotando os intervalos
    (inicio1, fim1) = intervalo1
    (inicio2, fim2) = intervalo2
    
    # Calculando o início e o fim da interseção
    inicio_interseção = max(inicio1, inicio2)
    fim_interseção = min(fim1, fim2)
    
    # Verificando se há interseção
    if inicio_interseção <= fim_interseção:
        return 1, (inicio_interseção, fim_interseção)
    else:
        return 0, 0


from sys import stdin, stdout

while True:
    N = int(stdin.readline())
    try:
        N = int(N)
    except:
        break
    val = [(0, 0)]* N
    res = []

    for i in range(N):
        val[i] =  tuple(map(int, stdin.readline().split()))

    val.sort(key=lambda y: y[0])
    x = 0
    while(x < N-1):
        VER, inter = interseção_intervalos(val[x], val[x+1])
        if VER == 1:
            val[x+1] = inter
        else:
            res.append(inter)
        x += 1

    print(len(res) + 1)
    