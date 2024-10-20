##### Function to input colour into our graphics #####
# www.devdungeon.com/content/colorize-terminal-output-python -> For ANSI escape colour information
# https://www.edlitera.com/blog/posts/python-parentheses -> For cheatsheet on brackets usages
# www.talkpython.fm/episodes/show/227/maintainable-data-science-tips-for-non-developers -> Python tips podcast
# www.talkpython.fm/episodes/show/252/what-scientific-computing-can-learn-from-cs
# www.talkpython.fm/episodes/show/237/a-gut-feeling-about-python

def coloured(seq):
    bcolours = {
        "A" : "\033[92m",
        "C" : "\033[94m",
        "G" : "\033[93m",
        "T" : "\033[91m",
        "U" : "\033[91m",
        "reset" : "\033[0;0m"
    }
    # \033 = Represents ANSI escape characters in Python
        # Can affect colour of characters, bkground, foreground, fonts etc
        # Characters afterward is code that represents the colour
    # Should try out the package colorama -> Helps with shortcuts and presentation

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolours:
            tmpStr += bcolours[nuc] + nuc
        else:
            tmpStr += bcolours["reset"] + nuc
    return tmpStr + "\033[0;0m"
    # have to run this function in the terminal rather than the usual console (??)
        # Type: python main.py

def readtxtfile(filepath):
    """Open a file, read it line by line, strip all newline (\n) characters"""
    with open(filepath, 'r') as f:
        return "".join([l.strip() for l in f.readlines()])

def writetxtfile(filepath, seq, mode='w'):
    """Overwrite the file """
    with open(filepath, mode) as f:
        f.write(seq + '\n')

def read_fasta(filepath):
    """To open, read and extract lines from a FASTA file"""
    with open(filepath, 'r') as f:
        fastafile = [l.strip() for l in f.readlines()]

    fastadict = {}
    fastalabel = ""

    for line in fastafile:
        if '>' in line:
            fastalabel = line
            fastadict[fastalabel] = ""
        else:
            fastadict[fastalabel] += line
    return fastadict