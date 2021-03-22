# Press the green button in the gutter to run the script.
from Algorithmes.Greedy import Greedy
from Geography.Department import Department
from Rounds.AscendingRound import AscendingRound
from Rounds.RandomRound import RandomRound

cotedor = Department("Instances/top70.txt")


def TP1(q):
    # TP1 Q2
    if q == 2:
        cotedor

    elif q == 3:
        print(cotedor.listTown[0].distance(cotedor.listTown[1]))

    elif q == 4:
        turn = AscendingRound(cotedor.listTown)
        print(turn)

    elif q == 5:
        turn = AscendingRound(cotedor.listTown)
        print(turn.cost())

    elif q == 6:
        turn = RandomRound(cotedor.listTown)
        coutmin = turn.cost()
        strmin = turn.__str__()
        for i in range(0, 100000):
            turn = RandomRound(cotedor.listTown)
            couttemp = turn.cost()
            if couttemp < coutmin:
                coutmin = couttemp
                strmin = turn.__str__()

        print(strmin)
        print(coutmin)


def TP2(q):
    if q == 1:
        turn = AscendingRound(cotedor.listTown)
        print(turn.__str__())
        print(turn.cost())

    elif q == 999:
        # Test de nearest_Town
        r = AscendingRound(cotedor.listTown)
        glouton = Greedy(r.getTour())

        resglouton = glouton.nearest_Town(glouton.listTown[0])
        # print(f"startingtown : {glouton.listTown[0].getName()}")
        # print(f"res glouton : {resglouton.getName()}")


if __name__ == '__main__':
    TP2(999)
    r = AscendingRound(cotedor.listTown)
    for town in r.getTour():
        print(town)
    print("-----------------------------------------")
    g = Greedy(r.getTour())
    for town in g.listTown:
        print(town)
