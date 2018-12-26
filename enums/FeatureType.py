from enum import Enum

from CustomExceptions.UnsupportedOperationException import UnsupportedOperationException


class FeatureType(Enum):
    FEATURE = 'Feature'

    def define_by_name(self, string):
        if string == self.FEATURE:
            return self.FEATURE
        else:
            raise UnsupportedOperationException('Unsupported FeatureType: ' + string)
