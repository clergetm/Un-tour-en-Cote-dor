class Algorithm:
    """
    Class "abstract" of Algorithms
    """

    def __init__(self,name):
        """
        Constructor of Algorithm

        :param name: the Name of the Algorithm
        :type name: str
        """
        self.name = str(name)

    def getName(self):
        """
        Getter of Name
        :return: the name of the Algorithm
        :rtype: str
        """
        return self.name
