import typing


class GenericTracker(object):

    def __init__(self):
        self.item_list = []

    def insert(self, items):
        for item in items:
            self.item_list.append(item)

    def get_mean(self):
        if len(self.item_list) == 0:
            return 0
        raw_mean = sum(self.item_list) / len(self.item_list)
        return round(raw_mean, 2)


class TemperatureTracker(GenericTracker):

    def get_min(self):
        return min(self.item_list)

    def get_max(self):
        return max(self.item_list)

    def insert(self, items: typing.List):
        """
        Here I overrode the insert function to implement the exception handling concerning non-integer
        :param items:
        :return:
        """
        for item in items:
            if not isinstance(item, int):
                raise Exception(f"Integer only! : '{item}' is not an integer")
            self.item_list.append(item)
