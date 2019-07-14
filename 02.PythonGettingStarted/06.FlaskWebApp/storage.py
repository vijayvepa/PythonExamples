import json


class Storage:
    @staticmethod
    def save(obj):
        f = open('build/storage.json', 'w')
        json.dump(obj, f)
        f.close()

    @staticmethod
    def load():
        try:
            with open('build/storage.json', 'r') as f:
                return json.load(f)
        except Exception:
            return []
