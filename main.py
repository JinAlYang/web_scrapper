import csv
from extractors.dabang import extract_dabang_data
from extractors.dabang import extract_details


dabang = extract_dabang_data()

codes = []
f = open("./dabang_rscodes.csv", "r", errors="", newline="")

ex = csv.reader(f)
for line in ex:
    codes.append(line)

f.close()
extract_details(codes)
