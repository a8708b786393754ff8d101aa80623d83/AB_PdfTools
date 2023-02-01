import PyPDF4 as pdf

filename = ''

def decrypt(passwd: str, file_name_out: str = "out_PDFUtils.pdf") -> None:
    """Decrypt the file, it displays the corresponding password, copies the pdf,
        the copy is decrypted

    Args:
        passwd (str): Password that warns of a wordlist or user entry
        file_name_out (str, optional):filename of output. Defaults to "out_PDFUtils.pdf".
    """

    file_encrypted = pdf.PdfFileReader(filename, strict=False)
    file_out_decrypted = pdf.PdfFileWriter()

    if file_encrypted.isEncrypted:
        file_encrypted.decrypt(passwd)

        for index in range(file_encrypted.numPages):
            page = file_encrypted.getPage(index)
            file_out_decrypted.addPage(page)

        print(f"Le mot de passe est {passwd}")

    with open(file_name_out, "wb") as f:
        file_out_decrypted.write(f)

def encrypt( pdf_file: str, passwd: str) -> None:
    """Encrypt the pdf file by creating a copy, while keeping the original

    Args:
        pdf_file (str): filename of pdf file for encrypt
        passwd (str): password for encryption
    """

    file = pdf.PdfFileReader(pdf_file, strict=False)
    out = pdf.PdfFileWriter()

    for index in range(file.numPages):
        page = file.getPage(index)
        out.addPage(page)

    out.encrypt(passwd)

    with open(filename, "wb") as f:
        out.write(f)
