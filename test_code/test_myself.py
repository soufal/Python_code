"""
干扰源重构代码。
"""

class RouteLine(object):
    """
    RouteLine类：
        带方向路径类。
    attributes：

    """
    def __init__(self, lng, lat, to_lng, to_lat, weight):

        self.lng = lng
        self.lat = lat
        self.to_lng = to_lng
        self.to_lat = to_lat

class InsectPoint(object):
    """
    InsectPoint类：
        带权交点类。
    """

class ClassCentre(object):
    """
    ClassCentre:
        聚类中心类。
    """