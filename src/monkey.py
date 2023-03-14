
class Monkey:
    def __init__(self,nome:str, cocos: list, par: 'Monkey',  inpar: 'Monkey'):
        self.nome = nome
        self.cocos = cocos
        self.par = par
        self.inpar = inpar
        
 
    def distribui(self):
        for coco in self.cocos:
            if int(coco) % 2 == 0:
                self.par.recebe(coco)
            else:
                self.inpar.recebe(coco)

        self.cocos.clear()
        


    def recebe(self, coco):
        self.cocos.append(coco)
