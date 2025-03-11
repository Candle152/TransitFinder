import argparse
from .configManager import ConfigManager


class NavicCLI:
    """Command Tool"""
    def __init__(self, apiClinet):
        self.conMan = ConfigManager()
        self.apClt = apiClinet
        self.parser = argparse.ArgumentParser(description="基于高德api的查询工具")
        self._loadConfig()
        self._setupParameters()

    def _loadConfig(self):
        self.apClt.setKey(self.conMan.get('key'))
        self.apClt.setCity(self.conMan.get('city'))

    def _setupParameters(self):
        self._setup_nurmalParameters()

        self._setup_settingParameters()

    def _setup_nurmalParameters(self):
        self.parser.add_argument('-k', '--key', type=str,
                                 help='设置密钥')
        self.parser.add_argument('-c', '--city', type=str,
                                 help='设置查询城市(中文,城市编码)')
        self.parser.add_argument('-w', '--word', type=str,
                                 help='设置想要查询线路名称')
        self.parser.add_argument('-e', '--extensions', type=str,
                                 choices=['base', 'all'],
                                 default='base',
                                 help='返回基本信息或详细信息')
        self.parser.add_argument('-n', '--number', type=int,
                                 help='设置最大查询个数，默认1')

    def _setup_settingParameters(self):
        self.parser.add_argument('--set', action='store_true',
                                 help='开启设置模式，能保存默认的key和city')

    def _setup_mode(self, args):
        # save new config
        if args.key:
            self.conMan.set('key', args.key)
        if args.city:
            self.conMan.set('city', args.city)
        self.conMan.save()
        exit(0)

    def readCommand(self):
        args = self.parser.parse_args()

        if args.set:
            """ open setting mode"""
            self._setup_mode(args)

        if not args.city and not self.conMan.check_exists('city'):
            print("error: don`t have config city or -c/--city")
            exit(1)
        if not args.word:
            print("error: the following arguments are required: -l/--line")
            exit(1)

        if args.key:
            self.apClt.setKey(args.key)
        if args.number:
            self.apClt.setOffset(args.number)
        if args.city:
            self.apClt.setCity(args.city)
            
        self.apClt.setKeywords(args.word)
        self.apClt.setExtensions(args.extensions)

    def _printline_base(self, line):
        print('id: ' + line['id'])
        print('type: ' + line['type'])
        print('name: ' + line['name'])
        print('start_stop: ' + line['start_stop'])
        print('end_stop: ' + line['end_stop'])

    def _printline_other(self, line):
        print('start_time: ' + line['start_time'])
        print('end_time: ' + line['end_time'])
        print('company: ' + line['company'])
        print('busstops:')
        for busstop in line['busstops']:
            print(busstop)

    def printLines(self, lines):
        if len(lines) == 0:
            print('Don`t find any lines')

        extensions = self.apClt.getExtensions()
        for line in lines:
            print("--------------------------")
            if extensions == 'base':
                self._printline_base(line)
            elif extensions == 'all':
                self._printline_base(line)
                self._printline_other(line)
            print("--------------------------")
