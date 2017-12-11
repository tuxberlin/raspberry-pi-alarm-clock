# Raspberry Pi Installation

This guide assumes, that you operate from a Linux (Debian) machine.

## Put Raspbian on SD card

On your computer, download the latest raspian release from https://www.raspberrypi.org/downloads/raspbian/ (~2GB, takes 10-40min).

```
$ cd ~
$ mkdir pi-alarm
$ cd pi-alarm
$ wget https://downloads.raspberrypi.org/raspbian/images/raspbian-2017-12-01/2017-11-29-raspbian-stretch.zip
$ wget https://downloads.raspberrypi.org/raspbian/images/raspbian-2017-12-01/2017-11-29-raspbian-stretch.zip.sha256
$ sha256sum -c 2017-11-29-raspbian-stretch.zip.sha256
2017-11-29-raspbian-stretch.zip: OK
$ unzip 2017-11-29-raspbian-stretch.zip
``` 

Put the SD card into your computer and find the device point.  
Example:
```
$ lsblk
mmcblk0     179:0    0  29,5G  0 disk 
├─mmcblk0p2 179:2    0  29,4G  0 part /media/0ae2834e-2c8f-452d-a271-a266dc676114
└─mmcblk0p1 179:1    0    63M  0 part /media/boot
```
In the example the device point would be mmcblk0

If the card was automounted, unmount all mounted partitions.  
Example:
```
$ sudo umount /media/0ae2834e-2c8f-452d-a271-a266dc676114
$ sudo umount /media/boot
$ lsblk
mmcblk0     179:0    0  29,5G  0 disk 
├─mmcblk0p2 179:2    0  29,4G  0 part
└─mmcblk0p1 179:1    0    63M  0 part
```

Copy the raspbian image on the SD card _(replace XXX with your SD card device, e.g. /dev/mmcblk0)_.
```
$ sudo dd if=2017-11-29-raspbian-stretch.img of=/dev/XXX bs=4M conv=fsync
4919918592 bytes (4,9 GB, 4,6 GiB) copied, 40,6631 s, 121 MB/s
$ sudo sync
```
On older dd version you will not see any progress, just wait until the command is finished (takes 5-20min).

Remove the SD card from your computer and put it into the Pi.


## Initial setup of Raspbian

Connect a keyboard, a display and the WiFi-USB-adapter to your Pi and power it on.

The PIXEL desktop will boot. Open a terminal (CTRL+ALT+T).


### Localisation

```
$ sudo raspi-config
```

Main Menu > _4 Localisation Options_ >  _I1 Change Locale_  
Mark your locale (e.g. _de_DE-UTF-8 UTF-8_), plus the default one _en_GB.UTF-8 UTF-8_.
As default select _en_GB.UTF-8 UTF-8_.

Main Menu > _4 Localisation Options_ >  _I2 Change Timezone_  
Select your timezone.

Main Menu > _4 Localisation Options_ >  _I3 Change Keyboard Layout_  
Select your keymap.

Main Menu > _4 Localisation Options_ >  _I4 Change Wi-fi Country_  
Select your country.

<Finish> the Config dialog and reboot the Pi.

```
$ sudo reboot
```


### Setup WiFi

Check if the WiFi adapter is working.

```
$ iwlist wlan0 scan | grep SSID
```

It should print out all WiFi Accesspoints in your area. If not, troubleshoot first before going on.

Setup WiFi.
```
$ wpa_passphrase "YOUR-WIFI-NAME" "PASSWORD-FOR-WIFI" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
$ sudo wpa_cli -i wlan0 reconfigure
```

Try connection.

```
$ sudo dhclient -r
$ sudo dhclient wlan0
$ ping google.de
```

Reboot the Pi.

```
$ sudo reboot
```

Check if network connection is established automatically after reboot.

```
$ ping google.de
```


### Standard config

Update the system.

```
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo reboot
```

Raspi-Config

```
$ sudo raspi-config
```

Things you should do in the config dialog:
- 8 Update
- 1 Change user password
- 2 Network Options > N1 Hostname _(give your pi a name)_


update raspi-config
[extend file system → reboot] // newer versions: automatically done on first boot
locale
keyboard
timezone
wifi-country
boot options
ssh
password
[hostname, MemorySplit, overclock]








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