import math


class Town:
    """
    Class Town that contains all the information about a town
    """
    def __init__(self, num, name, la, lo):
        """
        Constructor of Town with all values

        :param num: the number of the town
        :param name: the name of the town
        :param la: the latitude of the town
        :param lo: the longitude of the town

        :type num: int
        :type name: str
        :type la: float
        :type lo: float
        """
        self.number = int(num)
        self.name = str(name)
        self.latitude = float(la)
        self.longitude = float(lo)

    def __init__(self, listV):
        """
        Constructor of Town with a list of values


        :param listV: the list of value
        :type listV: list
        """
        self.number = int(listV[0])
        self.name = str(listV[1])
        self.latitude = float(listV[2])
        self.longitude = float(listV[3])

    def __str__(self) -> str:
        """
        str method of Town

        return a string composed of the values of a town
        example :  1 DIJON 47.3167 5.01667

        :return: the full str of values of a Town
        :rtype: str
        """
        return str(self.number) + " " + self.name + " " + str(self.latitude) + " " + str(self.longitude)

    def distance(self, t2) -> float:
        """
        Calculate the distance between two towns

        :param t2: the Second town which is used to get Longitude and Latitude
        :type t2: Town

        :return: the calculated distance
        :rtype: float
        """
        x1 = math.radians(self.getLongitude())
        y1 = math.radians(self.getLatitude())
        x2 = math.radians(t2.getLongitude())
        y2 = math.radians(t2.getLatitude())
        r = 6371
        return abs(r * math.acos((math.sin(y1) * math.sin(y2)) + (math.cos(y1) * math.cos(y2) * math.cos(x1 - x2))))

    def toString_distance(self, t2) -> str:
        """
        Return a printable version of the calcul of distance

        :param t2: the Second town which is used to get Longitude and Latitude
        :type t2: Town

        :return: the full str of distance and more text
        :rtype: str

        .. seealso:: self.distance(self,t2)
        """
        return "distance entre ville 1 et ville 2 : " + self.distance(t2) + " km"

    def getNumber(self) -> int:
        """
        Getter of Number

        :return: the number of the Town
        :rtype: int
        """
        return self.number

    def getName(self) -> str:
        """
        Getter of Name

        :return: the name of the Town
        :rtype: str
        """
        return self.name

    def getLatitude(self) -> float:
        """
        Getter of Latitude

        :return: the latitude of the Town
        :rtype: float
        """
        return self.latitude

    def getLongitude(self) -> float:
        """
        Getter of Longitude

        :return: the longitude of the Town
        :rtype: float
        """
        return self.longitude
