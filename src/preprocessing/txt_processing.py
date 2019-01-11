import argparse
import sys
import textwrap

from txt_reader import TextLoader

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str,
                        help= textwrap.dedent("""data directory containing file name"""))
    parser.add_argument('--output', type=str,
                        help='Directs the output to a file name')
    parser.add_argument('--segment', type=str,
                        help='Directs the segment to a file name')

    args = parser.parse_args()

    if len(sys.argv) == 1 or not args.data_dir:
        parser.print_help()
    else:
        TextLoader(args.data_dir, output=args.output, segment=args.segment)

if __name__ == '__main__':
    main()