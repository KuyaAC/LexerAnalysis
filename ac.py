with open("DEV.ecpp", "r") as input_file:
    # read the contents of the file
    contents = input_file.read()

# use regex to find all quoted text
matches = re.findall(r'"([^"]*)"', contents)

# replace the quoted text with the unquoted text + "4"
for match in matches:
    if "const" in match:
        contents = contents.replace('"' + match + '"', match + "3")
    else :
        contents = contents.replace('"' + match + '"', match + "4")

# open the output file
with open("DEV2.ecpp", "w") as output_file:
    # write the modified contents to the output file
    output_file.write(contents)