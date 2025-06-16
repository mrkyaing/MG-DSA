import csv
# Input and output file paths
input_csv = 'staff-staging.csv'
output_txt = 'staff-staging.txt'
# Open the CSV file and the output text file
with open(input_csv, 'r', newline='', encoding='utf-8') as csv_file, \
open(output_txt, 'w', newline='', encoding='utf-8') as txt_file:
    csv_reader = csv.reader(csv_file)
    txt_writer = csv.writer(txt_file, delimiter='\t')
    # Write each row from the CSV to the tab-delimited file
    for row in csv_reader:
        txt_writer.writerow(row)
print("Conversion complete!")