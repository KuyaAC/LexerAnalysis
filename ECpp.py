import re

import nltk

file = open("sample.ecpp")

#Open file
input_program=file.read()
#input_program = input("Enter Your Code: ");
input_program_tokens = nltk.wordpunct_tokenize(input_program);

#OUTPUT
print(input_program_tokens);
print("Lexemes --> Tokens")


# TOKENS

RE_Keywords = "const|display|do|else|for|if|long|read|short|switch|void|while"
RE_Reserved_Words = "case|define|private|public|return|static|terminal"
#Arithmetic_Operators
RE_Modulus_Op = "(%)"
RE_Increment_Op = "(++)"
RE_Decrement_Op = "(--)"
RE_Equal = "(=)"
RE_Add = "(\++)"
RE_Subtract = "(-)"
RE_Divide = "(/)"
RE_Multiply = "(\*)"
#Boolean_Operators
RE_AND_Op = "(&&)"
RE_OR_Op = "(||)"
RE_NOT_Op = "(!)"  
RE_LESSTHAN = "(<)"
RE_GREATERTHAN = "(>)"
RE_LESSTHAN_EQUAL = "(<=)"
RE_GREATERTHAN_EQUAL = "(>=)"
RE_Equal_To = "(==)"
RE_Not_Equal_To = "(!=)"
RE_Equal_Value_Same_Type = "(===)"
RE_Not_Equal_Value_Same_Type = "(!==)"
#ETC
RE_SemiColon = "(;)"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "([a-zA-Z]+\.[h])"
RE_Integer = "int"
RE_Float = "float"
RE_Character = "char"
RE_Double= "double"
RE_String= "string"



#To Categorize The Tokens

for token in input_program_tokens:
    if(re.findall(RE_Keywords,token)):
        print(token , "-------> Keyword")
    elif(re.findall(RE_Reserved_Words,token)):
        print(token , "-------> Reserved_Words")
#arithmetic
    elif(re.findall(RE_Modulus_Op,token)):
        print(token , "-------> Modulus_Operator")
    elif(re.findall(RE_Increment_Op,token)):
        print(token , "-------> Incrementation")
    elif(re.findall(RE_Decrement_Op,token)):
        print(token , "-------> Decrementation")
    elif(re.findall(RE_Add,token)):
        print(token, "-------> Add_Operator")
    elif(re.findall(RE_Subtract,token)):
        print(token, "-------> Subtract_Operator")
    elif(re.findall(RE_Divide,token)):
        print(token, "-------> Division_Operator")
    elif(re.findall(RE_Multiply,token)):
        print(token, "-------> Multiplication_Operator")
#boolean        
    elif(re.findall(RE_Equal,token)):
        print(token , "-------> Equal_sign")
    elif(re.findall(RE_SemiColon,token)):
        print(token , "-------> Semi-colon")
    elif(re.findall(RE_Numerals,token)):
        print(token, "-------> Number")
    elif(re.findall(RE_Special_Characters,token)):
        print(token, "-------> Special Character/Symbol")
    elif(re.findall(RE_Integer,token)):
        print(token, "-------> Integer")
    elif(re.findall(RE_Float,token)):
        print(token, "-------> Float")
    elif(re.findall(RE_Character,token)):
        print(token, "-------> Character")
    elif(re.findall(RE_Double,token)):
        print(token, "-------> Double")
    elif(re.findall(RE_String,token)):
        print(token, "-------> String")
    elif(re.findall(RE_Identifiers,token)):
        print(token, "-------> Identifiers")
    else:
        print("Unknown Value")

