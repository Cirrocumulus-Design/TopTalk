#! /usr/bin/python

import socket

f= open("/var/www/html/data/toptalk.html","w+")

# begin the table
f.write("<table class='responstable'>\n")

# column headers
f.write("<tr>")
f.write("<td>Mbs</td>")
f.write("<td>Protocol</td>")
f.write("<td>Destination</td>")
f.write("<td>Host</td>")
f.write("<td>Port</td>")
f.write("<td>Source</td>")
f.write("<td>Host</td>")
f.write("<td>Port</td>")
f.write("</tr>\n")

infile = open("/var/www/html/data/toptalk.dat","r")

for line in infile:
    row = line.split(",")
    mbs = row[0]
    proto = row[1]
    dest = row [2]
    dp = row[3]
    srcip = row[4]
    sp = row[5]

    conv = float(125000)
    fqdn_d = socket.getfqdn(dest)
    try:
      fqdn_s = socket.gethostbyaddr(srcip)
      src = fqdn_s[0]
    except:
      src =srcip
    long_mbs = float(mbs)
    long_mbs = (long_mbs/conv)
    mbs = str(long_mbs)

    f.write("<tr>")
    f.write("<td>%s</td>" % mbs)
    f.write("<td>%s</td>" % proto)
    f.write("<td>%s</td>" % dest)
    f.write("<td><a href=https://www.whois.com/whois/%s target=_blank>%s</a></td>" % (fqdn_d, fqdn_d))
    f.write("<td>%s</td>" % dp)
    f.write("<td>%s</td>" % srcip)
    f.write("<td>%s</td>" % src)
    f.write("<td>%s</td>" % sp)
    f.write("</tr>\n")

# end the table
f.write("</table>")
f.close()
