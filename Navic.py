from tools import JKit
import sys

key = ''


def getLine(linename, city):
    """
    get the line for the bus in the city
    return JSON
    """
    global key

    url = "https://restapi.amap.com/v3/bus/linename?parameters"
    params = {
        'key': key,
        'city': city,
        'keywords': linename,
        'extensions': 'all'
    }
    data = JKit.load_url(url, params)
    try:
        if data['count'] != 0:
            return data['buslines'][0]
        else:
            return dict()
    except Exception:
        print(data['info'])
        if data['info'] == 'USER_DAILY_QUERY_OVER_LIMIT':
            print('The key is depleted')


def main():
    userInput = sys.argv[1:]
    global key
    key = userInput[2]
    line = getLine(userInput[0], userInput[1])
    print('id:\t' + line['id'])
    print('type:\t' + line['type'])
    print('name:\t' + line['name'])
    print('basic_price\t' + line['basic_price'])
    print('stops:')
    print(line['busstops'])


if __name__ == '__main__':
    main()
