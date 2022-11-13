import app.config
from pprint import pp

if __name__ == '__main__':
    pp(app.config.get_device())
    pp(app.config.get_device().map_report_to())
    pp(app.config.get_device().button_names())
