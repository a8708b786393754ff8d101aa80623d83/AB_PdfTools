import PyPDF4 as pdf
import cutt_file_parts as cpg
import argparse


class PDFUtils:

    def __init__(self, file_name_encrypted: str):
        self.file_name_encrypted = file_name_encrypted

    def decrypt(self, passwd: str, file_name_out: str = "out_PDFUtils.pdf"):
        file_encrypted = pdf.PdfFileReader(
            self.file_name_encrypted, strict=False)
        file_out_decrypted = pdf.PdfFileWriter()

        if file_encrypted.isEncrypted:
            file_encrypted.decrypt(passwd)
            for index in range(file_encrypted.numPages):
                page = file_encrypted.getPage(index)
                file_out_decrypted.addPage(page)
            print(f"Le mot de passe est {passwd}")

        with open(file_name_out, "wb") as f:
            file_out_decrypted.write(f)

    def encrypt(self, pdf_file: str, passwd: str):
        file = pdf.PdfFileReader(pdf_file, strict=False)
        out = pdf.PdfFileWriter()
        num_page = file.numPages
        for index in range(num_page):
            page = file.getPage(index)
            out.addPage(page)

        out.encrypt(passwd)

        with open(self.file_name_encrypted, "wb") as f:
            out.write(f)


def argument():
    argument = argparse.ArgumentParser()
    argument.add_argument("-w", "--wordlists", type=str)
    argument.add_argument("--mode", type=str, default="decrypt",
                          help="Enter a mode (decrypt or encrypt)")
    argument.add_argument("-p", '--password', type=str,
                          help="Enter a password if you choice the method encrypt")
    argument.add_argument("-f", "--file", type=str, required=True)
    return argument.parse_args()


if __name__ == "__main__":
    args = argument()
    pdf_utils = PDFUtils(args.file)

    if args.mode == "encrypt":
        pdf_utils.encrypt(args.file, args.password)

    elif args.mode == "decrypt":
        if args.password:
            pdf_utils.decrypt(args.password)
        else:
            content, length_cpg = cpg.before_last_lenght_file_element(
                args.wordlists)
            result_calcul = cpg.calcul(len(content), length_cpg)

            for content in cpg.cutt(content, result_calcul):
                cpg.thread_executor(content, pdf_utils.decrypt, 50)
