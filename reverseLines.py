#Reverse line of files function
def reverse_lines(infilename. outfilename):
    with open(infilename) as infile, open (outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_file.rstrip()[::-1]}\n')