import sys
import os

sys.path.extend([os.sep.join([os.getcwd(), 'src'])])

if __name__ == '__main__':
    import config
    print(config.json_indent)