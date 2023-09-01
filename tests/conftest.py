import os

CURRENT_FILE_PATH = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(CURRENT_FILE_PATH)
RESOURCE_PATH = os.path.join(DIR_NAME, 'resources')

xlsx_path = os.path.join(RESOURCE_PATH,'file_example_XLSX_50.xlsx')
xls_path = os.path.join(RESOURCE_PATH, 'file_example_XLS_10.xls')
pdf_path = os.path.join(RESOURCE_PATH, 'docs-pytest-org-en-latest.pdf')
csv_path = os.path.join(RESOURCE_PATH, 'new_csv.csv')
zip_path = os.path.join(RESOURCE_PATH, 'new_zip.zip')