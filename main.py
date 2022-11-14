from pprint import pprint

import app.config
import app.readers

"""
TODO:
- when a device is called, change the tuple of report_map to actual instances
- should be able to pass things like, self, index, is shifted, etc. to the new instance
    since it will have already been defined
- read the bytes from a byte array into the report map
- CompositeField has multiple bytes, so we'll need to instantiate and then count
    the bytes from all related ByteFields. Should be able to iterate based on those numbers to
    equal the total report_length.
- Maybe add a get_total_bytes() method to CompositeField to make that easier?
"""

if __name__ == '__main__':
    dev = app.config.get_device()
    r = app.readers.DeviceReader(dev)
    report = r.get_report(1)
    c = 0
    mapped = []
    for i in dev.get_report_map():
        for b in range(i[1].get_total_bytes()):
            mapped.append(
                (c, b, i[0], report[c+1])
            )
            c += 1

    pprint(mapped)
