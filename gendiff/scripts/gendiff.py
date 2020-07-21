
# -*- coding:utf-8 -*-


import argparse


def main():
    """Run an example code."""
    parser = argparse.ArgumentParser(description='Generate diff')
#    parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
#    parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')
    """
    parser.add_argument('--format', dest='', action='', nargs='?',
                    default='plain',
                    choices=['plain', 'pretty', 'JSON'],
                    help='plain text | pretty | JSON')
    """
    parser.add_argument('first_file',
                    type=argparse.FileType('r'))
    parser.add_argument('second_file',
                    type=argparse.FileType('r'))
    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()