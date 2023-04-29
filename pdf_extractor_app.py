import easygui as gui
from PyPDF2 import PdfReader, PdfWriter


# 1. Ask the user to select a PDF ﬁle to open.

input_path = gui.fileopenbox(title="Select a PDF to extract", default="*.pdf")

# 2. If user presses cancel, exit the program.

if input_path is None:
    exit()

# 3. Ask for a starting page number.

page_to_extract_from = gui.enterbox(
    msg="Enter the page number you want to extract from", title="Page Number")

# 4. If the user does not enter a starting page number, exit the program.

if page_to_extract_from is None:
    exit()

# 5. Valid page numbers are positive integers.

page_to_extract_from = int(page_to_extract_from)

while page_to_extract_from < 0:
    warning_message = gui.msgbox(msg="Invalid Page Number", title="Invalid")
    page_to_extract_from = gui.enterbox(
        msg="Enter the page number you want to extract from", title="Page Number")
    page_to_extract_from = int(page_to_extract_from)

# 6. Ask for an ending page number.

page_till = gui.enterbox(
    msg="Enter the page number you want to extract upto", title="Page Number")

if page_till is None:
    exit()

page_till = int(page_till)

while page_to_extract_from < 0:
    warning_message = gui.msgbox(msg="Invalid Page Number", title="Invalid")
    page_till = gui.enterbox(
        msg="Enter the page number you want to extract upto", title="Page Number")
    page_till = int(page_till)

# 7. Ask for the location to save the extracted pages.

extracted_pages_path = gui.filesavebox(title="Save as...", default="*.pdf")

if extracted_pages_path is None:
    exit()

while input_path == extracted_pages_path:
    warning_message = gui.msgbox(msg="Cannot overwrite", title="Error")
    extracted_pages_path = gui.filesavebox(title="Save as...", default="*.pdf")

# 8.Perform the page extraction:

pdf_reader = PdfReader(input_path)
pdf_writer = PdfWriter()

with open(extracted_pages_path, mode="wb") as output_file:
    for n in range(page_to_extract_from-1, page_till):
        page = pdf_reader.pages[n]
        pdf_writer.add_page(page)
    pdf_writer.write(output_file)
