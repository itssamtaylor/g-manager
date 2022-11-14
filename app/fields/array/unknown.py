from app.fields.array import ArrayField


class Unknown(ArrayField):
    def init(self):
        index = self.get_arg('index')
        if index is not None:
            group_indexes = self.device.unknown_group_indexes[index]
            self._data = [0 for i in range(group_indexes[0], group_indexes[1])]
