
def remove_comments(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    with open(file_name, "w") as file:
        for line in lines:
            if not line.startswith("#"):
                file.write(line)

remove_comments("sample.ecpp")
