

if __name__ == "__main__":
    reading = input("\nEnter name of file in this directory to read from:\n")

    with open(reading, 'r') as main_read:
        writing = input("\nEnter name of new file name to write to.\n")
        with open(writing, 'w') as main_write:
            too_long = []
            main_write.write("<nameList race=\"human\" sex=\"female\">\n")

            all_lines = main_read.readlines()
            for line in all_lines:
                if "nameList" in line: continue
                # strip off whitespace on ends including \n and \t
                line = line.strip()
                # remove <name> tags if XML
                if ("<name>" and "</name>") in line:
                    line = line[line.find(">") +1:line.rfind("<")]
                # ignore empty lines
                if line == "": continue
                # ampersand catch
                # if "&" in line:
                #     i = line.find("&")
                #     first_half, second_half = line[:i], line[i+1:]
                #     line = first_half + "&amp;" + second_half
                if len(line) > 15:
                    too_long.append(line)
                    continue
                main_write.write(
                    "\t<name>{}</name>\n".format(line))
            main_write.write("\n")
            for name in too_long:
                main_write.write(
                    "\t<name>{}</name>\n".format(name))

            main_write.write("</nameList>\n")
