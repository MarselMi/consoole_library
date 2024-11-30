import json


class JsonMixin:
    def to_json(self):
        json.dumps(self.__dict__)
