# Open the input file for reading
with open("sample.ecpp", "r") as file:
    # Open the output file for writing
    with open("output.ecpp", "w") as output:
        # Iterate over each line in the input file
        for line in file:
            # Check if the line contains "const"
            if "const" in line:
                # Split the line into words
                words = line.split()
                # Iterate over each word
                for i in range(len(words)):
                    # Check if the word is a number
                    if words[i].isdigit():
                        # Append "c" to the end of the number
                        words[i] += "c"
                # Join the modified words back into a string
                new_line = " ".join(words)
                # Write the modified line to the output file
                output.write(new_line + "\n")
            # Check if the line starts with "#"
            elif line.startswith("#"):
                # Do nothing, ignore the line
                pass
            else:
                # Write the original line to the output file
                output.write(line)