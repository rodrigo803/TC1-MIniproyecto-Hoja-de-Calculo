def mostrarMenu():
    print('--- MENÚ HOJA DE CÁLCULO ---')
    print('1. Asignar valor a una celda')
    print('2. Ver la matriz de fórmulas')
    print('3. Ver la matriz normal')
    print('4. Salir')
def mostrarMatriz(matriz, titulo):
    print('')
    print((('--- ' + titulo) + ' ---'))
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    encabezado = '    '
    c = 0
    while (c < 10):
        encabezado = (encabezado + letras[c].rjust(6))
        c = (c + 1)
    print(encabezado)
    fila = 0
    while (fila < 10):
        linea = (str((fila + 1)).rjust(3) + ' ')
        col = 0
        while (col < 10):
            indice = ((fila * 10) + col)
            linea = (linea + str(matriz[indice]).rjust(6))
            col = (col + 1)
        print(linea)
        fila = (fila + 1)
    print('')
def evaluarCelda(entrada, matriz):
    if (entrada != ''):
        if entrada.startswith('='):
            print('-> ¡Fórmula detectada por el evaluador!')
            return 'CALC...'
    return entrada
def ejecutarSistema():
    matrizFormulas = []
    matrizNormal = []
    i = 0
    while (i < 100):
        matrizFormulas.append(' ')
        matrizNormal.append('0')
        i = (i + 1)
    print('Matriz 10x10 lista en memoria.')
    ejecutable = True
    opcion = ''
    while ejecutable:
        mostrarMenu()
        opcion = input('Elige una opción: ')
        if (opcion == '1'):
            print('\n--- ASIGNAR VALOR ---')
            fila_str = input('Ingresa la fila (1 a 10): ')
            col_str = input('Ingresa la columna (1 a 10, 1=A, 2=B...): ')
            valor = input('Ingresa el valor o fórmula: ')
            fila = int(fila_str)
            col = int(col_str)
            indice = (((fila - 1) * 10) + (col - 1))
            matrizFormulas[indice] = valor
            matrizNormal[indice] = evaluarCelda(valor, matrizNormal)
            print('¡Valor asignado correctamente!')
        elif (opcion == '2'):
            mostrarMatriz(matrizFormulas, 'MATRIZ DE FÓRMULAS')
        elif (opcion == '3'):
            mostrarMatriz(matrizNormal, 'MATRIZ NORMAL')
        elif (opcion == '4'):
            print('Cerrando la hoja de cálculo...')
            ejecutable = False
        else:
            print('Opción no válida.')