# Press the green button in the gutter to run the script.
from Algorithmes.GreedyAlgorithms.Greedy import Greedy
from Algorithmes.GreedyAlgorithms.GreedyFI import GreedyFI
from Algorithmes.GreedyAlgorithms.GreedyNI import GreedyNI
from Algorithmes.GreedyAlgorithms.GreedyNN import GreedyNN
from Algorithmes.SearchAlgorithms.SearchEC import SearchEC
from Geography.Department import Department
from Rounds.AscendingRound import AscendingRound
from Rounds.RandomRound import RandomRound

cotedor = Department("Instances/top70.txt")


def TP1(q):
    # TP1 Q2
    if q == 2:
        print(cotedor)

    elif q == 3:
        print(cotedor.listTown[0].distance(cotedor.listTown[1]))

    elif q == 4:
        turn = AscendingRound(cotedor.listTown)
        print(turn)

    elif q == 5:
        turn = AscendingRound(cotedor.listTown)
        print(turn.cost())

    elif q == 6:
        # Prend un peu de temps à l'execution
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
        # Validation TP1
        turn = AscendingRound(cotedor.listTown)
        print(turn)

    if q == 2 or q == 3:
        # Validation Méthode Gloutonne plus proche voisin
        r = AscendingRound(cotedor.listTown)
        glouton = GreedyNN(r.getTour())
        res = glouton.greedyMethod(glouton.listTown[0])
        # res = glouton.best_Nearest_Neighbor()
        print(res)

    if q == 4:
        # Validation Méthode Gloutonne insertion proche
        r = AscendingRound(cotedor.listTown)
        glouton = GreedyNI(r.getTour())
        res = glouton.greedyMethod()
        print(res)

    if q == 5:
        # Validation Méthode Gloutonne insertion plus loin
        r = AscendingRound(cotedor.listTown)
        glouton = GreedyFI(r.getTour())
        res = glouton.greedyMethod()
        print(res)
    if q == 6:
        # Comparaison des résultats obtenus
        r = AscendingRound(cotedor.listTown)
        gloutonNN = GreedyNN(r.getTour())
        res = gloutonNN.best_Nearest_Neighbor()
        print(res)
        TP2(4)

    # elif q == 999:
    #     # Test de nearest_Town
    #     r = AscendingRound(cotedor.listTown)
    #     glouton = Greedy(r.getTour())
    #     glouton.visited.append(glouton.listTown[0])
    #     glouton.visited.append(glouton.listTown[3])
    #     resglouton = glouton.nearest_Town(glouton.listTown[0])
    #     print(f"startingtown : {glouton.listTown[0].getName()}")
    #     print(f"res glouton : {resglouton.getName()}")
    #
    #     start = r.getTour()[0]
    #     coutmin = 100000000000000000000000000000
    #     villemin = 'aucune'
    #     for i in range(1, len(r.getTour())):
    #         tempcout = start.distance(r.getTour()[i])
    #         if tempcout < coutmin:
    #             coutmin = tempcout
    #             villemin = r.getTour()[i].getName()
    #     print(f"resultat : {villemin} : {coutmin}")


def TP3(q):
    r = AscendingRound(cotedor.listTown)

    if q == 1:
        TP2(1)

    if q == 2 or q == 3:
        # Correspond aussi à la Q3
        glouton = GreedyNN(r.getTour())
        res = glouton.greedyMethod(glouton.listTown[0])
        print(res)

    if q == 4:
        # Recherche locale
        glouton = GreedyNN(r.getTour())
        tour = glouton.greedyMethod(glouton.listTown[0])
        search = SearchEC(tour)
        res = search.Local_Search()
        print(res)


def TP4(q):
    r = AscendingRound(cotedor.listTown)

    if q == 1:
        # la tournée croissante et  son cout.
        TP2(1)

    if q == 2:
        # tournée plus_proche_voisin(1) + son cout
        TP3(2)

    if q == 3:
        # recherche locale : Tournée + cout de la tournée
        TP3(4)


if __name__ == '__main__':
    TP3(4)



