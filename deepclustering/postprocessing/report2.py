# this is to compare experimental data cross different folders
import argparse
from itertools import repeat
from pprint import pprint
from typing import List, Dict

import pandas as pd
from pathlib import Path
from deepclustering.utils import str2bool
from deepclustering.utils import merge_dict


def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Report results from different folders.')
    filepath_group = parser.add_mutually_exclusive_group(required=True)
    filepath_group.add_argument("--specific_folders", '-s', type=str, nargs='+', help='list specific folders.',
                                metavar='PATH')
    filepath_group.add_argument("--top_folder", '-t', type=str, help='top folder.',
                                metavar="PATH")
    parser.add_argument('--classes', type=str, nargs='+', help='Targeted class in the .csv file.', required=True)
    parser.add_argument('--file', type=str, default='wholeMeter.csv', metavar='FILENAME',
                        help='.csv file name, default `wholeMeter.csv`.')
    parser.add_argument('--high_better', type=str2bool, nargs='+',
                        help='is the class value is high is better. default True,'
                             'if given, high_better must have the same size as classes.',
                        default=True)
    parser.add_argument('--save_dir', type=str, help='save summary dir.', required=True)
    args = parser.parse_args()
    if isinstance(args.high_better, list):
        assert len(args.high_better) == len(args.classes), f"high_better must correspond to classes, " \
            f"given classes: {args.classes} and high_better: {args.high_better}."
    print(vars(args))
    return args


def main(args: argparse.Namespace):
    if hasattr(args, 'top_folder'):
        # a top folder is provided.
        csvfile_paths: List[Path] = list(Path(args.top_folder).rglob(f'{args.file}'))
    else:
        pass
    assert len(csvfile_paths) > 0, f"Found 0 {args.file} file."
    print(f"Found {len(csvfile_paths)} {args.file} files, e.g.,")
    pprint(csvfile_paths[:5])
    path_features = extract_path_info(csvfile_paths)

    values: Dict[str, Dict[str, float]] = \
        {str(p): {c: extract_value(p, c, h) for c, h in zip(args.classes, repeat(
            args.high_better) if args.high_better == True else args.high_better)} for p in csvfile_paths}

    table = pd.DataFrame(merge_dict(path_features, values)).T
    print(table)
    table.to_csv(Path(args.save_dir, 'summary.csv'))


extract_value = lambda file_path, class_name, is_high: pd.read_csv(file_path)[class_name].max() if is_high else \
    pd.read_csv(file_path)[class_name].min()


def extract_path_info(file_paths: List[Path]) -> List[List[str]]:
    # return the list of path features for all the file_paths
    def split_path(file_path: str, sep='/') -> List[str]:
        parents: List[str] = file_path.split(sep)[:-1]
        return parents

    assert (set([len(split_path(str(p))) for p in
                 file_paths])).__len__() == 1, f"File paths must have located in a structured way."
    parents_path = []
    for i, p in enumerate(file_paths):
        parents_path.append(split_path(str(p)))

    path_begin: int = (pd.DataFrame(parents_path).nunique(axis=0) > 1).values.argmax()
    return {str(p): {f"feature_{i}": _p for i, _p in enumerate(split_path(str(p))[path_begin:])} for p in file_paths}


if __name__ == '__main__':
    args = arg_parser()
    main(args)
