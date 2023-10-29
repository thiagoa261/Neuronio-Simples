class Neuronio:
    entradas = None
    pesos = None
    limiar = 0
    taxa_aprendizado = 0.1

    def __init__(self, entradas = None, pesos = None):
        self.entradas = entradas
        self.pesos = pesos

    def soma(self):
        return sum([e1 * e2 for e1, e2 in zip(self.entradas, self.pesos)])

    def ativacao(self):
        return 1 if(self.soma() >= self.limiar) else 0

    def delta(self, desejada):
        return desejada - self.ativacao()

    def treino(self, entradas, pesos, desejadas):
        self.pesos = pesos
        epoch = 1
        while True:
            acertos = 0
            for i in range(len(desejadas)):
                self.entradas = entradas[i]
                if(self.ativacao() != desejadas[i]):
                    delta = self.delta(desejadas[i])
                    for j in range(len(self.pesos)):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * delta * self.entradas[j]
                else:
                    acertos += 1
            print("Epoca: ", epoch, " Erros: ", len(desejadas)-acertos)
            epoch += 1
            if acertos >= len(desejadas):
                break

if __name__ == "__main__":
    and_neur = Neuronio()
    and_neur.treino([[1,0,0], [1,0,1], [1,1,0], [1,1,1]], [0.1,-0.1,-0.1], [0,0,0,1])
    print("--------------------------------------")

    nand = Neuronio()
    nand.treino([[1,0,0], [1,0,1], [1,1,0], [1,1,1]], [0.1,-0.1,-0.1], [1,1,1,0])
    print("--------------------------------------")

    or_neur = Neuronio()
    or_neur.treino([[1,0,0], [1,0,1], [1,1,0], [1,1,1]], [0.1,-0.1,-0.1], [0,1,1,1])
    print("--------------------------------------")

    print("Neuronio treinado")