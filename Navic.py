from core import apiClient
import sys

# the file which save the key
CONFIG_FILE = "_navicrc"


def readCommand(argv):
    import argparse
    # read the command
    parser = argparse.ArgumentParser(description="基于高德api的公交查询工具")
    parser.add_argument('-k', '--key', type=str, help='设置密钥')
    parser.add_argument('-c', '--city', type=str,
                        help='设置查询城市(中文,全拼音,城市编码)')
    parser.add_argument('-l', '--line', type=str,
                        help='设置想要查询线路')
    parser.add_argument('-a', '--all',
                        action='store_true', help='返回详细信息')
    parser.add_argument('-n', '--number', type=int, help='设置最大查询个数，默认1')
    parser.add_argument('--set-key', type=str, help='设置默认key')

    # Parsing parameters and return
    return parser.parse_args()


def processCommand(args, apc):
    if not args.city:
        print("error: the following arguments are required: -c/--city")
        exit(1)
    if not args.line:
        print("error: the following arguments are required: -l/--line")
        exit(1)
    if args.key:
        apc.setKey(args.key)
    if args.number:
        apc.setOffset(args.number)
    apc.setCity(args.city)
    apc.setKeywords(args.line)
    apc.setExtensions(args.all)


if __name__ == '__main__':
    userInput = sys.argv[1:]
    apc = apiClient.ApiClient()
    processCommand(readCommand(userInput), apc)
    lines = apc.getLine()
    for line in lines:
        print(line)
