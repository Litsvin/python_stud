class Feature:
    def __init__(self, feature_type, prop_list, geometry):
        self.feature_type = feature_type
        self.prop_list = prop_list
        self.geometry = geometry

    def __str__(self):
        representation = 'Feature description: \n Feature type: {0}'.format(self.feature_type)
        representation = representation + '\n' + 'Feature properties: \n' + str(self.prop_list)
        representation = representation + '\n' + self.geometry.__str__()
        return representation
