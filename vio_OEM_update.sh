#!/bin/bash

# Function to detect MediaTek (MTK) hardware
detect_mtk() {
  echo "Detecting MediaTek (MTK) hardware..."
  adb shell getprop ro.mediatek.platform
}

# Function to detect Qualcomm hardware
detect_qualcomm() {
  echo "Detecting Qualcomm hardware..."
  adb shell getprop ro.board.platform
}

# Function to detect eMMC hardware
detect_emmc() {
  echo "Detecting eMMC hardware..."
  adb shell cat /sys/class/block/mmcblk0/device/name
}

# Detect MTK hardware
mtk_hardware=$(detect_mtk)
if [ -n "$mtk_hardware" ]; then
  echo "MediaTek (MTK) hardware detected: $mtk_hardware"
else
  echo "MediaTek (MTK) hardware not detected."
fi

# Detect Qualcomm hardware
qualcomm_hardware=$(detect_qualcomm)
if [ -n "$qualcomm_hardware" ]; then
  echo "Qualcomm hardware detected: $qualcomm_hardware"
else
  echo "Qualcomm hardware not detected."
fi

# Detect eMMC hardware
emmc_hardware=$(detect_emmc)
if [ -n "$emmc_hardware" ]; then
  echo "eMMC hardware detected: $emmc_hardware"
else
  echo "eMMC hardware not detected."
fi
