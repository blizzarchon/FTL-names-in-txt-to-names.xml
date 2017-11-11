def names_to_xml(read_file, write_file):
    # too_long list is just to separate names that won't fit in the crew box,
    # so that you can tell which ones you NEED to edit/fix
    too_long = []

    write_file.write("<nameList race=\"human\" sex=\"female\">\n")

    all_lines = read_file.readlines()
    for line in all_lines:
        # ignore lines with <nameList> tags if XML since they don't have names
        if "nameList" in line: continue
        # strip off whitespace on ends including \n and \t
        line = line.strip()
        # remove wrapped <name> tags if XML
        if ("<name>" and "</name>") in line:
            line = line[line.find(">") + 1:line.rfind("<")]
        # ignore empty lines
        if line == "": continue
        # ampersand catch -- not needed, FTL doesn't mind '&' in XML
        # if "&" in line:
        #     i = line.find("&")
        #     first_half, second_half = line[:i], line[i+1:]
        #     line = first_half + "&amp;" + second_half
        if len(line) > 15:
            too_long.append(line)
            continue
        write_file.write("\t<name>{}</name>\n".format(line))

    # blank separator lines
    write_file.write("\n\n\n\n\n")

    for name in too_long:
        write_file.write("\t<name>{}</name>\n".format(name))

    write_file.write("</nameList>\n")


if __name__ == "__main__":
    reading = input("Enter name of file in this directory to read from:\n")

    with open(reading, 'r') as main_read:
        writing = input("Enter name of new file name to write to.\n")
        with open(writing, 'w') as main_write:
            names_to_xml(main_read, main_write)
