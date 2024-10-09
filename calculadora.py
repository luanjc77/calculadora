import math

class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtrai(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Divisão por zero não é permitida.")

    def potencia(self, a, b):
        return a ** b

    def raiz_quadrada(self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            raise ValueError("Raiz quadrada de número negativo não é permitida.")

def main():
    calc = Calculadora()
    
    a = float(input("Digite o primeiro número: "))

    print("Operações disponíveis: ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    
    operacao = int(input("Escolha a operação (1-6): "))
    
    if operacao in [1, 2, 3, 4, 5]:
        b = float(input("Digite o segundo número: "))
        
        if operacao == 1:
            resultado = calc.soma(a, b)
        elif operacao == 2:
            resultado = calc.subtrai(a, b)
        elif operacao == 3:
            resultado = calc.multiplica(a, b)
        elif operacao == 4:
            resultado = calc.divide(a, b)
        elif operacao == 5:
            resultado = calc.potencia(a, b)
    elif operacao == 6:
        resultado = calc.raiz_quadrada(a)
    else:
        print("Operação inválida.")
        return
    
    print(f"O resultado é: {resultado}")

if __name__ == "__main__":
    main()
