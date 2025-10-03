import sys 

class Calculator:
    """
    Representa uma calculadora que consome bateria para realizar operações.
    """
    def __init__(self, batteryMax: int):
        """
        Inicializa a calculadora com uma capacidade máxima de bateria.
        """
        self.batteryMax = batteryMax
        self.battery = 0
        self.display = 0.0

    def __str__(self) -> str:
        """
        Retorna a representação da calculadora em formato de string.
        Exemplo: display = 0.00, battery = 0
        """
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def charge(self, increment: int):
        """
        Adiciona carga à bateria, sem ultrapassar o limite máximo.
        """
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a: float, b: float):
        """
        Soma dois números e armazena o resultado no display.
        Gasta 1 ponto de bateria.
        """
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        self.battery -= 1
        self.display = a + b

    def div(self, num: float, den: float):
        """
        Divide dois números e armazena o resultado no display.
        Gasta 1 ponto de bateria.
        Verifica se há bateria e se o denominador não é zero.
        """
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        if den == 0:
            print("fail: divisao por zero")
            return
        self.battery -= 1
        self.display = num / den

def main():
    """
    Função principal que processa os comandos do usuário.
    """
    calculator = None

    for line in sys.stdin:
        # Remove espaços em branco e quebras de linha
        command_line = line.strip()
        print(f"$ {command_line}")
        
        # Divide a linha em argumentos
        args = command_line.split(" ")
        command = args[0]

        if command == "end":
            break
        elif command == "init":
            # Cria a instância da calculadora com a bateria máxima
            calculator = Calculator(int(args[1]))
        elif calculator is None:
            # Garante que a calculadora foi inicializada
            print("fail: a calculadora precisa ser iniciada")
        elif command == "show":
            print(calculator)
        elif command == "charge":
            calculator.charge(int(args[1]))
        elif command == "sum":
            calculator.sum(float(args[1]), float(args[2]))
        elif command == "div":
            # O primeiro argumento é o numerador, o segundo é o denominador
            calculator.div(float(args[1]), float(args[2]))
        else:
            print("fail: comando invalido")

# Executa a função principal
if __name__ == "__main__":
    main()