#!/usr/bin/python

from openpyxl import Workbook
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} in.txt out.xlsx")
    sys.exit(1)

txt=sys.argv[1]
xlsx=sys.argv[2]

wb = Workbook(write_only=True)
ws = wb.create_sheet()

with open(txt,"r") as f:
    ls = f.readlines()

for l in ls:
    ws.append(list(l))

wb.save(xlsx)


