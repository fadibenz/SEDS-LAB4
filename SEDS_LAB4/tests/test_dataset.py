import csv
import SEDS_LAB4.SEDS_LAB4.modeling.model as model
import pytest



# Load your dataset from the CSV file
dataset = []
with open('../../data/raw/house_price.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)

# Test if the function correctly handles rows with missing values
# Parametrize the test function to iterate through each row in the dataset
@pytest.mark.parametrize("input_row", dataset)
def test_row_to_list_with_missing_values(input_row):
    input_string = ' '.join(input_row)  # Convert list to string

    input_list = input_string.split(';')
    assert '' not in input_list