#!/bin/bash

# Hitung ukuran folder webapp/images dalam byte
USAGE=$(du -sb /home/linuxmint/final-destination-12-main/webapp/images | awk '{print $1}')

# Simpan ke format metric Prometheus
echo "webapp_images_usage_bytes $USAGE" > /var/lib/node_exporter/textfile_collector/images_usage.prom
