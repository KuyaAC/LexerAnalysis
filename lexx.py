import re

import os
import nltk
from nltk.tokenize import word_tokenize

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



#import sys

#Restrict File INput
while True:
    file_name1 = input("Enter the file name: ")
    if file_name1.endswith('.ecpp'):
        print("File name accepted.\n")
        break
    else:
        print("The file you've enter is invalid. \nPlease enter a file that has .ecpp at the end.\n")

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
            elif line.startswith("//"):
                # Do nothing, ignore the line
                pass
            else:
                # Write the original line to the output file
                output.write(line)
# input_file = "DEV.ecpp"
# output_file = "DEV2.ecpp"
# string

with open("DEV.ecpp", "r") as input_file:
    # read the contents of the file
    contents = input_file.read()

# use regex to find all quoted text
matches = re.findall(r'"([^"]*)"', contents)

# replace the quoted text with the unquoted text + "4"
for match in matches:
    contents = contents.replace('"' + match + '"', match + "4")
    

# open the output file
with open("DEV2.ecpp", "w") as output_file:
    # write the modified contents to the output file
    output_file.write(contents)





#Open file
file_name = "DEV2.ecpp"
file = open(file_name)
input_program=file.read()

#input_program = input("Enter Your Code: ");
input_program_tokens = nltk.wordpunct_tokenize(input_program);


#OUTPUT
#print("From File:",file)
#print("From File:",file)
print("The Symbol Table has been generated. \nPlease check the file.")

# TOKENS
#NoiseWords
RE_Nint = "integer"
RE_Nchar = "character"
RE_Nconst = "constant"
RE_Nbool = "boolean"
RE_string = "^[a-zA-Z_]+[4]"
#func
RE_checkf = "check"
RE_decf = "sort_dec"
RE_Keywords = "int|float|char|string|double|const|display|do|else|for|if|long|read|short|switch|void|while"
RE_Reserved_Words = "case|define|private|public|return|static|terminate"
RE_Newline = "newline|endl"
RE_Newtab = "newtab"
#Arithmetic_Operators
RE_Modulus_Op = "(%)"
RE_Increment_Op = "(\++)+[+]"
RE_Decrement_Op = "(-)+[-]"
RE_Add = "(\++)"
RE_Subtract = "(-)"
RE_Divide = "(/)"
RE_Multiply = "(\*)"
#c operator
RE_ins = "(<)+[<]"
RE_ext = "(>)+[>]"
#Boolean_Operators
RE_AND_Op = "(&)+[&]"
RE_OR_Op = "(\|)+(\|)"
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
RE_Float = "[0-9]" + "." + "[0-9]"
RE_C_Numerals = "^[(\d+)]+[c]"
RE_Numerals = "^[\d+]"
RE_Special_Characters = "[\&~!\^\:?,\.']"
#RE_NewSpecial_Char = "([\]+[n]|[\]+[t])"
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "([a-zA-Z]+\.[h])"

#bracket and delimiters

RE_OpenP = "[(]"
RE_CloseP = "[)]"
RE_OpenCB = "[{]"
RE_CloseCB = "[}]"
RE_OpenB = "[[]"
RE_CloseB = "[]]"




#To Categorize The Tokens

with open(Outputt, "w") as f:
    f.write("From File: " + file_to_read + "\n")
    f.write("Here is the Output of EC++ Lexical Analyzer:\n")
    f.write("%-40s %s"%("\nLexemes",  " Tokens\n"))
    for token in input_program_tokens:
            if(re.findall(RE_Nint,token)):
                token = token[-4:]
                f.write("%-40s %s"%( token , "Noisewords\n"))
            elif(re.findall(RE_Nchar,token)):
                token = token[-5:]
                f.write("%-40s %s"%( token , "Noisewords\n"))
            elif(re.findall(RE_Nconst,token)):
                token = token[-3:]
                f.write("%-40s %s"%( token , "Noisewords\n"))
            elif(re.findall(RE_Nbool,token)):
                token = token[-3:]
                f.write("%-40s %s"%( token , "Noisewords\n"))
            elif(re.findall(RE_Keywords,token)):
                f.write("%-40s %s"%(token , "Keyword\n"))
            elif(re.findall(RE_string,token)):
                token = token[:-1]
                f.write("%-40s %s"%(token , "String_literal\n"))
            elif(re.findall(RE_checkf,token)):
                f.write("%-40s %s"%( token , "Check Function\n"))
            elif(re.findall(RE_decf,token)):
                f.write("%-40s %s"%( token , "Descending Function\n"))   
            elif(re.findall(RE_ins,token)):
                f.write("%-40s %s"%( token , "Insertion Operator\n"))
            elif(re.findall(RE_ext,token)):
                f.write("%-40s %s"%( token , "Extraction Operator\n"))
            elif(re.findall(RE_Reserved_Words,token)):
                f.write("%-40s %s"%( token , "Reserved_Word\n"))
            elif(re.findall(RE_Newline,token)):
                f.write("%-40s %s"%( token , "New_line\n"))
            elif(re.findall(RE_Newtab,token)):
                f.write("%-40s %s"%( token , "New_tab\n"))
#arithmetic
            elif(re.findall(RE_Modulus_Op,token)):
                f.write("%-40s %s"%( token , "Modulus_ArOperator\n"))
            elif(re.findall(RE_Increment_Op,token)):
                f.write("%-40s %s"%( token , "Increment_ArOperator\n"))
            elif(re.findall(RE_Decrement_Op,token)):
                f.write("%-40s %s"%( token , "Decrement_ArOperator\n"))
            elif(re.findall(RE_Add,token)):
                f.write("%-40s %s"%( token , "Addition_ArOperator\n"))
            elif(re.findall(RE_Subtract,token)):
                f.write("%-40s %s"%( token , "Subtraction_ArOperator\n"))
            elif(re.findall(RE_Divide,token)):
                f.write("%-40s %s"%( token , "Division_ArOperator\n"))
            elif(re.findall(RE_Multiply,token)):
                f.write("%-40s %s"%( token , "Multiplication_ArOperator\n"))
#boolean      
            elif(re.findall(RE_OR_Op,token)):
                f.write("%-40s %s"%( token , "Or_BoolRelOperator\n"))
            elif(re.findall(RE_AND_Op,token)):
                f.write("%-40s %s"%( token , "And_BoolRelOperator\n"))
            elif(re.findall(RE_Equal_Value_Same_Type,token)):
                f.write("%-40s %s"%( token , "Equal_Value_Same_Type\n"))
            elif(re.findall(RE_Not_Equal_To,token)):
                f.write("%-40s %s"%( token , "Not_Equalto_BoolOperator\n"))
            elif(re.findall(RE_NOT_Op,token)):
                f.write("%-40s %s"%( token , "Not_BoolOperator\n"))
            elif(re.findall(RE_LESSTHAN_EQUAL,token)):
                f.write("%-40s %s"%( token , "LessThanOrEqualTo_BoolOperator\n"))
            elif(re.findall(RE_GREATERTHAN_EQUAL,token)):
                f.write("%-40s %s"%( token , "GreaterThanOrEqualTo_BoolOperator\n"))
            elif(re.findall(RE_LESSTHAN,token)):
                f.write("%-40s %s"%( token , "LessThan_BoolOperator\n"))
            elif(re.findall(RE_GREATERTHAN,token)):
                f.write("%-40s %s"%( token , "GreaterThan_BoolOperator\n"))
            elif(re.findall(RE_Equal_To,token)):
                f.write("%-40s %s"%( token , "EqualTo_BoolOperator\n"))
            elif(re.findall(RE_Equal,token)):
                f.write("%-40s %s"%( token , "SimpleAssignment_ArOperator\n"))
#ETC
            elif(re.findall(RE_SemiColon,token)):
                f.write("%-40s %s"%( token , "Semi-colon\n"))
            elif(re.findall(RE_Float,token)):
                f.write("%-40s %s"%( token , "Float_literal\n"))
            elif(re.findall(RE_C_Numerals,token)):
                token = token[:-1]
                f.write("%-40s %s"%( token , "Constant_Number\n"))
            elif(re.findall(RE_Numerals,token)):
                f.write("%-40s %s"%( token , "Int_literals\n"))
            elif(re.findall(RE_Special_Characters,token)):
                f.write("%-40s %s"%( token , "Special Character\n"))
            elif(re.findall(RE_Identifiers,token)):
                f.write("%-40s %s"%( token , "Identifier\n"))
#bracket 
            elif(re.findall(RE_OpenP,token)):
                f.write("%-40s %s"%( token , "Open_Parenthesis\n"))
            elif(re.findall(RE_CloseP,token)):
                f.write("%-40s %s"%( token , "Close_Parenthesis\n"))
            elif(re.findall(RE_OpenCB,token)):
                f.write("%-40s %s"%( token , "Open_CurlyB\n"))
            elif(re.findall(RE_CloseCB,token)):
                f.write("%-40s %s"%( token , "Close_CurlyB\n"))
            elif(re.findall(RE_OpenB,token)):
                f.write("%-40s %s"%( token , "Open_Bracket\n"))
            elif(re.findall(RE_CloseB,token)):
                f.write("%-40s %s"%( token , "Close_Bracket\n"))
#invalid 
            else:
                f.write("%-40s %s"%( token , "Invalid Token\n"))



#comment
def print_line_numbers():
        file = open(file_name1)
        lines = file.readlines()
    # Iterate through each line
        for i, line in enumerate(lines):
        # Check if the line starts with #
                if line.startswith("//"):
            # Print the line number and the line
                    with open(Outputt, "a") as f:
                        
                        s = str(line)
                        s.replace(" ","")
                        f.write(f"\nComment in Line {i+1}: {line}")

print_line_numbers()

