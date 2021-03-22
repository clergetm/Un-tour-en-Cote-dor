from Rounds.Round import Round


class AscendingRound(Round):
    """
    Class of AscendingRound extends Rounds for a ... Ascending Round of Town
    """

    def __init__(self, listTown):
        """
        Constructor of  AscendingRound

        The constructor sort in the increasing order of the Number of the towns
        :param listTown: the list of towns
        :type listTown: list
        """
        # The temp dict and tour list are used to sort correctly the list
        temp = {}
        tour = []
        for i in range(0, len(listTown)):
            temp[listTown[i].getNumber()] = listTown[i]
        for i in sorted(temp):
            tour.append(temp[i])
        super().__init__(tour, "croissante")
