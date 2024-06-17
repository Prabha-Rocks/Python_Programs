import os
from pypdf import PdfReader, PdfWriter

def merge_pdfs(pdf_list, output_filename):
    pdf_writer = PdfWriter()

    for pdf in sorted(pdf_list):
        pdf_reader = PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
    print(f'Merged {len(pdf_list)} PDFs into {output_filename}')

if __name__ == "__main__":
    # Example usage:
    # Ensure these PDF files exist in the same directory as the script or provide the full paths.
    pdf_files = ["document1.pdf", "document2.pdf", "document3.pdf"]
    merge_pdfs(pdf_files, "merged.pdf")
