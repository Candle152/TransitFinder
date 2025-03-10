from tools import JKit


class ApiClient:
    def __init__(self):
        self.url = "https://restapi.amap.com/v3/bus/linename?parameters"
        self.params = {
            'key': '',
            'city': '',
            'keywords': '',
            'extensions': 'base',
            'offset': '1'
        }

    def setCity(self, city):
        self.params['city'] = city

    def setKey(self, key):
        self.params['key'] = key

    def setKeywords(self, keywords):
        self.params['keywords'] = keywords

    def setExtensions(self, extensions):
        self.params['extensions'] = extensions

    def setOffset(self, number):
        self.params['offset'] = number
    
    def getLine(self):
        """
        get the line for the bus in the city
        return JSON
        """
        data = JKit.load_url(self.url, self.params)
        try:
            if data['count'] != 0:
                return data['buslines']
            else:
                return dict()
        except Exception:
            print(data['info'])
            if data['info'] == 'USER_DAILY_QUERY_OVER_LIMIT':
                print('The key is depleted')
