from tools import JKit
import sys


class ApiClient:
    def __init__(self):
        self.url = "https://restapi.amap.com/v3/bus/linename?parameters"
        self.params = {
            'key': '',
            'city': '',
            'keywords': '',
            'extensions': 'base'
        }

    def setCity(self, city):
        self.params['city'] = city

    def setKey(self, key):
        self.params['key'] = key

    def setKeywords(self, keywords):
        self.params['keywords'] = keywords

    def setExtensions(self, all):
        if all:
            self.params['extensions'] = 'all'

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


def main():
    userInput = sys.argv[1:]
    apc = ApiClient()
    apc.setKey(userInput[0])
    apc.setCity(userInput[1])
    apc.setKeywords(userInput[2])
    lines = apc.getLine()
    for line in lines:
        print(line)


if __name__ == '__main__':
    main()
