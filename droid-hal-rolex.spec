# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device rolex
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 4a

%define installable_zip 1

%define straggler_files \
   /usr/bin/test_nfc\
   /usr/lib/libnfc_ndef_nxp.so\
   /usr/lib/libnfc_ndef_nxp.so.1\
   /usr/lib/libnfc_ndef_nxp.so.1.0.0\
   /usr/lib/libnfc_nxp.so\
   /usr/lib/libnfc_nxp.so.1\
   /usr/lib/libnfc_nxp.so.1.0.0\
   /usr/lib/pkgconfig/libnfc_ndef_nxp.pc\
   /usr/lib/pkgconfig/libnfc_nxp.pc\
   %{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

