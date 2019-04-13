# ISW / Ice-Sealed Wyvern

## Warning
- isw was made/tested with MSI GS40 6QE, other laptops depend on user contribution and can't be tested by myself.
- Check that your EC (Embedded Controler) work the same way before trying.
- You can find documentation on the <a href="https://github.com/YoyPa/isw/wiki/How-EC-work-(for-GS40-6QE-at-least)">wiki</a>.
- isw is only tested under Arch/Manjaro (systemd).
- Use it at your own risk !

## Purpose
isw was made as an equivalent of "control tools by pherein" but under linux.

### In details
- Replace <b>temp/fan_speed</b> at <b>temp/fan_speed_address</b>,<b>temp/fan_speed_address</b>+1,[...],<b>temp/fan_speed_address</b>+5.
- <b>temp/fan_speed_address</b> are in hex.
- <b>temp/fan_speed</b> are in °C/%.
- EC contain 7 <b>temp</b>, 6 of them will be edited, last one is left at 0x64(100).
- Profiles for supported laptops are located in <a href="https://github.com/YoyPa/isw/blob/master/etc/isw.conf">/etc/isw.conf</a>.

## How to install
### Package or not package ?
- If you are using archlinux or a derivative you can install it from AUR:
```
yay -S isw
```
- If you are on a different distro family:
  - Clone ```git clone https://github.com/YoyPa/isw```
  - Then look at this <a href="https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=isw">PKGBUILD</a> to know where to put files.
  - /!\ Path can change a bit depending on the distro /!\

### Builtin or not builtin ?
- It need ```ec_sys``` module with option ```write_support=1```, there are two scenario to set that:
  - ec_sys is a builtin kernel module:
    - add ```ec_sys.write_support=1``` in ```/etc/default/grub``` (Arch AUR package can't do it for you).
    - then update your grub and reboot.
  - ec_sys is not a builtin kernel module:
    - copy both ```isw-ec_sys.conf``` files provided (/etc/mod[...]) with same path (Arch AUR package will do it for you).
    - then reboot OR ```modprobe ec_sys write_support=1```.

## How to use it ?
```
usage: isw [-h] [-r R] [-w W] [-s S S] [-c]

optional arguments:
  -h, --help  show this help message and exit
  -r R        ┬ show realtime CPU+GPU temp and fan speed from EC
              └ replace R with PROFILE_NAME
  -w W        ┬ write into EC
              └ replace W with PROFILE_NAME
  -s S S      ┬ set a single value into EC
              └ replace first S with address(hex) second S with value(dec)
  -c          ─ show an EC dump

--- TIPS --------------------------------------------------------------------
-- Set your config in '/etc/isw.conf'.                                     --
-- Arguments order is relevant, -c can be used twice. Example:             --
-- isw -c -w [Profile] -c will show you EC dump before and after change.   --
-----------------------------------------------------------------------------
```
<b>NB: all option exept -h need priviledges.</b>


## Launch at startup
You can launch ```isw -w [PROFILE_NAME]``` at startup via systemd with isw@.service (need priviledges):
```
systemctl enable isw@[PROFILE_NAME].service
```

## TODO
```
- Daemonisation
	- Launch at startup								done
	- launch after resume (hibernation/suspend)		looking into it
	- Launch at event(power source change)			seems hard to achieve
```
