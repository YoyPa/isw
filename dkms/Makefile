#!/usr/bin/make -f

MODULES := ec_sys

reverse = $(if $(1),$(call reverse,$(wordlist 2,$(words $(1)),$(1)))) $(firstword $(1))
REVMODS := $(call reverse,$(MODULES))

all: $(MODULES)

$(MODULES):
	$(MAKE) -C "$@"

CLEANMODS := $(addprefix clean-,$(MODULES))
$(CLEANMODS):
	$(MAKE) -C "$(subst clean-,,$@)" clean
clean: $(CLEANMODS)

LOADMODS := $(addprefix load-,$(MODULES))
$(LOADMODS):
	$(MAKE) -C "$(subst load-,,$@)" load
load: $(LOADMODS)

UNLOADMODS := $(addprefix unload-,$(REVMODS))
$(UNLOADMODS):
	$(MAKE) -C "$(subst unload-,,$@)" unload
unload: $(UNLOADMODS)

INSTALLMODS := $(addprefix install-,$(MODULES))
$(INSTALLMODS):
	$(MAKE) -C "$(subst install-,,$@)" install
install: $(INSTALLMODS)

UNINSTALLMODS := $(addprefix uninstall-,$(REVMODS))
$(UNINSTALLMODS):
	$(MAKE) -C "$(subst uninstall-,,$@)" uninstall
uninstall: $(UNINSTALLMODS)

.PHONY: all clean $(MODULES) $(CLEANMODS) $(LOADMODS) $(UNLOADMODS) $(INSTALLMODS) $(UNINSTALLMODS)
