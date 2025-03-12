import argparse
from .configManager import ConfigManager
from tools.echo import echo


class NavicCLI:
    """Command Tool"""
    def __init__(self, apiClinet):
        self.conMan = ConfigManager()
        self.apClt = apiClinet
        self.parser = argparse.ArgumentParser(description="基于高德api的查询工具")
        self.file = ''
        self._loadConfig()
        self._setupParameters()

    def _loadConfig(self):
        self.apClt.setKey(self.conMan.get('key'))
        self.apClt.setCity(self.conMan.get('city'))
        self.file = self.conMan.get('file')

    def _setupParameters(self):
        self._setup_nurmalParameters()

        self._setup_advanceParameters()

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

    def _setup_advanceParameters(self):
        self.parser.add_argument('--set', action='store_true',
                                 help='开启设置模式，能保存默认的key和city')
        self.parser.add_argument('-r', '--remove', action='store_true',
                                 help='删除相应的默认设置')
        self.parser.add_argument('-f', '--file', type=str,
                                 help='将原始数据重定向到文件')

    def _setup_mode(self, args):
        # save new config
        if args.key:
            self.conMan.set('key', args.key)
        if args.city:
            self.conMan.set('city', args.city)
        if args.file:
            self.conMan.set('file', args.file)
        self.conMan.save()
        exit(0)

    def _remove_mode(self):
        # remove old config
        user_input = input("请输入k/c/f\n来删除默认key/city/file:\n")
        user_input = user_input.lower()
        if 'k' in user_input:
            self.conMan.del_key('key')
        if 'c' in user_input:
            self.conMan.del_key('city')
        if 'f' in user_input:
            self.conMan.del_key('file')
        self.conMan.save()
        exit(0)

    def readCommand(self):
        args = self.parser.parse_args()

        if args.set:
            """ open setting mode"""
            self._setup_mode(args)

        if args.remove:
            self._remove_mode()

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
        if args.file:
            self.file = args.file

        self.apClt.setKeywords(args.word)
        self.apClt.setExtensions(args.extensions)

    def output(self, data, data_type='lines'):
        if self.file:
            echo(data, 'json', file_path=self.file)
        else:
            # stdout
            extensions = self.apClt.getExtensions()
            echo(data, extensions, data_type=data_type)
