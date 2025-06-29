import fitz  # PyMuPDF

def pdf_to_text(pdf_path, txt_path):
    pdf_document = fitz.open(pdf_path)
    with open(txt_path, 'w', encoding='utf-8') as text_file:
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            # Use "blocks" layout extraction
            blocks = page.get_text("blocks")
            # Sort blocks by top Y coordinate to maintain reading order
            blocks.sort(key=lambda b: b[1])
            for block in blocks:
                text = block[4].strip()
                if text:
                    text_file.write(text + "\n")
            text_file.write("\n\n")
    print("done")
