import app.core.transformer
import app.config
import app.readers


if __name__ == '__main__':
    r = app.readers.DeviceReader(app.config.get_device())
    for i, r in enumerate(r.get_report(3)):
        print(i, r)

