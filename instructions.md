# Raspberry-Pi Alarm Clock

## What you need
- Raspberry-Pi + power supply
- SD-Card with 8GB or more
- external active speakers (connect via 3.5mm headphone jack)
- USB WiFi adapter (if your Pi has no WiFi module)
- LCD TODO: specification + link

TODO: image of all components

## Setup Raspbian
Download the latest raspian release from https://www.raspberrypi.org/downloads/raspbian/ (~2GB, takes 10-30min).
```bash
$ cd ~
$ mkdir pi-alarm
$ cd pi-alarm
$ wget https://downloads.raspberrypi.org/raspbian/images/raspbian-2017-12-01/2017-11-29-raspbian-stretch.zip
$ wget https://downloads.raspberrypi.org/raspbian/images/raspbian-2017-12-01/2017-11-29-raspbian-stretch.zip.sha256
$ sha256sum -c 2017-11-29-raspbian-stretch.zip.sha256
2017-11-29-raspbian-stretch.zip: OK
$ unzip 2017-11-29-raspbian-stretch.zip
``` 

Put the SD Card into your computer, unmount if automounted and find out the device point.
(replace XXX with your SD-card device, e.g. /dev/sdc)
```bash
$ lsblk
TODO: ausgabe lsblk
$ sudo umount /dev/XXX1
```


Copy the raspbian image on the SD Card (replace XXX with your SD-card device, e.g. /dev/sdc).
```
$ sudo dd if=2017-11-29-raspbian-stretch.img of=/dev/XXX bs=4M conv=fsync
4919918592 bytes (4,9 GB, 4,6 GiB) copied, 40,6631 s, 121 MB/s
$ sudo sync
```

Remove the SD Card from your computer and put it into the Pi.
Connect a keyboard, a display and the WiFi-USB-adapter to your Pi and power it on.

TODO: installation / first steps on raspbian (raspberry-config, apt-get dist-upgrade, ...)

Setup WiFi.


Install vim.
```bash
$ sudo apt-get install vim
```

Install SSH.
```bash
TODO: $ raspberry-config
```

TODO: Select SSH-Server

Setup automatic updates.
Let it install stable updates and (if necessary) reboot automatically at 3pm. Also it should cleanup after updates.
```bash
$ sudo apt-get install unattended-upgrades
$ dpkg-reconfigure -plow unattended-upgrades
$ sudo sed -i 's/^\/\/Unattended-Upgrade::Automatic-Reboot "[^"]+";/Unattended-Upgrade::Automatic-Reboot "true";/g' /etc/apt/apt.conf.d/50unattended-upgrades
$ sudo sed -i 's/^\/\/Unattended-Upgrade::Automatic-Reboot-Time "..:..";/Unattended-Upgrade::Automatic-Reboot-Time "15:00";/g' /etc/apt/apt.conf.d/50unattended-upgrades
$ sudo sed -i 's/^\/\/Unattended-Upgrade::Remove-Unused-Dependencies "[^"]+";/Unattended-Upgrade::Remove-Unused-Dependencies "true";/g' /etc/apt/apt.conf.d/50unattended-upgrades
```
Logfiles will be generated at `/var/log/unattended-upgrades/unattended-upgrades.log`

TODO: Setup ntp

Change the default password to a new one.
```bash
$ passwd
```

Shutdown the Pi.
```bash
$ sudo shutdown -P now
```

Disconnect Display and keyboard. Power on again.

Login via SSH from your Computer.

Setup SSH-login via keyfile. On your computer lookup your ssh-publickey.
```bash
$ cd ~/.ssh
```

## Setup LCD

TODO: xxx



