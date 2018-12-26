class Geometry:
    def __init__(self, figure_type, points_list):
        self.figure_type = figure_type

        self.points_list = points_list

    def get_figure_type(self):
        return self.figure_type

    def get_points_list(self):
        return self.points_list

    def __str__(self):
        representation = 'Figure type: {0}'.format(self.figure_type)
        for point in self.points_list:
            representation = representation + '\n' + point.__str__()
        return representation
