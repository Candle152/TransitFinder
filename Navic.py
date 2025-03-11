from core import apiClient
from core import navicCLI
import sys

# the file which save the key
CONFIG_FILE = "_navicrc"


if __name__ == '__main__':
    userInput = sys.argv[1:]
    apc = apiClient.ApiClient()
    NCLI = navicCLI.NavicCLI(apc)
    NCLI.readCommand()
    # print(apc.params['key'])
    # print(apc.params['extensions'])
    # print(apc.params)
    lines = apc.getLine()
    NCLI.printLines(lines)