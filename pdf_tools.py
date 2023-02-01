import cutt_file_parts as cpg
from args import argument
from pdf_utils import PDFUtils

args = argument()
pdf_utils = PDFUtils(args.file)

if args.mode == "encrypt":
    pdf_utils.encrypt(args.file, args.password)

elif args.mode == "decrypt":
    if args.password:
        pdf_utils.decrypt(args.password)
    else:
        content, length_cpg = cpg.before_last_lenght_file_element(args.wordlists)
        result_calcul = cpg.calcul(len(content), length_cpg)

        for content in cpg.cutt(content, result_calcul):
            cpg.thread_executor(content, pdf_utils.decrypt, 50)
