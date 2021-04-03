from abc import ABC


class Algorithm(ABC):
    """
    Class "interface" of Algorithms
    """

    def __init__(self, name, method):
        """
        Constructor of Algorithm

        :param name: the Name of the Algorithm
        :param method: the method used for this round

        :type name: str
        :type method: str
        """

        self.name = str(name)
        self.method = str(method)

    def getName(self):
        """
        Getter of Name

        :return: the name of the Algorithm
        :rtype: str
        """
        return self.name

    def getMethod(self):
        """
        Getter of Method

        :return: the method of the Round of theAlgorithm
        :rtype: str
        """
        return self.method
