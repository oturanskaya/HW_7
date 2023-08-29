import os
import csv
from conftest import RESOURCE_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv():
    with open(os.path.join(RESOURCE_PATH, 'new_csv.csv'), 'w', newline="") as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(os.path.join(RESOURCE_PATH, 'new_csv.csv')) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        catalog = []
        for row in csvreader:
            catalog.append(row)
            print(row)

        assert catalog[0] == ['Bonny', 'Born', 'Peter']
        assert catalog[1] == ['Alex', 'Serj', 'Yana']

    os.remove(os.path.join(RESOURCE_PATH, 'new_csv.csv'))
