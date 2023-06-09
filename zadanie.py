import argparse
import json

parser = argparse.ArgumentParser(description='Opis programu')
parser.add_argument('-a', '--argument', help='Opis argumentu')
args = parser.parse_args()
if args.argument:
    print(f'Przekazany argument: {args.argument}')
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f'Błąd podczas wczytywania pliku JSON: {e}')
        return None
