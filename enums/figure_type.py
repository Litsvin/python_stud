from enum import Enum

from CustomExceptions.UnsupportedOperationException import UnsupportedOperationException


class FigureType(Enum):
    POLYGON = 'Polygon'

    def define_by_name(self, string):
        if string == self.POLYGON:
            return self.POLYGON
        else:
            raise UnsupportedOperationException('Unsupported FigureType: ' + string)
