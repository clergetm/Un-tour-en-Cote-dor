from Algorithmes.Algorithm import Algorithm
from Geography.Town import Town


class Greedy(Algorithm):
    """
    Class Greedy extends Algorithm for the Greedy Algorithm (Algorithme Glouton)
    """

    def __init__(self, towns):
        """
        Constructor of Greedy

        :param towns: the list of Towns
        :type towns: list
        Initiate the Algorithm with the name Glouton
        And the list with all the towns used
        """
        super().__init__("Glouton")
        self.listTown = towns

    def nearest_Neighbor(self, startingTown):
        # Initiate the visited dict to False
        visited = {}
        for town in self.listTown:
            visited[town] = False

        T1 = [startingTown]
        visited[startingTown] = True
        while False in visited:
            next = self.nearest_Town(startingTown)

    def nearest_Town(self, startingTown) -> Town:
        print(len(self.listTown))
        listt = self.listTown
        listt.remove(startingTown)
        print(len(self.listTown))
        cost = {}
        for town in listt:
            cost[town] = startingTown.distance(town)
        t = min(cost, key=cost.get)
        print(f"min cost is \n{startingTown} \n{t} \n {startingTown.distance(t)}")
        return t
