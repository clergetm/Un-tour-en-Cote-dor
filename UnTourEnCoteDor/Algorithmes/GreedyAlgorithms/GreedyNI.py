from Algorithmes.GreedyAlgorithms.Greedy import Greedy
from Geography.Town import Town
from Rounds.Round import Round


class GreedyNI(Greedy):
    """
    Class GreedyNI extends Greedy for the Nearest Insertion Greedy Algorithm
    """

    def __init__(self, towns):
        """
        Constructor of GreedyNI

        :param towns: the list of towns
        :type towns: list
        """
        super().__init__(towns, "gloutonne \"insertion proche\"")

    def Nearest_Insertion(self):
        """
        Calculate the round from the two further towns



        :return: A Round made of nearest Neighbor from the two further starting towns
        :rtype: Round

        .. seealso:: starting_Further_Towns(self)
        .. seealso:: nearest_Town_From_List(self, roundList)
        """
        v1, v2 = self.starting_Further_Towns()
        self.Visited(v1)
        self.Visited(v2)
        print(f"v1 : {v1} et v2 : {v2}")
        R2 = [v1, v2]
        while not self.AreAllVisited():
            pass

        return R2

    def nearest_Town_From_List(self, roundList) -> Town:
        """
        Found the nearest town for all the town of roundList

        :param roundList:

        :type roundList: list
        :return: the nearest town
        :rtype: Town


        """
        cost = {}
        for i in range(0, len(roundList)-1):
            town = self.nearest_Town(roundList[i])
            cost[town] = \
                float(roundList[i].distance(town))+\
                float(town.distance(roundList[i+1]))-\
                float(roundList[i].distance(roundList[i+1]))

        # return from the cost dict the min value -> Town
        return min(cost, key=cost.get)
