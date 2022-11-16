import sys
import app
from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()
    parser.add_argument(
        'source', nargs='?',
        help='Config source, file name or device accessor (default: DEVICE)'
    )
    parser.add_argument(
        'destination', nargs='?',
        help='Config destination, file name or device accessor (default: DEVICE)'
    )
    parser.add_argument(
        '-b', '--bytes', action='store_true', dest='as_bytes',
        help='Store the config as bytes. This will be portable from version to version.'
    )
    parser.add_argument(
        '-y', '--overwrite', action='store_true',
        help='Overwrite the destination file if it exists.'
    )
    parser.add_argument(
        '-m', '--minified', action='store_true',
        help='Store as minified JSON.'
    )
    parser.add_argument(
        '-n', '--dry-run', action='store_true',
        help='Skip actually writing to the device.'
    )
    parser.add_argument(
        '-f', '--force', action='store_true',
        help='Skip verification before writing to the device. NOT RECOMMENDED'
    )
    parser.add_argument(
        '-l', '--lenient', action='store_true',
        help='Allow loading readable JSON format from older versions.'
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='Show more detailed output.'
    )
    parser.add_argument(
        '-q', '--quiet', action='store_true',
        help='Don\'t show any output.'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='Show debug output.'
    )
    parser.add_argument(
        '--version', action='store_true',
        help='Display the current version and exit.'
    )
    parser.add_argument(
        '--device',
        help='Specify the device driver to use. This overrides the config value. Access as "somepackage.somedriver" '
             'relative to app.devices '
    )
    parser.add_argument(
        '--config-file',
        help='Specify a different config file to use instead of the default.'
    )
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
        if self._loaded['version']:
            print('{0} v{1}'.format(app.name, app.version))
            exit(0)
        if self._loaded['source'] is None:
            print('[ERROR]: source is a required argument!')
            exit(1)

    def get_loaded(self):
        return self._loaded
