import argparse
from .configReader import ConfigReader


class NavicCLI:
    def __init__(self, apiClinet):
        self.conRe = ConfigReader()
        self.apClt = apiClinet
        self.parser = argparse.ArgumentParser(description="基于高德api的查询工具")
        self._loadConfig()
        self._setCommand()

    def _loadConfig(self):
        self.apClt.setKey(self.conRe.get('key'))

    def _setCommand(self):
        self.parser.add_argument('-k', '--key', type=str,
                                 help='设置密钥')
        self.parser.add_argument('-c', '--city', type=str,
                                 help='设置查询城市(中文,全拼音,城市编码)')
        self.parser.add_argument('-l', '--line', type=str,
                                 help='设置想要查询线路')
        self.parser.add_argument('-a', '--all', action='store_true',
                                 help='返回详细信息')
        self.parser.add_argument('-n', '--number', type=int,
                                 help='设置最大查询个数，默认1')
        self.parser.add_argument('--set-key', type=str,
                                 help='设置默认key')

    def readCommand(self):
        args = self.parser.parse_args()

        if args.set_key:
            self.conRe.set('key', args.set_key)
            self.conRe.save()
            exit(0)
        if not args.city:
            print("error: the following arguments are required: -c/--city")
            exit(1)
        if not args.line:
            print("error: the following arguments are required: -l/--line")
            exit(1)
        if args.key:
            self.apClt.setKey(args.key)
        if args.number:
            self.apClt.setOffset(args.number)

        self.apClt.setCity(args.city)
        self.apClt.setKeywords(args.line)
        self.apClt.setExtensions(args.all)

        return self.parser.parse_args() 
