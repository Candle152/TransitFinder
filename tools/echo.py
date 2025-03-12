from tools.JKit import save_json_file


def printline_base(line):
    print('id: ' + line['id'])
    print('type: ' + line['type'])
    print('name: ' + line['name'])
    print('start_stop: ' + line['start_stop'])
    print('end_stop: ' + line['end_stop'])


def printline_other(line):
    print('start_time: ' + line['start_time'])
    print('end_time: ' + line['end_time'])
    print('company: ' + line['company'])
    print('busstops:')
    for busstop in line['busstops']:
        print(busstop)


def printLines(lines, mode='base'):
    if len(lines) == 0:
        print('Don`t find any lines')
    for line in lines:
        print("--------------------------")
        if mode == 'base':
            printline_base(line)
        elif mode == 'all':
            printline_base(line)
            printline_other(line)
        print("--------------------------")


def echo(data, mode, file_path=None, data_type='lines'):
    """
    if file_path is not None ,the mode is the data type
    else the mode is the output mode
    """
    if file_path:
        # out to file
        if mode == 'json':
            save_json_file(data, file_path)
    else:
        # std output
        if data_type == 'lines':
            printLines(data, mode)


if __name__ == '__main__':
    lines = [{'id': '0', 'name': 'helo', 'type': 'test',
              'start_stop': '0', 'end_stop': '1', 'company': 'test',
              'start_time': '2', 'end_time': '3', 'busstops': []}]
    echo(lines, mode='base')
    echo(lines, mode='all')
    echo(lines, mode='json', file_path='test.log')