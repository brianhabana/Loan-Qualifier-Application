from qualifier.utils.fileio import (
    load_csv,
    save_csv,
)

def test_csv(cvspath, save_csv):
        print(f'the cvspath is{cvspath}')
        print(f'the filename is{save_csv}')