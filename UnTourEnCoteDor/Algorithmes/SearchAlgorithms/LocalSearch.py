from Algorithmes.Algorithm import Algorithm


class LocalSearch(Algorithm):
    """
    Class LocalSearch extends Algorithms for the LocalSearch Algorithm (Algorithme Recherche Locale)
    """

    def __init__(self, towns, method):
        """
        Constructor of LocalSearch
        :param towns: the list of Towns
        :param method: the method used for this round
        :type towns: list
        :type method: str
        Initiate the Algorithm with the name "Recherche Locale"
        And the list with all the towns used
        """
        super().__init__("Recherche Locale", method)
        self.listTown = towns
        self.visited = []
