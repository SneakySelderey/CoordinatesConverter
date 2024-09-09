class CoordinateSystem:
    dimensionsNumber = 0
    coordinates = []
    rounding = 2

    def __init__(self, dimensionsNumberInp, coordinatesInp, roundingInp) -> None:
        if (dimensionsNumberInp != len(coordinatesInp)):
            raise Exception('Number of specified coordinated does not match specified number of dimensions')

        self.dimensionsNumber = dimensionsNumberInp
        self.coordinates = coordinatesInp
        self.rounding = roundingInp
