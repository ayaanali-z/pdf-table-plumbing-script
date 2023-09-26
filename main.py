import os
import pdfplumber
import csv

file_path = os.path.expanduser("~/PDFs/3157/cds_22-23.pdf")

tables = []

with pdfplumber.open(file_path) as pdf:
    for i, page in enumerate(pdf.pages):
        table = page.extract_table()
        if table is not None:
            csv_filename = f"output_table_page_{i+1}.csv"

            with open(csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(table)
