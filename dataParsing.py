import csv
import json
import xml.etree.ElementTree as ET

# Function to convert tab-delimited file to CSV
def tsv_to_csv(file_path, encoding='ISO-8859-1'):
    csv_file_path = file_path.replace('.txt', '.csv')
    with open(file_path, 'r', encoding=encoding, errors='replace') as tsvfile, open(csv_file_path, 'w', newline='', encoding=encoding) as csvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        csv_writer = csv.writer(csvfile)
        for row in tsv_reader:
            csv_writer.writerow(row)
    return csv_file_path

# Function to convert tab-delimited file to JSON
def tsv_to_json(file_path, encoding='ISO-8859-1'):
    json_file_path = file_path.replace('.txt', '.json')
    data = []
    with open(file_path, 'r', encoding=encoding, errors='replace') as tsvfile:
        tsv_reader = csv.DictReader(tsvfile, delimiter='\t')
        for row in tsv_reader:
            data.append(row)
    with open(json_file_path, 'w', encoding=encoding) as jsonfile:
        json.dump(data, jsonfile, indent=4)
    return json_file_path

# Function to convert tab-delimited file to XML
def tsv_to_xml(file_path, encoding='ISO-8859-1'):
    xml_file_path = file_path.replace('.txt', '.xml')
    with open(file_path, 'r', encoding=encoding, errors='replace') as tsvfile:
        tsv_reader = csv.DictReader(tsvfile, delimiter='\t')
        root = ET.Element("root")
        for row in tsv_reader:
            entry = ET.SubElement(root, "entry")
            for key, value in row.items():
                child = ET.SubElement(entry, key)
                child.text = value
    tree = ET.ElementTree(root)
    tree.write(xml_file_path)
    return xml_file_path

# Function to convert file based on the format argument
def convert_file(file_path, format_arg, encoding='ISO-8859-1'):
    if format_arg == '-c':
        return tsv_to_csv(file_path, encoding)
    elif format_arg == '-j':
        return tsv_to_json(file_path, encoding)
    elif format_arg == '-x':
        return tsv_to_xml(file_path, encoding)
    else:
        raise ValueError("Invalid format argument. Use '-c' for CSV, '-j' for JSON, or '-x' for XML.")

# The format argument should be one of '-c', '-j', or '-x'
# Replace 'NFL Offensive Player stats, 1999-2013.txt' with the correct path if necessary
output_file_path = convert_file('NFL Offensive Player stats, 1999-2013.txt', '-c')
output_file_path = convert_file('NFL Offensive Player stats, 1999-2013.txt', '-j')
output_file_path = convert_file('NFL Offensive Player stats, 1999-2013.txt', '-x')

