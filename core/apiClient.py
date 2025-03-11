from tools import JKit


class ApiClient:
    """API Call Management"""
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
        if the requests error, data will have 'error'
        """
        data = JKit.load_url(self.url, self.params)
        if 'error' in data:
            print(data['error'])
            exit(1)
        try:
            if data['count'] != 0:
                return data['buslines']
            else:
                return dict()
        except Exception:
            print(data['info'])
