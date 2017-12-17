# Raspberry-Pi Alarm Clock

## Setup LCD

As an example we will use a
[Waveshare 3.2inch RPi LCD (B)](https://www.waveshare.com/product/3.2inch-rpi-lcd-b.htm) (320×240px / XPT2046 / ads7846)
which will fit perfectly on a Raspberry Pi 1 Model B (or B+).
More information:
[Manual](https://www.waveshare.com/w/upload/3/3e/RPi-LCD-User-Manual.pdf),
[Dimensions](https://www.waveshare.com/w/upload/5/56/3.2inch-rpi-lcd-b-panel-dimension.pdf),
[Schematics](http://www.waveshare.com/w/upload/a/ad/3.2inch-RPi-LCD-B-Schematic.pdf),
[Wiki](https://www.waveshare.com/wiki/3.2inch_RPi_LCD_(B)).

Shutdown your Pi and power it off.

Connect the display and power the Pi back on.

Download and install the driver (Pi will reboot during the installation).

```
rpi$ cd ~
rpi$ mkdir pi-alarm
rpi$ cd pi-alarm
rpi$ wget http://www.waveshare.com/w/upload/0/00/LCD-show-170703.tar.gz
rpi$ tar xf LCD-show-170703.tar.gz
rpi$ cd LCD-show
rpi$ ./LCD32-show
```

Rotate Display (replace XXX with one of [0, 90, 180, 270]) (Will reboot the Pi).

```
rpi$ cd ~/pi-alarm/LCD-show
rpi$ ./LCD32-show XXX
```

TouchScreen calibration (Needs reboot to become effective).

```
rpi$ cd ~/pi-alarm
rpi$ sudo apt-get install xinput-calibrator
rpi$ DISPLAY=:0.0 xinput_calibrator > lcd-calibration-new.cfg
rpi$ sed -i '/Section "InputClass"/,$!d' lcd-calibration-new.cfg
rpi$ cp /usr/share/X11/xorg.conf.d/99-calibration.conf ./lcd-calibration-old.cfg
rpi$ sudo cp ./lcd-calibration-new.cfg /usr/share/X11/xorg.conf.d/99-calibration.conf
```

Disable screen auto power off.
```
rpi$ sudo sed -i 's/#\(xserver-command=X\)/\1 -s 0 -dpms/' /etc/lightdm/lightdm.conf
```
