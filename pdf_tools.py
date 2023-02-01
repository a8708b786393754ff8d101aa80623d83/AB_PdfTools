#! /usr/bin/python3
import cutt_file_parts as cpg
from args import argument
import pdf_utils 

args = argument()
pdf_utils.filename = args.file

if args.encrypt:
    pdf_utils.encrypt(args.file, args.password)

elif args.decrypt:
    if args.password:
        pdf_utils.decrypt(args.password)
    else:
        content, length_cpg = cpg.before_last_lenght_file_element(args.wordlists)
        result_calcul = cpg.calcul(len(content), length_cpg)

        for content in cpg.cutt(content, result_calcul):
            cpg.thread_executor(pdf_utils.decrypt, content, 50)
