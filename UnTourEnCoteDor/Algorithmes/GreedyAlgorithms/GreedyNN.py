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
        self.visited.clear()  # it's might be an useless line
        self.visited.append(startingTown)
        # While each town arent visited
        while len(self.visited) < len(self.listTown):
            # Search for the nearest Town
            nextTown = self.nearest_Town(startingTown)
            self.visited.append(nextTown)
            R1.append(nextTown)
            startingTown = nextTown
        return Round(R1, self.getMethod())

    def nearest_Town(self, startingTown) -> Town:
        """
        get the nearest Town from startingTown
        :param startingTown: the Town where to begin
        :type startingTown: Town

        :return: the nearest Town
        :rtype: Town
        """
        # temp list without the starting town
        temp = list(self.listTown)

        # delete all visited town
        for town in self.visited:
            temp.remove(town)

        # Calculate all distances from startingTown
        cost = {}
        for town in temp:
            cost[town] = startingTown.distance(town)
        # return from the cost dict the min value -> Town
        return min(cost, key=cost.get)

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
