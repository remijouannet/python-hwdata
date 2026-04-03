#!/usr/bin/python

from hwdata import PCI, USB, PNP

# for obtaining real id of your devices you can use package python-gudev

pci_vendor_id = '1002'
pci_device_id = '687f'
pci_subsystem_id = '1043:04c4'
pci_class = ""
pci_subclass = ""
pci_prog_if = ""
usb_vendor_id = '03f0'
usb_device_id = '1f12'


pci = PCI()
print("Vendor: %s" % pci.get_vendor(pci_vendor_id))
print("Device: %s" % pci.get_device(pci_vendor_id, pci_device_id))
print("Subsystem: %s" % pci.get_subsystem(pci_vendor_id, pci_device_id, pci_subsystem_id))
print("Class: %s" % pci.get_class("0c"))
print("subclass: %s" % pci.get_subclass("0c", "07"))
print("prog_if: %s" % pci.get_prog_if("0c", "07", "02"))


usb = USB()
print("Vendor: %s" % usb.get_vendor(usb_vendor_id))
print("Device: %s" % usb.get_device(usb_vendor_id, usb_device_id))

pnp = PNP()
print("Vendor: %s" % pnp.get_vendor('AAA'))
