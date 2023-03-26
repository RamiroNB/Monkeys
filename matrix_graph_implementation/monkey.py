

def main():
    monkeys_r_dict = dict()
    with open("casos/caso1000.txt") as f:
        lines = f.readlines()
        r = lines[0]
        lines.remove(r)
        r = r.split(" ")
        rounds = int(r[1])
        monkeys = []*len(lines)
        i = 0
        for line in  lines:
            monkeys.append([0]*4)
            line = line.split(":")
            referencias = line[0]
            cocos = line[2]
            referencias = referencias.split(" ")
            # cria lista de cocos
            cocos = cocos.strip()
            cocos = cocos.split(" ")
            qtd_pares = 0
            qtd_impares = 0
            # cria monkey
            #referencia par
            monkeys[i][0] = int(referencias[4])
            #print(monkeys[i][0])
            #referencia impar
            monkeys[i][1] = int(referencias[7])

            for coco in cocos:
                coco = int(coco)
                if coco % 2 == 0:
                   qtd_pares = qtd_pares + 1
                else:
                    qtd_impares = qtd_impares + 1
            monkeys[i][2] = qtd_pares
            monkeys[i][3] = qtd_impares
            i = i+1
            
    #########################################################################################
    for round in range(rounds):
        for i in range(len(monkeys)):
            monkeys[monkeys[i][0]][2] = monkeys[monkeys[i][0]][2] + monkeys[i][2]
            monkeys[i][2]=0
            monkeys[monkeys[i][1]][3] = monkeys[monkeys[i][1]][3] = monkeys[i][3]
            monkeys[i][3] = 0


    idx_vencedor = -1
    vencedor = -10
    for i, monkey in enumerate(monkeys):
        if monkey[2]+monkey[3] >= vencedor:
            idx_vencedor = i
            vencedor = monkey[2]+monkey[3]

    print(idx_vencedor)
    print(vencedor)


if __name__ == "__main__":
    main()
