from pymysql.cursors import Cursor

from Algorithmes.SearchAlgorithms.LocalSearch import LocalSearch
from Geography.Town import Town
from Rounds.Round import Round


class SearchEC(LocalSearch):
    """
    Class SearchEC extends LocalSearch with exchange of successors
    """

    def __init__(self, towns):
        """
        Constructor of SearchEC

        :param towns: the list of towns
        :type towns: list
        """
        super().__init__(towns, "\" Echange de successeurs\"")

    def Local_Search(self) -> Round:
        CurrentR = self.listTown
        Finished = False
        while not Finished:
            Finished = True
            NeighborR = self.ff_Principle(CurrentR)
            if NeighborR.cost() < CurrentR.cost():
                CurrentR = Round(NeighborR.getTour(), NeighborR.getType())
                Finished = False
        return CurrentR

    def ff_Principle(self, CurrentR) -> list:
        tour = list(CurrentR.getTour())
        for i in range(1, len(tour) - 2):
            dist1 = tour[i - 1].distance(tour[i]) + \
                    tour[i + 1].distance(tour[i + 2])
            dist2 = tour[i - 1].distance(tour[i + 1]) + \
                    tour[i].distance(tour[i + 2])
            if dist1 > dist2:
                tour = self.Change(tour, i, i + 1)
        return Round(tour, "Première d'abord")

    # def bf_Principle(self,CurrentR) -> Round:
    #     r = CurrentR.getTour()
    #     for i in range(0,len(r)):
    #         rNeighbor = self.Change(CurrentR, i, i+1)

    @staticmethod
    def Change(l, T1, T2) -> list:
        l[T1], l[T2] = l[T2], l[T1]
        return l
