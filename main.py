import app.config
from pprint import pp
import app.readers

if __name__ == '__main__':
    pp(app.readers.DeviceReader(app.config.get_device()).get_report(1))
