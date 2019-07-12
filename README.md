# ISW / Ice-Sealed Wyvern
<img src="https://github.com/YoyPa/isw/blob/master/image/isw.svg" alt="" width="25%" align="right">

- isw started as an equivalent of "control tools by pherein" but under linux.
- It is meant to alter fan profiles of MSI laptops.
- Profiles for supported laptops are located in <a href="https://github.com/YoyPa/isw/blob/master/etc/isw.conf">/etc/isw.conf</a>.
- Check <a href="https://github.com/YoyPa/isw/blob/master/etc/isw.conf">/etc/isw.conf</a>. comments for more details.

## Warning
- Use it at your own risk !
- Secure boot can prevent access to the EC
- isw is made/tested with MSI GS40 6QE under Arch/Manjaro, other laptops depend on user contribution.
- Check that your EC (Embedded Controler) work the same way, you can find documentation on the <a href="https://github.com/YoyPa/isw/wiki/How-EC-work-(for-GS40-6QE-at-least)">wiki</a>.

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
usage: isw [-h] [-b B B] [-c] [-f F] [-p P] [-r R] [-s S S] [-w W]

optional arguments:
  -h, --help  show this help message and exit
  -b B B      ┬ activate or disable CoolerBoost
              ├ replace 1st B with PROFILE_NAME
              └ replace 2nd B with on OR off

  -c          ─ show an EC dump

  -f F        ┬ show profile in EC update file
              └ replace F with FILE_NAME

  -p P        ┬ show current profile in EC
              └ replace P with PROFILE_NAME

  -r R        ┬ show realtime CPU+GPU temp and fan speed from EC
              └ replace R with PROFILE_NAME

  -s S S      ┬ set a single value into EC
              ├ replace 1st S with ADDRESS in hexadecimal (0x00)
              └ replace 2nd S with VALUE   in decimal     (00)

  -w W        ┬ write into EC
              └ replace W with PROFILE_NAME

┌─ TIPS ──────────────────────────────────────────────────────────────────┐
│ Set your config in '/etc/isw.conf'.                                     │
│ Arguments order is relevant, -c and -p can be used twice. Example:      │
│ isw -cw PROFILE_NAME -c will show you EC dump before and after change.  │
├─ SUPPORT ───────────────────────────────────────────────────────────────┤
│ Help me support your laptop by providing following command output:      │
│ isw -cp MSI_ADDRESS_DEFAULT                                             │
│ via https://github.com/YoyPa/isw (open an issue).                       │
├─ NAME ──────────────────────────────────────────────────────────────────┤
│ ISW is MSI at 180°                                                      │
│ It mean Ice-Sealed Wyvern in opposition to MSI's "unleash the dragon"   │
└─────────────────────────────────────────────────────────────────────────┘
```
<b>NB: all option exept -h need priviledges.</b>


## Launch at startup/resume
You can launch ```isw -w [PROFILE_NAME]``` at startup/resume via systemd with isw@.service (need priviledges):
```
systemctl enable isw@[PROFILE_NAME].service
```

## TODO
```
- Daemonisation
	- Launch at startup                            done
	- launch after resume (hibernation/suspend)    done
	- Launch at event(power source change)         seems hard to achieve
```
