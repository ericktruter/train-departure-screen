# UK train departure screen - Forked from chrishutchinson
Original - https://github.com/chrishutchinson/train-departure-screen

I have modified Chris Hutchinson version of the code to rahter use the Huxley 2 cross-platform JSON proxy for the GB railway Live Departure Boards. It is using their demo server comes with zero guarantees of uptime. It can (and regularly does) go down or break. 

> Python script to display replica real-time UK railway station departure screens for SSD13xx devices

## Sample output

![Example output of the script](capture.png)

## Requirements

To run this code, you will need Python 3.6+.

### Raspbian

If you're using Raspbian Lite, you'll also need to install:

- `libopenjp2-7`

with:

```bash
$ sudo apt-get install libopenjp2-7
```

## Usage

1. Clone this repo

2. Install dependencies

```bash
$ pip install -r requirements.txt
```

3. Sign up for API access token from NRE - https://realtime.nationalrail.co.uk/OpenLDBWSRegistration/Registration

4. Copy `config.sample.json` to `config.json` and complete the values, including your NRE access token from step 3 to be entered in the apiKey variable. appId is not in use in this version. _Note: station names should be provided as their three-letter station code, all available [here](https://www.nationalrail.co.uk/stations_destinations/48541.aspx)._

eg:
```bash
{
  "journey": {
    "departureStation": "rmd",
    "destinationStation": null
  },
  "refreshTime": 180,
  "transportApi": {
    "appId": "",
    "apiKey": "xxxxxxyourxtokenxherexxxxxxx"
  }
}
```

5. Start the app with:

```bash
$ python ./src/main.py --display pygame --width 256 --height 64
```

Change the `--display` flag to alter the output mechanism (a list of options can be found in this README: https://github.com/rm-hull/luma.examples). Use `capture` to save to images, and `pygame` to run a visual emulator.

Remember to pass `--interface spi` if you are using SPI to communicate with your screen. Otherwise, the default of `i2c` should suffice.

```bash
$ python ./src/main.py --display ssd1322 --width 256 --height 64 --interface spi
```

## Video demo

I've tweeted a video demo of the software running on a real device: https://twitter.com/ericktruter/status/1792897298243924400

## Thanks

Thanks to Chris Hutchinson for the original version.
The fonts used were painstakingly put together by `DanielHartUK` and can be found on GitHub at https://github.com/DanielHartUK/Dot-Matrix-Typeface - A huge thanks for making that resource available!
