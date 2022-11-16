# G Manager

> Note: currently G600 is the **ONLY** device supported.
> If you have another device and would like to add support please create a device driver in `app/devices`

Onboard memory manager for Logitech G devices. 

Based heavily on [tulth/g600prog](https://github.com/tulth/g600prog)

## Disclaimer

This has been tested by me to work for my device. No guarantee it will work, and no guarantee it won't brick your device.

Highly recommend you run a `--dry-run` before actually writing to the device. 

## Requirements

- Python 3 (currently tested on 3.10)
- [PyUSB ^1.2](https://github.com/pyusb/pyusb)
- [libusb ^1.0](https://github.com/libusb/libusb)
- [toml ^0.1](https://github.com/uiri/toml)

## Install libusb

Visit [libusb.info](https://libusb.info/) for installation information.

### macOS

Using [homebrew](https://brew.sh):

```bash
brew install libusb
```

### Windows

Download from the libusb site

### Linux 

Your distribution may already have libusb installed.


## Install using pipenv (preferred)

You can install required pip dependencies using [pipenv](https://pipenv.pypa.io/en/latest/)

Clone the repository and in your terminal run:

```bash
pipenv install
```

## Install with pip

```bash
python3 -m pip install pyusb toml
```

## Command Arguments

|    Name     | Short Flag |       Long Flag        | Required | Description                                                                           |
|:-----------:|:----------:|:----------------------:|:--------:|:--------------------------------------------------------------------------------------|
|   source    |    N/A     |          N/A           |   Yes    | The config source, this can be a file or `'DEVICE'` to access device                  |
| destination |    N/A     |          N/A           |    No    | Destination of the config, can be a file name, `'DEVICE'` or empty to print to stdout |
|    bytes    |    `-b`    |       `--bytes`        |    No    | Set output to be the bytes of the config. This is a portable file between versions    |
|  overwrite  |    `-y`    |     `--overwrite`      |    No    | Will overwrite the destination file if it exists.                                     |
|  minified   |    `-m`    |      `--minified`      |    No    | Store the config as a minified file. No line breaks                                   |
|   dry run   |    `-n`    |      `--dry-run`       |    No    | Will not actually write to the device.                                                |
|    force    |    `-f`    |       `--force`        |    No    | Skip all validation checks before writing to the device. **NOT RECOMMENDED**          |
|   lenient   |    `-l`    |      `--lenient`       |    No    | Allow importing config from an earlier version of this app.                           |
|   verbose   |    `-v`    |      `--verbose`       |    No    | Show more detailed output .                                                           |
|    quiet    |    `-q`    |       `--quiet`        |    No    | Don't show any output.                                                                |
|    debug    |    `-d`    |       `--debug`        |    No    | Show debugging output.                                                                |
|   version   |    N/A     |      `--version`       |    No    | Print the version and quit.                                                           |
|   device    |    N/A     |  `--device [DEVICE]`   |    No    | Specify a device driver relative to `app.devices`                                     |
|   config    |    N/A     | `--config-file [FILE]` |    No    | Specify a different config file to load.                                              |


## Usage

> Note: if reading from the device you will need elevated privileges.
> macOS/Linux: run `sudo [COMMAND]`
> Windows: run command prompt as Administrator

For the following usage examples only `g-manager.py` will be displayed. Depending on your set up you will run using:

**Using `pipenv`**

```bash
pipenv run python g-manager.py [SOURCE] [DESTINATION] [options]
```

**No `pipenv`**

```bash
python3 g-manager.py [SOURCE] [DESTINATION] [options]
```

### From Device to File

```bash
g-manager.py DEVICE file.json
```

Will create a readable file called `file.json` with all the reports and button maps.

### From File to Device

```bash
g-manager.py file.json DEVICE
```

Will import from `file.json` and write to the device.

### From Readable File to Bytes File Format

```bash
g-manager.py file.json file-bytes.json --bytes
```

Will create a new file `file-bytes.json` in the bytes file format.

## Creating a Driver

Documentation in progress.