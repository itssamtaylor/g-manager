from pprint import pprint

import app.config
import app.readers


if __name__ == '__main__':
    dev = app.config.get_device()
    r = app.readers.DeviceReader(dev)
    report = r.get_report(1)
    c = 0
    mapped = []
    for i in dev.get_report_map():
        for b in range(i[1].get_total_bytes()):
            mapped.append(
                (c, b, i[0], report[c])
            )
            c += 1

    pprint(mapped)
