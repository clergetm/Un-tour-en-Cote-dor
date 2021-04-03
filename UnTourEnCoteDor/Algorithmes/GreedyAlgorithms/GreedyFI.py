from Algorithmes.GreedyAlgorithms.Greedy import Greedy
from Rounds.NormalRound import NormalRound


class GreedyFI(Greedy):
    """
    Class GreedyNI extends Greedy for the Farest Insertion Greedy Algorithm
    """

    def __init__(self, towns):
        """
        Constructor of GreedyNI

        :param towns: the list of towns
        :type towns: list
        """
        super().__init__(towns, "gloutonne \"insertion loin\"")

    def greedyMethod(self) -> NormalRound:
        """
        Calculate the tour of the two most distant towns with the other more distant towns

        :return: A round made up of the neighbor furthest from the other two starting towns
        :rtype: Round

        .. seealso:: starting_Further_Towns(self)
        """
        record = {}
        # Get the two most distant towns
        v1, v2 = self.starting_Further_Towns()
        # add both to the visited list and the round list
        R3 = [v1, v2]
        self.visited = [v1, v2]
        # While all town aren't visited
        while len(set(self.listTown).difference(self.visited)) > 0:
            # clear the record
            record.clear()
            # for each town unvisited
            for town in set(self.listTown).difference(self.visited):
                # get the distance from all town already visited
                for i in range(0, len(R3)):
                    # calculate the distance between the town and others around it
                    dist = R3[i].distance(town) + \
                           town.distance(R3[(i + 1) % len(R3)]) - \
                           R3[i].distance(R3[(i + 1) % len(R3)])
                    # register the information
                    record[dist] = [town, i]

            # get the best town and iterator from the best distance value
            best = record.get(max(record))


            # Insert at the ite + 1 % len(R2) the best town :
            # It insert at the beginning when the ite is the last one of R2
            R3.insert((best[1] + 1) % len(R3), best[0])
            self.visited.append(best[0])

        return NormalRound(R3, "insertion loin")

