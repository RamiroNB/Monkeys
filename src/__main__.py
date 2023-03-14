from .monkey import Monkey
#rounds.tamanhototaldaslistassomadas(velocidade da solução inicials)
def main():
    monkeys = []
    monkey_r_dict = dict()

    with open("casos/caso0100.txt") as f:
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

    rounds = 10000
    #muito tempo
    for i in range(rounds):
        for monkey in monkeys:
            monkey.distribui()
    print("acabou")
    #muito tempo
    vencedor = -10
    for moneky in monkeys:
       print(len(moneky.cocos))
       if len(moneky.cocos) >= vencedor:
           vencedor = len(moneky.cocos)
        
    
    print(vencedor)

if __name__ == "__main__":
    main()

#ordenar as listas entre par e impar?
#achar os que não são referenciados?
#achar os que ficam em 0 depois de algumas rodadas
#achar a rodada onde fica igual e não muda mais os tamahos das listas? (sim depois de 5 rodadas nada muda pro primeiro caso)
#pro segundo fica variando entre alguns valores especificos 
#algo a mais para otimizar? (ultimo caso ainda lento)
#sera que o ultimo caso tem solução?