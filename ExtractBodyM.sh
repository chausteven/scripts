#!/bin/bash
tail -n +2 ~/Developer/repos/CSB/unix/data/Pacifici2013_data.csv | cut -d ";" -f 2-6 | tr -s ";" " " | sort -r -n -k 6  > BodyM.csv
# tail will remove the header and only take the lines starting from the second line
# cut will seperate the data according to the delimiter ";" and only take columns 2-6
# tr will replace all semicolin with spaces
# sort will sort in reverse order, by numerical order, and only for column 6 then append that data to a file, BodyM.csv
