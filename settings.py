class Settings(object):

    def __init__(self, file_name):
        import json
        with open(file_name, 'r') as f:
            self.Config = json.load(f)

    def get(self, key):
        try:
            return self.Config.get(key)
        except:
            exit()
