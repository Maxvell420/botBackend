import sys
from rich.pretty import pprint


def dd(*args):
    """Красивый вывод с подсветкой и завершением"""
    pprint("----------------------------")
    for arg in args:
        pprint(arg, expand_all=True)
    pprint("----------------------------")
    sys.exit(0)


def dump(*args):

    pprint("----------------------------")
    for arg in args:

        pprint(arg, expand_all=True)
    pprint("----------------------------")
