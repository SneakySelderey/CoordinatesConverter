from sys import argv
from coordinate_systems import *

def main():
    inputSystem = 'None'
    outputSystem = 'None'
    dimensions = None
    coordinates = []
    rounding = 2

    availableSystems = {
        'cartesian': CartesianCoordinates,
        'polar': PolarCoordinates,
        'cylindrical': CylindricalCoordinates,
        'spherical': SphericalCoordinates
    }

    i = 0
    for i in range(1, len(argv)):
        if argv[i][0] == '-':
            if (argv[i] in ['-f', '--from']):
                inputSystem = argv[i + 1]

            elif argv[i] in ['-t', '--to']:
                outputSystem = argv[i + 1]

            elif argv[i] in ['-d', '--dimensions']:
                dimensions = int(argv[i + 1])
            
            elif argv[i] in ['-r', '--round']:
                rounding = int(argv[i + 1])
        else:
            if argv[i - 1][0] != '-':
                coordinates.append(float(argv[i]))

    if len(coordinates) != dimensions:
        raise Exception('Number of specified coordinated does not match specified number of dimensions')

    inputSystemObj = availableSystems[inputSystem](dimensions, coordinates, rounding)
    outputSystemObj = 'Error: one of specifies coordinate systems is not supported or does not exist'

    if outputSystem == 'cartesian':
            outputSystemObj = inputSystemObj.ToCartesianCoordinates()
    if outputSystem == 'polar':
            outputSystemObj = inputSystemObj.ToPolarCoordinates()
    if outputSystem == 'cylindrical':
            outputSystemObj = inputSystemObj.ToCylindricalCoordinates()
    if outputSystem == 'spherical':
            outputSystemObj = inputSystemObj.ToSphericalCoordinates()

    print(outputSystemObj)

    return

if __name__ == "__main__":
    main()
