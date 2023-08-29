import pypdf
import os
from conftest import RESOURCE_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def pdf_test():
    reader = pypdf.PdfReader(os.path.join(RESOURCE_PATH, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    # print(number_of_pages)
    # print(first_page)
    print(text)
    count = 0
    for image_file in first_page.images:
        with open(os.path.join(RESOURCE_PATH, str(count) + image_file.name), 'wb') as fp:
            fp.write(image_file.data)
            count += 1

    assert number_of_pages == 412
    assert text == "pytest Documentation\nRelease 0.1\nholger krekel, trainer and consultant, https://merlinux.eu/\nJul 14, 2022"
    assert count == 1
    assert os.path.isfile(os.path.join(RESOURCE_PATH, '0Im1.png'))
