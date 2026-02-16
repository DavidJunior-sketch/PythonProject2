numero1 = float(input('insira o primero numero:'))
numero2 = float(input('insira o segundo numero:'))

opcoes = int(input(' 1-soma \n 2-subtracao \n 3-multiplicacao \n 4-Divisao \n escolha uma das opcoes:'))

match opcoes:
    case 1:
        resultado = numero1 + numero2
        print("{:.2f}".format(resultado))
    case 2:
        resultado = numero1 - numero2
        print("{:.2f}".format(resultado))
    case 3:
        resultado = numero1*numero2
        print("{:.2f}".format(resultado))
    case 4:
        resultado = numero1 / numero2
        print("{:.2f}".format(resultado))