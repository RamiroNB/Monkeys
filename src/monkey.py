class Monkey:
    def __init__(self, nome: str, cocos: list, par: "Monkey", impar: "Monkey"):
        self.par_parent = None
        self.impar_parent = None
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
        # for coco in self.cocos:
        #     if int(coco) % 2 == 0:
        #         self.par.recebe(coco)
        #     else:
        #         self.impar.recebe(coco)
        self.par_list.clear()
        self.impar_list.clear()

    def recebe_par(self, list):
        self.par_list.extend(list)
        # self.cocos.append(coco)

    def recebe_impar(self, list):
        self.impar_list.extend(list)

    def __len__(self):
        return len(self.par_list) + len(self.impar_list)

    def suicide(self):
        self.par.par_parent = None
        self.impar.impar_parent = None

    def __str__(self) -> str:
        return f"Monkey(Name:{self.nome}, Len:{len(self)}, ParParent:{self.par_parent if self.par_parent is None else 'another-monkey'},ImParent:{self.impar_parent if self.impar_parent is None else 'another-monkey'}, par={self.par if self.par is None else 'another-monkey'},impar={self.par if self.par is None else 'another-monkey'})"
