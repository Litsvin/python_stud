class Feature:
    def __init__(self, feature_type, prop_list, geometry):
        self.feature_type = feature_type
        self.prop_list = prop_list
        self.geometry = geometry

    def get_feature_type(self):
        return self.feature_type

    def get_prop_list(self):
        return self.prop_list

    def get_geometry(self):
        return self.geometry

    def __str__(self):
        representation = 'Feature description: \n Feature type: {0}'.format(self.feature_type)
        representation = representation + '\n' + 'Feature properties: \n' + str(self.prop_list)
        representation = representation + '\n' + self.geometry.__str__()
        return representation
