# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device rolex
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 4a

%define installable_zip 1

%define straggler_files \
   /bugreports\
   /cache\
   /d\
   /nonplat_file_contexts\
   /nonplat_hwservice_contexts\
   /nonplat_property_contexts\
   /nonplat_seapp_contexts\
   /nonplat_service_contexts\
   /plat_file_contexts\
   /plat_hwservice_contexts\
   /plat_property_contexts\
   /plat_seapp_contexts\
   /plat_service_contexts\
   /sdcard\
   /vndservice_contexts\
   %{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

