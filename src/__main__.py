from .monkey import Monkey
#rounds.tamanhototaldaslistassomadas
def main():
    monkeys = []
    monkey_r_dict = dict()

    with open("casos/caso1000.txt") as f:
        lines = f.readlines()
        r = lines[0]
        lines.remove(r)
        r = r.split(" ")
        rounds = int(r[1])
        
        for line in lines:
            line = line.split(":")
            referencias = line[0]
            cocos = line [2]
            referencias = referencias.split(" ")
            #montar dict de referencias
            monkey_r_dict[referencias[1]]= [referencias[4], referencias[7]]
            #cria lista de cocos
            cocos =cocos.strip()
            cocos = cocos.split(" ")

            #cria monkey
            monkeys.append(Monkey(nome=referencias[1],cocos=cocos, par=None, inpar=None))
        
            #0 cria macacos
            #1 tam vetor 
            #numeros
        #print(monkey_r_dict)
        for monkey in monkeys:
            refs =monkey_r_dict[monkey.nome]
            monkey.par = monkeys[int(refs[0])]
            monkey.inpar = monkeys[int(refs[1])]
            #print(f"{monkey.nome} {monkey.par.nome} {monkey.inpar.nome}")
    #muito tempo
    for i in range(rounds):
        for monkey in monkeys:
            monkey.distribui()
    
if __name__ == "__main__":
    main()