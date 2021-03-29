from Algorithmes.Algorithm import Algorithm
from Geography.Town import Town


class Greedy(Algorithm):
    """
    Class Greedy extends Greedy for the Greedy Algorithm (Algorithme Glouton)
    """

    def __init__(self, towns, method):
        """
        Constructor of Greedy

        :param towns: the list of Towns
        :param method: the method used for this round
        :type towns: list
        :type method: str
        Initiate the Algorithm with the name Glouton
            the listTown with all  towns used
            the visited dict with all towns non visited by default
        """
        super().__init__("Glouton", method)
        self.listTown = towns
        self.visited = {}
        for town in self.listTown:
            self.visited[town] = False

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

    def starting_Further_Towns(self) -> [Town, Town]:
        """
        Search the couple of further towns of listTown

        :return: A couple of Town
        :rtype: (Town, Town)
        """

        # Initialize variables
        distanceMax = 0
        v1 = None
        v2 = None

        # For each town of listTown
        for i in range(0, len(self.listTown)):
            # Selected town
            town = self.listTown[i]
            # List of other towns that the selected town
            towns = list(self.listTown)
            towns.remove(town)

            # For each town of towns
            for j in range(0, len(towns)):
                # Calculate distance between this town and the selected town
                distance = town.distance(towns[j])
                # If its value is greater than the previous distanceMax
                if distance > distanceMax:
                    # Change the answers
                    distanceMax = distance
                    v1 = town
                    v2 = towns[j]
        # Return both answers
        return v1, v2

    def Visited(self, town):
        self.visited[town] = True

    def AreAllVisited(self):
        """
        Check if there are still a non-visited town

        :return: True if all towns are visited
        :rtype: bool
        """
        if False in self.visited.values():
            return False
        return True
