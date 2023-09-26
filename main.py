import os
import pdfplumber
import csv

file_path = os.path.expanduser("~/PDFs/3157/cds_22-23.pdf")
# Define file path for whatever specific file you need. 
tables = [] # Array that stores all the tables 

with pdfplumber.open(file_path) as pdf:
    for i, page in enumerate(pdf.pages):
        table = page.extract_table() # Simple command 
        if table is not None: # If there's a table on the page, it extracts. 
            csv_filename = f"output_table_page_{i+1}.csv"
            # WRITES CSV OF EXTRACTED TABLE 
            with open(csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(table)
