from app.devices.mouse.G600 import G600
from pprint import pp

if __name__ == '__main__':
    mouse = G600()
    pp(mouse)
    pp(mouse.map_report_to())
