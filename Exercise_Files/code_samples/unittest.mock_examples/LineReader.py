import os


def read_from_file(filename):
    """
    Function to read data in given file
    :param filename: path to the file
    :return:
    """
    if not os.path.exists(filename):
        raise Exception("Bad File")
    infile = open(filename, "r")
    line = infile.readline()
    return line





