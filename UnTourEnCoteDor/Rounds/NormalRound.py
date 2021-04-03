from Rounds.Round import Round


class NormalRound(Round):
    """
    Class of NormalRound extends Rounds for a ... Normal Round
    """
    def __init__(self, listTown,method):
        """
        Constructor of RandomRound

        The list of towns is calculate but the current used method
        :param listTown: a list of towns
        :type listTown: list
        """
        super().__init__(tour=listTown, method=method)