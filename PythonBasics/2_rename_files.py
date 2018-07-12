import os


def rename_files():
    file_location = r"C:\Users\Mikele\Desktop\IMG - Kopia"

    """ List all files from selected directory """
    file_list = os.listdir(file_location)
    # print(file_list)

    """ Check and update current working directory to specified location """
    initial_dir = os.getcwd()       # get current working directory
    print("Current Working Directory is "+initial_dir)
    os.chdir(file_location)         # change directory
    print("Changed Working Directory to "+file_location)
    print(50*'-')

    counter = 0
    for file in file_list:
        counter += 1

        """ Print current file name """
        print("Old name - "+file)

        """ Creates a table with ASCI code numbers to ignore. Code found at stackoverflow:
        https://stackoverflow.com/questions/39375712/translate-takes-exactly-one-argument-2-given-in-python-error/43135114
        """
        table = file.maketrans("", "", "0123456789_")

        """ Print name without ignored characters and with counter """
        print("New name - "+file.translate(table) + "_"+str(counter))
        #print("New name2 - "+file.lstrip(None, "0123456789"))

        """ Following code will rename files as initially assumed """
        # os.rename(file, file.translate(None, "0123456789"))

    """ Change back current working directory """
    os.chdir(initial_dir)


rename_files()