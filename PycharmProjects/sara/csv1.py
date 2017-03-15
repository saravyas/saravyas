import sys
import csv

csv.field_size_limit(sys.maxsize)

txt_file = r"loans.txt"
csv_file = r"loanscsvs.csv"

in_txt = csv.reader(open(txt_file, "rb"), delimiter =" ")
out_csv = csv.writer(open(csv_file, 'wb'))

out_csv.writerows(in_txt)
print 'done! go check your loancsvs.csv file'
