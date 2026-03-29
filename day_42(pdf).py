from pypdf import PdfReader
pdf = PdfReader('CSE.pdf')
page = pdf.pages[0]


print(len(pdf.pages))
print(page)
print(page.extract_text())