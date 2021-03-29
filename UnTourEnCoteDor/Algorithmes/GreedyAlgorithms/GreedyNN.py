from Algorithmes.GreedyAlgorithms.Greedy import Greedy
from Geography.Town import Town
from Rounds.Round import Round


class GreedyNN(Greedy):
    """
    Class GreedyNN extends Greedy for the Nearest Neighbor Greedy Algorithm
    """

    def __init__(self, towns):
        """
        Constructor of GreedyNN

        :param towns: the list of towns
        :type towns: list
        """
        super().__init__(towns, "gloutonne \"plus proche voisin\"")

    def nearest_Neighbor(self, startingTown) -> Round:
        """
        Calculate the round from startingTown to it's nearest neighbors

        :param startingTown: the Town where to begin
        :type startingTown: Town

        :return: A Round made of nearest Neighbor
        :rtype: Round

        .. seealso:: nearest_Town(self, startingTown)
        """

        # Initialise the list of the Round and the visited list
        R1 = [startingTown]
        self.Visited(startingTown)
        # While each town arent visited
        while not self.AreAllVisited():
            # Search for the nearest Town
            nextTown = self.nearest_Town(startingTown)
            self.Visited(nextTown)
            R1.append(nextTown)
            startingTown = nextTown
        return Round(R1, self.getMethod())

    def best_Nearest_Neighbor(self) -> Round:
        """
        Calculate the round for each town as a starting point and return the best one

        :return: The best Round
        :rtype: Round

        .. seealso:: nearest_Neighbor(self, startingTown)
        """
        rounds = {}
        for town in self.listTown:
            r = self.nearest_Neighbor(town)
            rounds[r] = r.cost()

        return min(rounds, key=rounds.get)
