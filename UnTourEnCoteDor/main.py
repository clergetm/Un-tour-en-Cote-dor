# Press the green button in the gutter to run the script.
from Geography.Department import Department
from Rounds.RandomRound import RandomRound

if __name__ == '__main__':
    cotedor = Department("Instances/top70.txt")
    # # dijon.toString_listVille()
    #
    # list = []
    # for ville in dijon.listTown:
    #     list.append(ville.getNumber())
    #
    # tournee = Round(dijon.listTown, "croissante")
    #
    # print(tournee.__str__())
    # print(str(tournee.cout()))
    # tournee = RandomRound(dijon.listTown)
    # print(tournee.__str__())
    # print(tournee.cout())

    tournee = RandomRound(cotedor.listTown)
    coutmin = tournee.cost()
    strmin = tournee.__str__()
    for i in range(0, 100000):
        tournee = RandomRound(cotedor.listTown)
        couttemp = tournee.cost()
        if couttemp < coutmin:
            coutmin = couttemp
            strmin = tournee.__str__()

    print(strmin)
    print(coutmin)
