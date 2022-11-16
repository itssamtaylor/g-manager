import sys

from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('destination', nargs='?')
    parser.add_argument('-b', '--bytes', action='store_true', dest='as_bytes')
    parser.add_argument('-y', '--overwrite', action='store_true')
    parser.add_argument('-m', '--minified', action='store_true')
    parser.add_argument('-n', '--dry-run', action='store_true')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('-f', '--force', action='store_true')
    parser.add_argument('--device')
    parser.add_argument('--config-file')
    return parser


class ArgumentLoader:
    _loaded: dict = {
        'config_file': None,
        'device': None,
    }

    def __init__(self):
        if sys.stdin.isatty():
            if len(sys.argv) == 1:
                sys.argv.append('-h')
            self._loaded = create_parser().parse_args().__dict__
            self._validate()

    def _validate(self):
        if self._loaded['verbose'] or self._loaded['debug']:
            if self._loaded['quiet']:
                raise Exception('--quiet is incompatible with --debug and --verbose!')

    def get_loaded(self):
        return self._loaded
