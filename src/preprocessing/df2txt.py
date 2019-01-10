import argparse
import sys
import textwrap

from df_reader import DataFrameLoader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str,
                        help= textwrap.dedent("""data directory containing file name"""))
    parser.add_argument('--output', type=str,
                        help='Directs the output to a file name')
    parser.add_argument('--select', type=str,
                        help='optional')

    args = parser.parse_args()

    if len(sys.argv) == 1 or not args.data_dir:
        parser.print_help()
    else:
        DataFrameLoader(args.data_dir, output=args.output, select=args.select)

if __name__ == '__main__':
    main()