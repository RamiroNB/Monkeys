
class Monkey:
    def init(self, cocos: list, par: 'Monkey',  inpar: 'Monkey'):
        self.cocos = cocos
        self.par = par
        self.inpar = inpar
 
    def distribui(self):
        for coco in self.cocos:
            if coco % 2 == 0:
                self.par.recebe(coco)
            else:
                self.inpar.recebe(coco)
                
        self.cocos.clear()

    def recebe(self, coco):
        self.cocos.append(coco)