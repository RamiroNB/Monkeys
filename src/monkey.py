class Monkey:
    def __init__(self, nome: str, cocos: list, par: "Monkey", impar: "Monkey"):
        self.nome = nome
        self.par = par
        self.impar = impar
        self.par_list = list()
        self.impar_list = list()
        self.qtd_par = 0
        self.qtd_inpar = 0
        for coco in cocos:
            coco = int(coco)
            if coco % 2 == 0:
                self.par_list.append(coco)
            else:
                self.impar_list.append(coco)
        self.qtd_par = len(self.par_list)
        self.qtd_inpar = len(self.impar_list)
        self.par_list.clear()
        self.impar_list.clear()

    def distribui(self):
        self.par.recebe_par(self.qtd_par)
        self.impar.recebe_impar(self.qtd_inpar)
        self.qtd_par = 0
        self.qtd_inpar = 0

    def recebe_par(self, num):
        # self.par_list.extend(list)
        self.qtd_par += num

    def recebe_impar(self, num):
        # self.impar_list.extend(list)
        self.qtd_inpar += num

    def __len__(self):
        return self.qtd_par + self.qtd_inpar
