#!/bin/bash

# Define the boot image path on the device
BOOT_IMAGE_PATH="/dev/block/by-name/boot"

# Define the destination path on the local machine
DESTINATION_PATH="/path/to/save/boot.img"

# Pull the boot image from the device
adb pull $BOOT_IMAGE_PATH $DESTINATION_PATH

# Compress the boot image to a .gzip file
gzip $DESTINATION_PATH

echo "Boot image has been copied and compressed to $DESTINATION_PATH.gz"
