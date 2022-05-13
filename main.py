import tabula
import os

while(True):
    # grab the path to pdf
    print("\nTo Exit Running Press Ctrl + C")
    print("Input PDF path...")
    PDF_Path = input()

    # read PDF file
    tables = tabula.read_pdf(PDF_Path, pages="all")

    # 1) save them in a folder
    folder_name = "tables"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    # iterate over extracted tables and export as excel individually
    for i, table in enumerate(tables, start=1):
        table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)

    # 2) convert all tables of a PDF file into a single CSV file
    # supported output_formats are "csv", "json" or "tsv"
    tabula.convert_into(PDF_Path, "output.csv", output_format="csv", pages="all")

    # 3) convert all PDFs in a folder into CSV format
    # `pdfs` folder should exist in the current directory
    tabula.convert_into_by_batch("pdfs", output_format="csv", pages="all")