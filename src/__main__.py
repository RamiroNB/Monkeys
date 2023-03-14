from .monkey import Monkey


# rounds.tamanhototaldaslistassomadas(velocidade da solução inicials)
def main():
    monkeys = []
    monkey_r_dict = dict()

    with open("casos/caso0050.txt") as f:
        lines = f.readlines()
        r = lines[0]
        lines.remove(r)
        r = r.split(" ")
        rounds = int(r[1])

        for line in lines:
            line = line.split(":")
            referencias = line[0]
            cocos = line[2]
            referencias = referencias.split(" ")
            # montar dict de referencias
            monkey_r_dict[referencias[1]] = [referencias[4], referencias[7]]
            # cria lista de cocos
            cocos = cocos.strip()
            cocos = cocos.split(" ")

            # cria monkey
            monkeys.append(
                Monkey(nome=referencias[1], cocos=cocos, par=None, inpar=None)
            )

        for monkey in monkeys:
            refs = monkey_r_dict[monkey.nome]
            monkey.par = monkeys[int(refs[0])]
            monkey.inpar = monkeys[int(refs[1])]

    #########################################################################################
    print("começou")
    # muito tempo
    for i in range(rounds):
        [monkey.distribui() for monkey in monkeys]

    print("acabou")
    # muito tempo
    idx_vencedor = -1
    vencedor = -10
    for i, moneky in enumerate(monkeys):
        if len(moneky) >= vencedor:
            idx_vencedor = i
            vencedor = len(moneky)

    print(monkeys[idx_vencedor].nome)
    print(len(monkeys[idx_vencedor]))


if __name__ == "__main__":
    main()

# ordenar as listas entre par e impar?
# lista par e lista inpar? e fa(dimimui considz só uma vez as ordenaçõeseravelmete o nmr de op)
# distribuir os inteiros de forma paralela????
# achar os que não são referenciados?
# achar os que ficam em 0 depois de algumas rodadas
# achar a rodada onde fica igual e não muda mais os tamahos das listas? (sim depois de 5 rodadas nada muda pro primeiro caso)
# pro segundo fica variando entre alguns valores especificos (e se botar o numeoro total de rodadas já nao roda)
# algo a mais para otimizar? (ultimo caso ainda lento)
# sera que o ultimo caso tem solução?

# montar o grapho e fazer operações?
