from abc import ABC
from Geography.Town import Town


class Round(ABC):
    """
    Class "abstract" of Rounds
    """

    def __init__(self, tour, method):
        """
        Constructor of Round

        :param tour: the round of towns done
        :param method: the method to obtain this round

        :type tour: list
        :type method: str
        """
        self.tour = tour
        self.type = method

    def __str__(self) -> str:
        """
        str method of Round

        :return: the method used for this round and the ordered list as a String
        :rtype: str
        """

        # Add the type of round
        res = "Tournée " + self.type

        # Add all values of the round
        res += " ["
        for town in self.tour:
            res += str(town.getNumber()) + ", "
        res = res[:-2]
        res += "]"
        res += "\nCost : " + str(self.cost())
        return res

    def cost(self) -> float:
        """
        Method that calculate the cost for the whole round

        :return res: the sums of distance between towns
        :rtype res: float

        .. seealso:: Town.distance(self, t2)
        """
        res = 0
        for i in range(0, len(self.tour) - 1):
            res += self.tour[i].distance(self.tour[i + 1])
        res += self.tour[0].distance(self.tour[len(self.tour) - 1])

        return res

    def getTour(self):
        """
        Getter of Tour
        :return: the tour list
        :rtype: list
        """
        return self.tour

    def setTour(self, newTour):
        """
        Setter of Tour
        :param newTour: the new tour list
        :type newTour: list
        """
        self.tour = newTour

    def getType(self):
        """
        Getter of Type
        :return: the type of the round
        :rtype: list
        """
        return self.type

    def getTown(self, i) -> Town:
        """
        Getter of Town
        :param i: an iterator
        :type i: int

        :return: the Town of the round at i
        :rtype: Town
        """
        return self.tour[i]
