import re

import nltk

import sys

#Restrict

while True:
    file_name = input("Enter the file name: ")
    if file_name.endswith('.ecpp'):
        print("\nFile name accepted.")
        break
    else:
        print("Invalid file name. \nPlease enter a file name ending in .ecpp")

#Open file
file = open(file_name)
input_program=file.read()
#input_program = input("Enter Your Code: ");
input_program_tokens = nltk.wordpunct_tokenize(input_program);


#OUTPUT
#print("From File:",file)
print("\n", input_program_tokens);
print("\n[Lexemes : Tokens]")


# TOKENS
RE_Keywords = "const|display|do|else|for|if|long|read|short|switch|void|while"
RE_Reserved_Words = "case|define|private|public|return|static|terminal"
#Arithmetic_Operators
RE_Modulus_Op = "(%)"
#RE_Increment_Op = "++"
#RE_Decrement_Op = "--"
RE_Add = "(\++)"
RE_Subtract = "(-)"
RE_Divide = "(/)"
RE_Multiply = "(\*)"
#Boolean_Operators
RE_AND_Op = "(&&)"
#RE_OR_Op = "||"
RE_Not_Equal_To = "(!=)"
RE_NOT_Op = "(!)"  
RE_LESSTHAN_EQUAL = "<="
RE_GREATERTHAN_EQUAL = ">="
RE_LESSTHAN = "(<)"
RE_GREATERTHAN = "(>)"
RE_Equal_To = "(==)"
RE_Equal = "(=)"
#RE_Equal_Value_Same_Type = "(===)"
#RE_Not_Equal_Value_Same_Type = "(!==)"
#ETC
RE_SemiColon = "(;)"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!$\^\|{}\]:<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "([a-zA-Z]+\.[h])"
RE_Integer = "int"
RE_Float = "float"
RE_Character = "char"
RE_Double= "double"
RE_String= "string"
#RE_Comments = "#"
#bracket and delimiters
#RE_Open_Brackets = "("
#RE_Closing_Brackets = ")"
#RE_Delimiter = "|"




#To Categorize The Tokens
for token in input_program_tokens:
    if(re.findall(RE_Keywords,token)):
        print("[", token , ": Keyword]")
    #elif(re.findall(RE_Comments,token)):
    elif(re.findall(RE_Reserved_Words,token)):
        print("[",token , ": Reserved_Words]")
#arithmetic
    elif(re.findall(RE_Modulus_Op,token)):
        print("[",token , ": Modulus_Operator]")
    #elif(re.findall(RE_Increment_Op,token)):
        #print("[",token , ": Incrementation]")
    #elif(re.findall(RE_Decrement_Op,token)):
        #print("[",token , ": Decrementation]")
    elif(re.findall(RE_Add,token)):
        print("[",token, ": Add_Operator]")
    elif(re.findall(RE_Subtract,token)):
        print("[",token, ": Subtract_Operator]")
    elif(re.findall(RE_Divide,token)):
        print("[",token, ": Division_Operator]")
    elif(re.findall(RE_Multiply,token)):
        print("[",token, ": Multiplication_Operator]")
#boolean        
    elif(re.findall(RE_AND_Op,token)):
        print("[",token , ": And]")
    #elif(re.findall(RE_OR_Op,token)):
        #print("[",token , ": OR]")
    elif(re.findall(RE_NOT_Op,token)):
        print("[",token , ": NOT]")
    elif(re.findall(RE_LESSTHAN,token)):
        print("[",token , ": LessThan]")
    elif(re.findall(RE_GREATERTHAN,token)):
        print("[",token , ": Greaterthan]")
    elif(re.findall(RE_LESSTHAN_EQUAL,token)):
        print("[",token , ": Lessthan_Equal]")
    elif(re.findall(RE_GREATERTHAN_EQUAL,token)):
        print("[",token , ": Greaterthan_Equal]")
    elif(re.findall(RE_Equal_To,token)):
        print("[",token , ": Equal_To]")
    #elif(re.findall(RE_Equal_Value_Same_Type,token)):
        #print("[",token , ": Equal_Value_Same_Type]")
    #elif(re.findall(RE_Not_Equal_Value_Same_Type,token)):
        #print("[",token , ": Not_Equal_Value_Same_Type]")
#ETC
    elif(re.findall(RE_Equal,token)):
        print("[",token , ": Equal_sign]")
    elif(re.findall(RE_SemiColon,token)):
        print("[",token , ": Semi-colon]")
    elif(re.findall(RE_Numerals,token)):
        print("[",token, ": Number]")
    elif(re.findall(RE_Special_Characters,token)):
        print("[",token, ": Special Character/Symbol]")
    elif(re.findall(RE_Integer,token)):
        print("[",token, ": Integer]")
    elif(re.findall(RE_Float,token)):
        print("[",token, ": Float]")
    elif(re.findall(RE_Character,token)):
        print("[",token, ": Character]")
    elif(re.findall(RE_Double,token)):
        print("[",token, ": Double]")
    elif(re.findall(RE_String,token)):
        print("[",token, ": String]")
    elif(re.findall(RE_Identifiers,token)):
        print("[",token, ": Identifiers]")
#bracket and delimiters
    #elif(re.findall(RE_Open_Brackets,token)):
        #print("[",token, ": Open_Brackets]")
   # elif(re.findall(RE_Closing_Brackets,token)):
        #print("[",token, ": Closing_Brackets]")
    #elif(re.findall(RE_Delimiter,token)):
        #print("[",token, ": Delimiter]")
    else:
        print("Unknown Value")



#comment
    def print_line_numbers():
        file = open(file_name)
        lines = file.readlines()

    # Iterate through each line
        for i, line in enumerate(lines):
        # Check if the line starts with #
                if line.startswith("#"):
            # Print the line number and the line
                    print(f"\nComment in Line {i+1}: {line}")

print_line_numbers()