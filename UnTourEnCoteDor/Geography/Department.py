from Geography.Town import Town


class Department:
    """
    Class that contains all the towns of the project
    """

    def __init__(self, file):
        """
        Constructor of Department

        Initialize the list of Towns with all the towns from a file

        :param file: the file where we get all the towns like 'name_of_file.txt'
        :type file: str
        """
        self.listTown = []

        # Open the file and insert each line as a town in the list
        with open(file, "r", encoding='utf-8') as file:
            lines = file.read().splitlines()
            for line in lines:
                infoV = line.split()
                self.listTown.append(Town(infoV))

    def __str__(self):
        """
        str method for all towns

        :return: the list of all towns informations
        :rtype: str
        .. seealso:: town.__str__()
        """
        res = ""
        for town in self.listTown:
            res += town.__str__()+"\n"
        return res

    def getTown(self, i) -> Town:
        """
        Getter for a specific town with this number saved

        :param i: the number of the Town
        :type i: int
        :return: the town with this number or nothing if nothing found
        :rtype: Town
        """
        for j in range(0, len(self.listTown)):
            if j == self.listTown[i].getNumber():
                return self.listTown[i]

            return
