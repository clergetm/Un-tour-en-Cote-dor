from random import shuffle
from Rounds.Round import Round


class RandomRound(Round):
    """
    Class of RandomRound extends Rounds for a ... Random Round
    """
    def __init__(self, listTown):
        """
        Constructor of RandomRound

        The list of towns is randomly shuffled before use
        :param listTown: a list of towns
        :type listTown: list
        """
        shuffle(listTown)  # shuffle the list of towns

        super().__init__(listTown, "aléatoire")
