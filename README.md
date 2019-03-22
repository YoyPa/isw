# ISW / Ice-Sealed Wyvern

## Warning
- isw was made/tested with MSI GS40 6QE, check that your EC (Embedded Controler) work the same way before trying.
- You can find documentation on the <a href="https://github.com/YoyPa/isw/wiki/How-EC-work-(for-GS40-6QE-at-least)">wiki</a>
- isw is only tested under Arch/Manjaro (systemd).
- Use it at your own risk !

## Purpose
isw was made as an equivalent of "control tools by pherein" but under linux.

### In details
- Replace <b>temp</b> at <b>address</b>,<b>address</b>+1,...,<b>address</b>+5.
- <b>address</b> are in hex
- <b>temp</b> are in °C.
- EC contain 7 <b>temp</b>, 6 of them will be edited, last one is left at 0x64(100).
- Profiles for supported laptops are located in <a href="https://github.com/YoyPa/isw/blob/master/etc/isw.conf">/etc/isw.conf</a>.

## How to use it ?
- It need ```ec_sys``` module with option ```write_support=1```, there are two scenario to set that:
  - ec_sys is a builtin kernel module:
    - add ```ec_sys.write_support=1``` in ```/etc/default/grub``` (Arch AUR package can't do it for you).
    - then update your grub and reboot.
  - ec_sys is not a builtin kernel module:
    - copy both ```isw-ec_sys.conf``` files provided (/etc/foo) with same path (Arch AUR package will do it for you).
    - then reboot OR ```modprobe ec_sys write_support=1```.
- Use option ```-c``` to read EC <b>and/or</b> ```-w [PROFILE_NAME]``` to write in EC.
- Option ```-c``` can be used alone or in conjuction with ```-w``` like ```-cw [foo]``` ```-w [foo] -c``` ```-cw [foo] -c``` to print EC before/after write or both.

<b>NB: all option exept -h need priviledges.</b>

/!\ GIF are outdated /!\

<a href="https://github.com/YoyPa/isw/blob/master/gif/isw-c.gif">
	<img src="https://github.com/YoyPa/isw/blob/master/gif/isw-c.gif" width="427" height="480" border="10" />
</a>
<a href="https://github.com/YoyPa/isw/blob/master/gif/isw-w.gif">
	<img src="https://github.com/YoyPa/isw/blob/master/gif/isw-w.gif" width="427" height="480" border="10" />
</a>
<a href="https://github.com/YoyPa/isw/blob/master/gif/isw-cwc.gif">
	<img src="https://github.com/YoyPa/isw/blob/master/gif/isw-cwc.gif" width="427" height="480" border="10" />
</a>
<a href="https://github.com/YoyPa/isw/blob/master/gif/isw-h.gif">
	<img src="https://github.com/YoyPa/isw/blob/master/gif/isw-h.gif" width="427" height="480" border="10" />
</a>

### isw -c
It check your EC with:
```
od -A x -t x1z /sys/kernel/debug/ec/ec0/io
```

## TODO
- Daemonisation ?
	- Launch at startup
	- Launch at event(power source change)
