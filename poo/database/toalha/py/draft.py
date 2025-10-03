class Towel:
    def __init__(self, color: str, size: str): # construtor
        self.color: str = color # atributos
        self.size: str = size
        self.wetness: int = 0
    
    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.isMaxWetness():
            self.wetness = self.isMaxWetness()
            print("toalha encharcada")

    def isDry(self):
        return self.wetness == 0

    def wringOut(self):
        self.wetness = 0

    def isMaxWetness(self) -> int:
        if self.size == "P": # early return
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0 # default return

    def __str__(self) -> str: # toString
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

def main(): 
    towel: Towel = Towel("", "") # 2: criar um obj com qq valor inicial
    while True: # 3: loop infinito

        line: str = input() # 4: perguntar ao usuario
        print("$" + line) # echo
        args: list[str] = line.split(" ") # 5: separar argumentos

        if args[0] == "end":
            break
        elif args[0] == "criar": # color size
            color: str = args[1]
            size: str = args[2]
            towel = Towel(color, size)
        elif args[0] == "seca":
            print("sim" if towel.isDry() else "nao")
        elif args[0] == "torcer":
            towel.wringOut()
        elif args[0] == "enxugar":
            amount: int = int(args[1])
            towel.dry(amount)
        elif args[0] == "mostrar":
            print(towel)
        else: # 7: erro
            print("fail: comando não encontrado")

main() # passo 1
