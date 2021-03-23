from Algorithmes.Algorithm import Algorithm


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
        And the list with all the towns used
        """
        super().__init__("Glouton",method)
        self.listTown = towns
        self.visited = []


