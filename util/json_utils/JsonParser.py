from models.Feature import Feature
from models.Geometry import Geometry
from models.Point import Point
from util.Reader import Reader


def parse_features_collection_json():
    # path_to_file = '/Users/akratovich/projects/python/python_stud/parser/RealJsonSample.json'
    path_to_file = '/Users/akratovich/projects/python/sf-city-lots-json/citylots.json'
    parsed_features = []

    features_collection = Reader.read_json(path_to_file)

    for feature_item in features_collection['features']:
        tmp_coord_list = __get_points(feature_item)
        tmp_figure_type = __get__geometry_type(feature_item)

        tmp_geometry = Geometry(tmp_figure_type, tmp_coord_list)

        tmp_feature_type = __get_feature_type(feature_item)
        tmp_prop_list = __get_prop_feature_prop_list(feature_item)
        feature = Feature(tmp_feature_type, tmp_prop_list, tmp_geometry)
        # print(feature.__str__())
        parsed_features.append(feature)
        print('{0} features are parsed'.format(parsed_features.__len__()))
    print('Parsed {0} features'.format(parsed_features.__len__()))
    return parsed_features


def __get_prop_feature_prop_list(feature):
    prop_list = feature['properties']
    return prop_list


def __get_feature_type(feature):
    feature_type = feature['type']
    return feature_type


def __get__geometry_type(feature):
    geometry = feature['geometry']
    geometry_type = 'N/A'
    if geometry:
        geometry_type = geometry['type']
    return geometry_type


def __get_points(feature):
    # try:
    geometry = feature['geometry']
    points_list = []
    if geometry:
        coord_list = geometry['coordinates']

        for point in coord_list:
            for item in point:
                tmp_point = Point(item[0], item[1], item[2])
                points_list.append(tmp_point)

    return points_list


def get_feature_by_property(prop_key, prop_value):
    features = parse_features_collection_json()
    result = []
    for feature in features:
        properties = feature.get_prop_list()
        if prop_value == properties.get(prop_key):
            result.append(feature)
            print(feature.__str__())
    print("{0} features satisfies search criteria (property's value: [{1}:{2}])".format(result.__len__(), prop_key,
                                                                                        prop_value))
    return result


# parse_features_collection_json()
get_feature_by_property('STREET', 'NORTH POINT')
