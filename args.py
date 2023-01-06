from argparse import ArgumentParser

def argument():
    argument = ArgumentParser()
    argument.add_argument("-w", "--wordlists", type=str)
    argument.add_argument("--mode", type=str, default="decrypt",help="Enter a mode (decrypt or encrypt)")
    argument.add_argument("-p", '--password', type=str,help="Enter a password if you choice the method encrypt")
    argument.add_argument("-f", "--file", type=str, required=True)
    
    return argument.parse_args()