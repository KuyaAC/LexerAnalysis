import re

import os
import nltk

#import sys

#Restrict File INput
while True:
    file_name1 = input("Enter the file name: ")
    if file_name1.endswith('.ecpp'):
        print("File name accepted.\n")
        break
    else:
        print("The file you've enter is invalid. \nPlease enter a file that has .ecpp at the end.")

#Restrict File INput

#try

# File to read
file_to_read = file_name1

# File to write
file_to_write = "DEV.ecpp"
#output file
Outputt = "Symbol Table.txt"

# Coms and Cons
with open(file_to_read, "r") as file:
    # Open the output file for writing
    with open(file_to_write, "w") as output:
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


#Open file
file_name = file_to_write
file = open(file_name)
input_program=file.read()

#input_program = input("Enter Your Code: ");
input_program_tokens = nltk.wordpunct_tokenize(input_program);


#OUTPUT
#print("From File:",file)
#print("From File:",file)
print("The symbol table has been generated. \nPlease check the file.")


# TOKENS
RE_Keywords = "int|float|char|string|double|const|display|do|else|for|if|long|read|short|switch|void|while"
RE_Reserved_Words = "case|define|private|public|return|static|terminal"
#Arithmetic_Operators
RE_Modulus_Op = "(%)"
RE_Increment_Op = "(\++)+[+]"
RE_Decrement_Op = "(-)+[-]"
RE_Add = "(\++)"
RE_Subtract = "(-)"
RE_Divide = "(/)"
RE_Multiply = "(\*)"
#Boolean_Operators
RE_AND_Op = "(&&)"
#RE_OR_Op = "||"
RE_Not_Equal_To = "(!=)"
RE_NOT_Op = "(!)"  
RE_LESSTHAN_EQUAL = "(<)+[=]"
RE_GREATERTHAN_EQUAL = "(>)+[=]"
RE_LESSTHAN = "(<)"
RE_GREATERTHAN = "(>)"
RE_Equal_To = "(==)"
RE_Equal_Value_Same_Type = "(==)+[=]"
RE_Equal = "(=)"
#RE_Not_Equal_Value_Same_Type = "(!==)"
#ETC
RE_SemiColon = "(;)"
RE_C_Numerals = "^[(\d+)$]+[c]"
RE_Numerals = "^[(\d+)]"
RE_Special_Characters = "[\&~!\^\:?,\.']"
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "([a-zA-Z]+\.[h])"

#bracket and delimiters
RE_Brackets = "[\[\|{}\],]|\(\)\(\)|{}|\[\]|\""





#To Categorize The Tokens

with open(Outputt, "w") as f:
    f.write("From File: " + file_to_read + "\n")
    f.write("Here is the Output of EC++ Lexical Analyzer:\n")
    f.write("\n[Lexemes : Tokens]")
    for token in input_program_tokens:
            if(re.findall(RE_Keywords,token)):
                f.write("\n["+ token + ": Keyword]")
            elif(re.findall(RE_Reserved_Words,token)):
                f.write("\n[" + token + ": Reserved_Words]")
#arithmetic
            elif(re.findall(RE_Modulus_Op,token)):
                f.write("\n["+ token + ": Modulus_Operator]")
            elif(re.findall(RE_Increment_Op,token)):
                f.write("\n["+ token + ": Incrementation_Operator]")
            elif(re.findall(RE_Decrement_Op,token)):
                f.write("\n["+ token + ": Decrementation_Operator]")
            elif(re.findall(RE_Add,token)):
                f.write("\n["+ token + ": Addition_Operator]")
            elif(re.findall(RE_Subtract,token)):
                f.write("\n["+ token + ": Subtraction_Operator]")
            elif(re.findall(RE_Divide,token)):
                f.write("\n["+ token + ": Division_Operator]")
            elif(re.findall(RE_Multiply,token)):
                f.write("\n["+ token + ": Multiplication_Operator]")
#boolean        
            elif(re.findall(RE_AND_Op,token)):
                f.write("\n["+ token + ": And]")
    #elif(re.findall(RE_OR_Op,token)):
        #print("[",token , ": OR]")
            elif(re.findall(RE_NOT_Op,token)):
                f.write("\n["+ token + ": NOT]")
            elif(re.findall(RE_LESSTHAN,token)):
                f.write("\n["+ token + ": LessThan]")
            elif(re.findall(RE_GREATERTHAN,token)):
                f.write("\n["+ token + ": Greaterthan]")
            elif(re.findall(RE_LESSTHAN_EQUAL,token)):
                f.write("\n["+ token + ": Lessthan_Equal]")
            elif(re.findall(RE_GREATERTHAN_EQUAL,token)):
                f.write("\n["+ token + ": Greaterthan_Equal]")
            elif(re.findall(RE_Equal_To,token)):
                f.write("\n["+ token + ": Equal_To]")
            elif(re.findall(RE_Equal_Value_Same_Type,token)):
                f.write("\n["+ token + ": Equal_Value_Same_Type]")
    #elif(re.findall(RE_Not_Equal_Value_Same_Type,token)):
        #print("[",token , ": Not_Equal_Value_Same_Type]")
#ETC
            elif(re.findall(RE_Equal,token)):
                f.write("\n["+ token + ": Equal_sign]")
            elif(re.findall(RE_SemiColon,token)):
                f.write("\n["+ token + ": Semi-colon]")
            elif(re.findall(RE_C_Numerals,token)):
                token = token[:-1]
                f.write("\n["+ token + ": Constant_Number]")
            elif(re.findall(RE_Numerals,token)):
                f.write("\n["+ token + ": Number]")
            elif(re.findall(RE_Special_Characters,token)):
                f.write("\n["+ token + ": Special Character]")
            elif(re.findall(RE_Identifiers,token)):
                f.write("\n["+ token + ": Identifiers]")
#bracket and delimiters
            elif(re.findall(RE_Brackets,token)):
                f.write("\n["+ token + ": Brackets/Delimiter]")
            else:
                f.write("\nUnknown Value")



#comment
def print_line_numbers():
        file = open(file_name1)
        lines = file.readlines()

    # Iterate through each line
        for i, line in enumerate(lines):
        # Check if the line starts with #
                if line.startswith("#"):
            # Print the line number and the line
                    with open(Outputt, "a") as f:
                        f.write("\n")
                        f.write(f"Comment in Line {i+1}: {line}")

print_line_numbers()

