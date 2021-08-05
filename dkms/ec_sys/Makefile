obj-m := ec_sys.o

ifndef KVER
KVER := $(shell uname -r)
endif
ifndef KDIR
KDIR := /lib/modules/$(KVER)/build
endif

PWD := $(shell pwd)

default:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean

install:
	$(MAKE) -C $(KDIR) M=$(PWD) modules_install

uninstall:
	$(MAKE) -C $(KDIR) M=$(PWD) modules_uninstall

load:
	insmod ec_sys.ko

unload:
	-rmmod ec_sys
