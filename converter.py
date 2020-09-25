import xml.etree.ElementTree as ET
import json
from poppler import load_from_file

pdf_document = load_from_file("./raw_res/book_for_wine.pdf")
print(pdf_document.fonts()[0])
page_1 = pdf_document.create_page(0)
page_1_text = page_1.text()
print(len(page_1.text_list()))
print(page_1.text_list()[1].bbox.top)
print('***')
for tbox in page_1.text_list():
    print(tbox.bbox.top)
    print(page_1.text(tbox.bbox))