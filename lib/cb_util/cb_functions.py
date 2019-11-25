import logging




#We take the file that the program outputted and move it back to the shared folder
# with the following edits: Add new base link. Remove "Searching in" line.

def fix_html(file_str):

        #CODE
        #Updated base link:
        base_html = '<base href="http://papers.genomics.lbl.gov/cgi-bin/" target="_blank">'
        
        #finding and inserting the base link:
        file_list = file_str.split('\n')

        #DEBUG
        logging.info("Number of lines in output file: " + str(len(file_list)))

        #CODE
        #inserting the base html line
        new_file_list = file_list[:8] + [base_html] + file_list[8:]
        
        #finding lines to remove
        bad_lines = []

        #finding a line to replace
        replace_line = -1

        #Finding and removing searching in line
        for i in range(len(new_file_list)):
            if '(ababffffbaba)' in new_file_list[i]:
                bad_lines.append(i)
            elif 'Running ublast with E' in new_file_list[i]:
                bad_lines.append(i)
            elif 'relevant proteins in Proteome with' in new_file_list[i]:
                bad_lines.append(i)
            elif 'Running ublast against the 6-frame translation.' in new_file_list[i]:
                replace_line = i

        #Replacing last ublast line:
        if replace_line != -1:
            new_file_list[replace_line] = new_file_list[replace_line].replace('ublast','mmseqs2')
        else:
            logging.critical("Could not find ublast line")
        #Going through the indeces in reverse and removing the lines
        bad_lines.sort()
        for j in range(len(bad_lines)):
            i = len(bad_lines) - j - 1
            ind = bad_lines[i]
            new_file_list = new_file_list[:ind] + new_file_list[ind+1:]


        
        new_file_str = '\n'.join(new_file_list)
        return new_file_str        







