import json
import csv

def convertQuestionnaireDataToCSV():

    # Specify the input JSON file and output CSV file
    json_file = './database/questionnaire_data.json'
    csv_file = 'questionnaire_data.csv'

    # Load JSON data from the input file
    with open(json_file, 'r') as infile:
        data = json.load(infile)

    # Extract the keys (assuming all entries have the same structure)
    keys = data[0].keys()

    # Write the data to the CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)

        # Write the header row
        writer.writeheader()

        # Write each data entry as a row
        for entry in data:
            writer.writerow(entry)

    print(f"Data has been successfully converted to {csv_file}")


def convertFacialDataToCSV():
    # Specify the input JSON file and output CSV file
    json_file = './database/facial_data.json'
    csv_file = 'facial_data.csv'

    # Load JSON data from the input file
    with open(json_file, 'r') as infile:
        data = json.load(infile)

    # Extract the keys (assuming all entries have the same structure)
    keys = data[0].keys()

    # Write the data to the CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)

        # Write the header row
        writer.writeheader()

        # Write each data entry as a row
        for entry in data:
            writer.writerow(entry)

    print(f"Data has been successfully converted to {csv_file}")


convertQuestionnaireDataToCSV()
convertFacialDataToCSV()