from Algorithmes.GreedyAlgorithms.Greedy import Greedy
from Geography.Town import Town
from Rounds.NormalRound import NormalRound


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

    def greedyMethod(self, startingTown) -> NormalRound:
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
        self.visited.clear()
        self.visited.append(startingTown)
        # While each town arent visited
        while len(self.visited) < len(self.listTown):
            # Search for the nearest Town
            nextTown = self.nearest_Town(startingTown)
            self.visited.append(nextTown)
            R1.append(nextTown)
            startingTown = nextTown
        return NormalRound(R1, self.getMethod())

    def best_Nearest_Neighbor(self) -> NormalRound:
        """
        Calculate the round for each town as a starting point and return the best one
        :return: The best Round
        :rtype: Round
        .. seealso:: nearest_Neighbor(self, startingTown)
        """
        self.method = "gloutonne \"best plus proche voisin\""
        rounds = {}
        for town in self.listTown:
            r = self.greedyMethod(town)
            rounds[r] = r.cost()
        return min(rounds, key=rounds.get)
