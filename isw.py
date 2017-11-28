#! /usr/bin/python

# IMPORTS
import sys
import os
from optparse import OptionParser

# VARIABLES GLOBALES
EC_IO_FILE="/sys/kernel/debug/ec/ec0/io"
EC_SYS_STARTUP="/etc/modules-load.d/isw-ec_sys.conf"
EC_SYS_STARTUP_OPT="/etc/modprobe.d/isw-ec_sys.conf"
DUMP_POS=""
ADDRESS=0x6a
VALUE=68
X=int(5)

# FONCTIONS
# option -l
def check_ec_sys(option, opt, value, parser):
	if not os.path.exists(EC_IO_FILE):
		os.system("modprobe ec_sys write_support=1")
		print("ec_sys module have been loaded")
	else:
		print("ec_sys module is already loaded")

# option -s
def check_ec_sys_startup(option, opt, value, parser):
	if not os.path.exists(EC_SYS_STARTUP):
		with open(EC_SYS_STARTUP,"xt") as file:
			file.write("ec_sys")
		print(EC_SYS_STARTUP+" created")
	else:
		print("nothing added in module-load.d")
	if not os.path.exists(EC_SYS_STARTUP_OPT):
		with open(EC_SYS_STARTUP_OPT,"xt") as file:
			file.write("options ec_sys write_support=1")
		print(EC_SYS_STARTUP_OPT+" created")
	else:
		print("nothing added in modprobe.d")

# option -a
def change_address(option, opt, value, parser):
	global ADDRESS
	ADDRESS=int(value)

# option -v
def change_value(option, opt, value, parser):
	global VALUE
	VALUE=int(value)

# option -x
def change_x(option, opt, value, parser):
	global X
	X=int(value)

# option -w
def ec_write(option, opt, value, parser):
	global ADDRESS
	global VALUE
	global DUMP_POS
	DUMP_POS="after modification"
	print('\r')
	with open(EC_IO_FILE,"wb") as file:
		for i in range(6):
			file.seek(ADDRESS)
			file.write(bytearray((VALUE,)))
			print('Value '+hex(VALUE)+'('+str(VALUE)+'°C)'+' written at '+hex(ADDRESS)+'(byte'+str(ADDRESS)+')')
			ADDRESS=ADDRESS+1
			VALUE=VALUE+X

# option -c
def ec_check(option, opt, value, parser):
	print('\nEC dump '+str(DUMP_POS))
	print('\x1b[0;32;1m' + '       00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F' + '\x1b[0m')
	os.system("od -A x -t x1z "+str(EC_IO_FILE))

def main():
	# permet l'utilisation d'arguments
	# callback permet l'appel d'une fonction
	parser = OptionParser(epilog=
"""TIPS ------------------------------------------------------------------------
Fan will start spinning at VALUE (°C) and increase speed every XJUMP.		 
EC contain 7 values, 6 of them will be edited, last one is left at 0x64(100).
Please ensure that VALUE+5*XJUMP stay below 0x64(100).						 
For options -a -v -x, decimal and hexadecimal values are allowed.			 
NAME ------------------------------------------------------------------------
ISW is MSI at 180°														 	
ISW mean ice-sealed wyvern in opposition to MSI's "unleash the dragon"		 
-----------------------------------------------------------------------------
""")
	parser.add_option("-l", "--load", action="callback", callback=check_ec_sys,
					  help="look for ec_sys module and load it if needed")
	parser.add_option("-s", "--startup", action="callback", callback=check_ec_sys_startup,
					  help="configure ec_sys module for startup (systemd)")
	parser.add_option("-a", "--address", action="callback", callback=change_address, type="int",
					  help="specify starting address (default: 0x6a)")
	parser.add_option("-v", "--value", action="callback", callback=change_value, type="int",
					  help="specify starting value (°C) (default: 68)")
	parser.add_option("-x", "--xjump", action="callback", callback=change_x, type="int",
					  help="specify by how much value will increment (default: 5)")
	parser.add_option("-w", "--write", action="callback", callback=ec_write,
					  help="write into EC, always keep this option at the end")
	parser.add_option("-c", "--check", action="callback", callback=ec_check,
					  help="show an EC dump, -cw=before -wc=after -cwc=both")
	(options, args) = parser.parse_args()

if __name__ == "__main__":
    main()
