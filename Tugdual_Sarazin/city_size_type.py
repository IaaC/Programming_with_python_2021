from abc import ABC


class CitySizeType(ABC):
    @property
    def min_size(self) -> int:
        """

        :rtype: int
        """
        pass

    @property
    def name(self) -> str:
        """

        :rtype: str
        """
        pass


class MegaCity(CitySizeType):
    min_size = 10000000
    name = "Megacity"


class LargeMetropolitan(CitySizeType):
    min_size = 1500000
    name = "Large metropolitan"


class Metropolitan(CitySizeType):
    min_size = 500000
    name = "Metropolitan"


class MediumCity(CitySizeType):
    min_size = 500000
    name = "Medium city"


class SmallUrbanArea(CitySizeType):
    min_size = 0
    name = "Small urban area"
