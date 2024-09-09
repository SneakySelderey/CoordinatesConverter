from coordinate_system_interface import CoordinateSystem
from math import sqrt, atan2, atan, cos, sin, pi

class CartesianCoordinates(CoordinateSystem):
    def __init__(self, dimensionsNumberInp, coordinatesInp, roundingInp) -> None:
        super().__init__(dimensionsNumberInp, coordinatesInp, roundingInp)

    def ToCartesianCoordinates(self):
        return self

    def ToPolarCoordinates(self):
        if self.dimensionsNumber != 2:
            raise Exception('Cannot create polar coordinates with other than two dimensions')

        r = sqrt(self.coordinates[0] ** 2 + self.coordinates[1] ** 2)
        phi = atan2(self.coordinates[1], self.coordinates[0])

        return PolarCoordinates(2, [r, phi], self.rounding)

    def ToCylindricalCoordinates(self):
        r = sqrt(self.coordinates[0] ** 2 + self.coordinates[1] ** 2)
        phi = atan2(self.coordinates[1], self.coordinates[0])
        h = self.coordinates[2]

        return CylindricalCoordinates(3, [r, phi, h], self.rounding)

    def ToSphericalCoordinates(self):
        p = sqrt(self.coordinates[0] ** 2 + self.coordinates[1] ** 2 + self.coordinates[2] ** 2)
        phi = atan(self.coordinates[1] / self.coordinates[0])
        theta = atan(sqrt(self.coordinates[0] ** 2 + self.coordinates[1] ** 2) / self.coordinates[2])

        return SphericalCoordinates(3, [p, phi, theta], self.rounding)

    def __str__(self):
        string = 'Cartesian coordinates (x, y, z): '

        for i in range(self.dimensionsNumber):
            string += str(round(self.coordinates[i], self.rounding)) + ' '

        return string


class CylindricalCoordinates(CoordinateSystem):
    def __init__(self, dimensionsNumberInp, coordinatesInp, roundingInp) -> None:
        if dimensionsNumberInp != 3:
            raise Exception('Cannot create cylindrical coordinates with other than three dimensions')

        if not (0 < coordinatesInp[1] < pi and coordinatesInp[0] > 0):
            raise Exception('Some conditions for cylindrical coordinate system are broken')
        
        super().__init__(dimensionsNumberInp, coordinatesInp, roundingInp)

    def ToCartesianCoordinates(self):
        x = self.coordinates[0] * cos(self.coordinates[1])
        y = self.coordinates[0] * sin(self.coordinates[1])
        z = self.coordinates[2]

        return CartesianCoordinates(3, [x, y, z], self.rounding)

    def ToPolarCoordinates(self):
        raise Exception('Cannot convert cylindrical coordinates to polar ones')

    def ToCylindricalCoordinates(self):
        return self

    def ToSphericalCoordinates(self):
        return self.ToCartesianCoordinates().ToSphericalCoordinates()

    def __str__(self):
        return f'Cylindrical coordinates (r, phi, h): {round(self.coordinates[0], self.rounding)} {round(self.coordinates[1], self.rounding)} {round(self.coordinates[2], self.rounding)}'


class PolarCoordinates(CoordinateSystem):
    def __init__(self, dimensionsNumberInp, coordinatesInp, roundingInp) -> None:
        if dimensionsNumberInp != 2:
            raise Exception('Cannot create polar coordinates with other than two dimensions')

        if not (0 < coordinatesInp[1] < pi and coordinatesInp[0] > 0):
            raise Exception('Some conditions for polar coordinate system are broken')
        
        super().__init__(dimensionsNumberInp, coordinatesInp, roundingInp)

    def ToCartesianCoordinates(self):
        x = self.coordinates[0] * cos(self.coordinates[1])
        y = self.coordinates[0] * sin(self.coordinates[1])

        return CartesianCoordinates(2, [x, y], self.rounding)

    def ToPolarCoordinates(self):
        return self

    def ToCylindricalCoordinates(self):
        raise Exception('Cannot convert polar coordinates to cylindrical ones')

    def ToSphericalCoordinates(self):
        raise Exception('Cannot convert polar coordinates to spherical ones')

    def __str__(self):
        return f'Polar coordinates (r, phi): {round(self.coordinates[0], self.rounding)} {round(self.coordinates[1], self.rounding)}'


class SphericalCoordinates(CoordinateSystem):
    def __init__(self, dimensionsNumberInp, coordinatesInp, roundingInp) -> None:
        if dimensionsNumberInp != 3:
            raise Exception('Cannot create spherical coordinates with other than three dimensions')
        
        if not (-pi < coordinatesInp[1] < pi and 0 < coordinatesInp[2] < pi and coordinatesInp[0] > 0):
            raise Exception('Some conditions for spherical coordinate system are broken')
        
        super().__init__(dimensionsNumberInp, coordinatesInp, roundingInp)

    def ToCartesianCoordinates(self):
        x = self.coordinates[0] * cos(self.coordinates[2]) * sin(self.coordinates[1])
        y = self.coordinates[0] * sin(self.coordinates[2]) * sin(self.coordinates[1])
        z = self.coordinates[0] * cos(self.coordinates[1])

        return CartesianCoordinates(3, [x, y, z], self.rounding)

    def ToPolarCoordinates(self):
        raise Exception('Cannot convert spherical coordinates to polar ones')

    def ToCylindricalCoordinates(self):
        temp = self.ToCartesianCoordinates()
        return temp.ToCylindricalCoordinates()

    def ToSphericalCoordinates(self):
        return self

    def __str__(self):
        return f'Spherical coordinates (r, phi, theta): {round(self.coordinates[0], self.rounding)} {round(self.coordinates[1], self.rounding)} {round(self.coordinates[2], self.rounding)}'
