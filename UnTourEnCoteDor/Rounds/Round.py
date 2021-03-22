class Round:
    """
    Class "abstract" of Rounds
    """

    def __init__(self, tour, method):
        """
        Constructor of Round

        :param tour: the round of towns done
        :param method: the method to obtain this round
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