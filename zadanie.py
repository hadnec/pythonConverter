import argparse

parser = argparse.ArgumentParser(description='Opis programu')
parser.add_argument('-a', '--argument', help='Opis argumentu')
args = parser.parse_args()
if args.argument:
    print(f'Przekazany argument: {args.argument}')
