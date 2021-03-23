# Press the green button in the gutter to run the script.
from Algorithmes.GreedyAlgorithms.Greedy import Greedy
from Algorithmes.GreedyAlgorithms.GreedyNN import GreedyNN
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

    if q == 2:
        r = AscendingRound(cotedor.listTown)
        glouton = GreedyNN(r.getTour())
        #  res = glouton.nearest_Neighbor(glouton.listTown[0])
        res = glouton.best_Nearest_Neighbor()
        print(res)

    elif q == 999:
        # Test de nearest_Town
        r = AscendingRound(cotedor.listTown)
        glouton = Greedy(r.getTour())
        glouton.visited.append(glouton.listTown[0])
        glouton.visited.append(glouton.listTown[3])
        resglouton = glouton.nearest_Town(glouton.listTown[0])
        print(f"startingtown : {glouton.listTown[0].getName()}")
        print(f"res glouton : {resglouton.getName()}")

        start = r.getTour()[0]
        coutmin = 100000000000000000000000000000
        villemin = 'aucune'
        for i in range(1, len(r.getTour())):
            tempcout = start.distance(r.getTour()[i])
            if tempcout < coutmin:
                coutmin = tempcout
                villemin = r.getTour()[i].getName()
        print(f"resultat : {villemin} : {coutmin}")


if __name__ == '__main__':
    TP2(2)



