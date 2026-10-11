"""Run original notebook code cells from the repository root."""
import argparse
import json
import os
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('part', choices=['1', '2'])
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
os.chdir(root)
if args.part == '2':
    missing = [str(root / 'data' / f'{year}.csv.bz2') for year in range(2004, 2009)
               if not (root / 'data' / f'{year}.csv.bz2').is_file()]
    if missing:
        parser.error('Restore raw flight files first. See data/README.md. Missing: ' + ', '.join(missing))
notebook = root / f'240672870_part{args.part}_python.ipynb'
namespace = {'__name__': '__main__'}
for index, cell in enumerate(json.loads(notebook.read_text())['cells']):
    if cell['cell_type'] == 'code':
        print(f'Running code cell {index + 1}', flush=True)
        exec(compile(''.join(cell['source']), f'{notebook.name}:cell{index + 1}', 'exec'), namespace)
if args.part == '1':
    print(namespace['summary_a_py'].to_string(index=False))
    print(namespace['rb_result_py'].to_string(index=False))
print('Finished. New figures are in the repository root; supplied figures are in figures/.')
