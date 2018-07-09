import re
import sys

try:
    rx_log_filename = sys.argv[1]
except IndexError:
    print "Usage: rx_parse.py <RX log file>"
    sys.exit(1)

rx_lines = [line.rstrip('\n') for line in open(rx_log_filename, 'r')]

for rx_line in rx_lines:
    rx_match = re.match("^.*\$(.*)\*.*$", rx_line)
    if rx_match is not None:
        rx_msg = rx_match.group(1)
        rx_fields = rx_msg.split(',')
        if len(rx_fields) == 8:
            #trkpt_str = '<trkpt lat="'+rx_fields[2]+'" lon="'+rx_fields[3]+'"><ele>'+rx_fields[4]+'</ele><time>0</time></trkpt>'
            #print trkpt_str
            kml_coordinates_str = rx_fields[3]+','+rx_fields[2]+','+rx_fields[4]
            print kml_coordinates_str
