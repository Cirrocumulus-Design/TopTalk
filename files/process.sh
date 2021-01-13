#!/bin/sh

sed -i 's/\\n/\n/g' /tmp/toptalk.raw
sed -i '1d' /tmp/toptalk.raw
sed -i 's/\"\]//' /tmp/toptalk.raw
cat /tmp/toptalk.raw  |awk '{print $9, $1, $3, $5}' |sort -nr | head -100 > /var/www/html/data/toptalk.dat
sed -i 's/,//g' /var/www/html/data/toptalk.dat
sed -i 's/\s/,/g' /var/www/html/data/toptalk.dat
sed -i 's/:/,/g' /var/www/html/data/toptalk.dat
