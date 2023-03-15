class Monkey:
    def __init__(self, nome: str, cocos: list, par: "Monkey", impar: "Monkey"):
        self.nome = nome
        self.cocos = cocos
        self.par = par
        self.impar = impar
        self.par_list = list()
        self.impar_list = list()
        for coco in cocos:
            coco = int(coco)
            if coco % 2 == 0:
                self.par_list.append(coco)
            else:
                self.impar_list.append(coco)
        self.cocos.clear()

    def distribui(self):
        self.par.recebe_par(self.par_list)
        self.impar.recebe_impar(self.impar_list)
        self.par_list.clear()
        self.impar_list.clear()

    def recebe_par(self, list):
        self.par_list.extend(list)

    def recebe_impar(self, list):
        self.impar_list.extend(list)

    def __len__(self):
        return len(self.par_list) + len(self.impar_list)
