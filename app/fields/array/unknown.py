from app.fields.array import ArrayField


class Unknown(ArrayField):
    def init(self):
        index = self.get_arg('index')
        if index is not None:
            group_indexes = self.device.unknown_group_indexes[index]
            self._length = len(range(group_indexes[0], group_indexes[1]))
