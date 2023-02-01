#module part
import re
import os

#Import file codings
while True:
    file_name1 = input("Enter the file name: ")
    if file_name1.endswith('.ecpp'):
        print("File name accepted.\n")
        break
    else:
        print("The file you've enter is invalid. \nPlease enter a file that has .ecpp at the end.\n")

#Defining Constant part
CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]

#Defining Tokens part
TOKENS = [
    'KEY_WORD', 'IDENTIFIER', 'INTEGER_CONSTANT',
    'OPERATOR', 'SEPARATOR', 'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'DATATYPE' , 'BOOL_CONST']

#Open File dat end in ECPP
with open(file_name1, "r") as input_file:
    contents = input_file.read()
blank_var = contents
print("INPUT FILE:\n",blank_var)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


integers = re.findall('^[0-9]+$|[0-9]+', blank_var)
floatn = re.findall(r'[0-9]+\.[0-9]+', blank_var)
chars = re.findall(r'\'[^\'\\\.]\'', blank_var)

TOKENS_DEF = {
    '=': 'ASSIGN',
    '&': 'ADDRESS',
    '<': 'LT',
    '>': 'GT',
    '++': 'SELF_PLUS',
    '--': 'SELF_MINUS',
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MUL',
    '/': 'DIV',
    '>=': 'GET',
    '<=': 'LET',
    '(': 'LL_BRACKET',
    ')': 'RL_BRACKET',
    '{': 'LB_BRACKET',
    '}': 'RB_BRACKET',
    '[': 'LM_BRACKET',
    ']': 'RM_BRACKET',
    ',': 'COMMA',
    '"': 'DOUBLE_QUOTE',
    '\'': 'SINGLE_QUOTE',
    ';': 'SEMICOLON',
    '#': 'SHARP',
    '&&': 'AND',
    '!': 'NOT',
    '||': 'OR',
    '<<': 'L_SHIFT',
    '>>': 'R_SHIFT',
    '==':'EQUALITY',
    ':':'COLON'
    
}

Keyword = ["if", "else", "while", "for", "display", "read", "return", "switch", "case", "terminate", "function",
           "define", "using", "namespace", "include", "endl","default"]
bracket = ['(', ')', '{', '}', '[', ']']
datatype = ['int', 'float', 'char', 'string', 'bool','void']
punctuator = [',', ';', ':', ',']
arithop = ['-', '+', '*', '/', '%']
logop = ['||', '&&']
slogop = ['!']
assop = ['=']
sinlop = ['<', '>']
relop = ['<=', '>=', '!=', '==', "<<", ">>"]
incr = ['++', '--']
bool_cons = ['True','False']


class Node:

    # Function to initialise the node object
    def __init__(self, value, line_numbers, type):
        self.data = {
            "LINE_NUMBERS": line_numbers,
            "value": value,
            "TYPE": type
        }  # Assign data
        self.next = None  # Initialize next as null

# Node of a doubly linked list
class Symbol_table_Node:
    def __init__(self, name, line_numbers, type,scope):
        self.data = {
            "Name": name,
            "LINE_NUMBERS": line_numbers,
            "TYPE": type,
            "Scope": scope
        }  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None
class SymbolTable:
    def __init__(self):
        self.head = None
    def push(self, name, line_numbers, type,scope):
            new_node = Symbol_table_Node(name, line_numbers, type,scope)


            new_node.next = self.head
            new_node.prev = None


            if self.head is not None:
                self.head.prev = new_node


            self.head = new_node

    def printList(self):
        node = self.head
        while (node != None):

            print(node.data)
            last = node
            node = node.next

    def FindData(self, name):
        flag = False
        node = self.head

        while (node != None):

            if (node.data['Name'] == name):
                return node.data
            last = node
            node = node.next
        if (flag == False):
            return False


class Tokkens:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function is defined in Linked List class
    # Appends a new node at the end. This method is
    # defined inside LinkedList class shown above */
    def append(self, value, line_numbers, type):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(value, line_numbers, type)

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data),
            temp = temp.next

class Token(object):

    def __init__(self, pos, value, linenumber):
        self.type = TOKENS_DEF[value] if (
                pos == 3 or pos == 4
        ) else TOKENS[pos]
        self.value = value
        self.line_number = linenumber

class Lexer(object):

    def __init__(self):
        self.tokens = []
        self.count = 1
        self.temp = ''
        self.sym = SymbolTable()

    def is_blank(self, index):
        return (
                blank_var[index] == ' '
        )

    def is_Escape(self, index):
        return (

                blank_var[index] == '\t' or
                blank_var[index] == '\n' or
                blank_var[index] == '\r'
        )

    def line_break(self, index):
        return (
                blank_var[index] == '\n' or
                blank_var[index] == '\t' or
                blank_var[index] == '\b' or
                blank_var[index] == ' '

        )

    def skip_blank(self, index, stringflag):
        while index < len(blank_var) and self.is_blank(index):
            index += 1
        return index

    def print_log(self, style, value):
        print(style, value)

    def checkforiden(self):
        if (self.temp != ''):

            i = re.findall('[a-zA-Z_][a-zA-Z_0-9]*', self.temp)

            if (self.temp in i):

                self.tokens.append(Token(1, self.temp, self.count))


                self.sym.push(self.temp, self.count, "NOT DEFINED", "NOT DEFINED")
                self.temp = ''


                # symbol table code








            else:
               print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
               exit()
                # error handler
            self.temp = ''
        else:
            return 0;

    def is_keyword(self, value):
        for item in Keyword:
            if value in item:
                return True
        return False

    def main(self):
        i = 0
        strf = False

        while i < len(blank_var):

            if (blank_var[i] == ' '):
                self.checkforiden()
                i = i + 1
                continue
            if blank_var[i] == '\n':
                self.checkforiden()
                self.count = self.count + 1
                i = i + 1
                continue
            if blank_var[i] == '#':
                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i], self.count))
                i = i + 1
                continue
            elif blank_var[i:i + 2] in logop:
                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i:i + 2], self.count))
                i = i + 1
            elif blank_var[i:i + 2] in relop:
                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i:i + 2], self.count))
                i = i + 1
            elif blank_var[i:i + 2] in incr:
                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i:i + 2], self.count))
                i = i + 1
            elif blank_var[i] in bracket:
                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i], self.count))

            elif blank_var[i] in punctuator:

                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i], self.count))

            elif blank_var[i] in sinlop:
                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i], self.count))

            elif blank_var[i] in assop:

                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i], self.count))

            elif blank_var[i] in slogop:
                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i], self.count))
            elif blank_var[i] in arithop:
                self.checkforiden()
                self.tokens.append(Token(3, blank_var[i], self.count))
            else:
                self.temp = self.temp + blank_var[i]

                if (blank_var[i] == '"'):
                    #self.tokens.append(Token(3, blank_var[i], self.count))
                    if (self.temp == '"'):
                        self.temp = ''
                        i = i + 1
                        strf = True
                        while i < len(blank_var) and blank_var[i] != '"':

                            if (blank_var[i:i + 2] == "\\t"):
                                self.temp = self.temp + '\t'
                                i = i + 2
                            elif (blank_var[i:i + 2] == "\\n"):

                                self.temp = self.temp + '\n'
                                i = i + 2
                            else:
                                self.temp = self.temp + blank_var[i]
                                i = i + 1

                            if (i == len(blank_var) or i > len(blank_var)):
                                print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
                                exit()

                        if (len(self.temp) > 0):
                            self.tokens.append(Token(5, self.temp, self.count))
                            strf = False
                            self.temp = ''
                        #self.tokens.append(Token(3, blank_var[i], self.count))
                        i = i + 1
                        continue

                if (self.temp in integers):

                    if (blank_var[i + 1] != '.' and blank_var[i+1] not in re.findall('[0-9]',blank_var)):

                        j = re.findall('[a-zA-Z_][a-zA-Z_0-9]*', blank_var[i + 1]);

                        if (blank_var[i + 1] not in j):

                            self.tokens.append(Token(2, self.temp, self.count))
                            integers.pop(integers.index(self.temp))
                            
                            self.temp = ''


                elif (self.temp in Keyword):
                    self.tokens.append(Token(0, self.temp, self.count))
                    self.temp = ''



                elif (self.temp in datatype):
                    self.tokens.append(Token(8, self.temp, self.count))
                    self.temp = ''

                elif (self.temp in bool_cons):
                	self.tokens.append(Token(9,self.temp,self.count))
                	self.temp=''
                elif (self.temp in floatn):
                    self.tokens.append(Token(6, self.temp, self.count))
                    self.temp = ''

                if (blank_var[i] == '\''):
                    #self.tokens.append(Token(3, blank_var[i], self.count))
                    self.temp = ''
                    i = i + 1

                    if (blank_var[i] == '\''):
                        #self.tokens.append(Token(3, blank_var[i], self.count))
                        self.temp = ''
                        i = i + 1
                        continue
                    elif (blank_var[i:i + 2] == '\\n' or blank_var[i:i + 2] == '\\t' or ord(blank_var[i])):
                        if (blank_var[i:i + 2] == '\\n' or blank_var[i:i + 2 == '\\t']):
                            if (blank_var[i + 2] == '\''):
                                self.tokens.append(Token(7, blank_var[i:i + 2], self.count))
                                self.temp = ''
                                i = i + 2
                                #self.tokens.append(Token(3, blank_var[i], self.count))
                                i = i + 1
                                continue
                            else:
                                print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
                                exit()
                        else:

                            if (blank_var[i + 1] == '\''):
                                self.tokens.append(Token(7, blank_var[i], self.count))
                                self.temp = ''
                                i = i + 1
                                #self.tokens.append(Token(3, blank_var[i], self.count))
                                #i = i + 1
                            else:
                                print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
                                exit()

                    else:
                        print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
                        exit()

            i = i + 1
            continue


class parser:

    def __init__(self,tok):
        self.tok=tok.head
        self.lookahead=None

    def nextToken(self):
        if(self.lookahead==None):
            return self.tok
        else:
            self.tok=self.tok.next
            return self.tok

    def includestmt(self):
        data = self.lookahead.data['value'];
        if (data == '#'):
            self.match("#")
            self.match("include")
            self.match("<")
            self.matchID(self.lookahead.data['TYPE'])
            self.match('>')
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def includelist_(self):
        data = self.lookahead.data['value'];
        if (data == '#'):
            self.includestmt()
            self.includelist_()
        elif(data in ['$',"using"]):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()


    def includelist(self):
        data = self.lookahead.data['value'];
        if (data == '#'):
            self.includestmt()
            self.includelist_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def namespace(self):
        data = self.lookahead.data['value'];
        if(data == 'using'):
            self.match('using')
            self.match('namespace')
            self.matchID(self.lookahead.data["TYPE"])
            self.match(';')
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def start(self):
        data = self.lookahead.data['value'];
        if(data == '#'):
            self.includelist()
            self.namespace()
            self.program()
        elif(data == "$"):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()



    def vardeclist_(self):
        data = self.lookahead.data['value'];
        if (data == ','):
            self.match(',')
            self.vardecinit()
            self.vardeclist_()
        elif (data == ';'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def vardecid(self):
        data = self.lookahead.data['value']

        if ( self.lookahead.data["TYPE"]=="IDENTIFIER"):
            self.matchID(self.lookahead.data["TYPE"])
            self.vardecid_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def vardecid_(self):
        data = self.lookahead.data['value'];

        if ( data == '['):
            self.match('[')
            if(self.lookahead.data['TYPE']=='INTEGER_CONSTANT'):
                self.lookahead = self.nextToken()
                self.match(']')
            else:
                print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
                exit()
        elif ( data == ',' or data == ';' or data == '='):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def relop(self):
        data = self.lookahead.data['value'];

        if( data == '<='):
            self.match('<=')
        elif ( data == '<'):
            self.match('<')
        elif ( data == '>'):
            self.match('>')
        elif ( data == '>='):
            self.match('>=')
        elif (data == '=='):
            self.match('==')
        elif ( data == '!='):
            self.match('!=')
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()


    def expression(self):
        data = self.lookahead.data['value'];

        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        data_next = self.lookahead.next
        if (self.lookahead.data["TYPE"] == "IDENTIFIER" and data_next.data["value"] == "++"):
        	self.matchID(self.lookahead.data["TYPE"])
        	self.match("++")
        	
        elif(self.lookahead.data["TYPE"] == "IDENTIFIER" and data_next.data["value"] == "--"):
        	self.matchID(self.lookahead.data["TYPE"])
        	self.match("--")
        elif(self.lookahead.data["TYPE"] == "IDENTIFIER" and data_next.data["value"] == "="):
        	self.matchID(self.lookahead.data["TYPE"])
        	self.match("=")
        	self.expression()
        elif (data == '!' or self.lookahead.data['TYPE'] == 'IDENTIFIER'or data == '(' or self.lookahead.data['TYPE'] in CONST):
            self.simpleExp()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()


    def arglist_(self):
        data = self.lookahead.data['value'];
        if(data == ','):
            self.match(',')
            self.expression()
            self.arglist_()
        elif (data ==')'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def arglist(self):
        data = self.lookahead.data['value'];
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if (data == '!' or self.lookahead.data['TYPE'] == 'IDENTIFIER' or data == '(' or self.lookahead.data['TYPE'] in CONST):
            self.expression()
            self.arglist_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def args(self):
        data = self.lookahead.data['value'];

        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if (data == '!' or self.lookahead.data['TYPE'] == 'IDENTIFIER' or data == '(' or self.lookahead.data['TYPE'] in CONST):
            self.arglist()
        elif ( data == ')'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def constants(self):
        data = self.lookahead.data['value']
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if(self.lookahead.data['TYPE'] in CONST):
            self.lookahead=self.nextToken()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def factor_(self):
        data = self.lookahead.data['value']

        if(data == '('):
            self.match('(')
            self.args()
            self.match(')')
        elif ( data == '*' or data == '/' or data == '%' or data == '+' or data == '-' or data == '<=' or data == '<' or data == '>' or data == '>=' or data == '==' or data == '!=' or data == '&&' or data=="||" or data == ',' or data == ';' or data == ')' or data == "<<"):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def factor(self):
        data = self.lookahead.data['value'];
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if (self.lookahead.data['TYPE'] == 'IDENTIFIER'):
            self.matchID(self.lookahead.data['TYPE'])
            self.factor_()
        elif (data == '('):
            self.match('(')
            self.expression()
            self.match(')')
        elif (self.lookahead.data['TYPE'] in CONST):
            self.constants()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()



    def unaryExp(self):
        data = self.lookahead.data['value'];
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if (self.lookahead.data['TYPE'] == 'IDENTIFIER' or data == '(' or self.lookahead.data['TYPE'] in CONST):
            self.factor()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def mulOp(self):
        data = self.lookahead.data['value']
        if (data =='*'):
            self.match('*')
        elif (data=='/'):
            self.match('/')
        elif (data=='%'):
            self.match('%')
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def mulExp_(self):
        data = self.lookahead.data['value']
        
        if ( data == '*' or data == '/' or data == '%'):
            self.mulOp()
            self.unaryExp()
            self.mulExp_()
        elif ( data == '+' or data == '-' or data == '<=' or data == '<' or data == '>' or data == '>=' or data == '==' or data == '!=' or data == '&&' or data=="||" or data == ',' or data == ';' or data == ')' or data=="<<"):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def sumOP(self):
        data = self.lookahead.data['value']
        if( data == '+'):
            self.match('+')
        elif( data == '-'):
            self.match('-')
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def sumExp_(self):
        data = self.lookahead.data['value'];
        if (data == '+' or data == '-'):
            self.sumOP()
            self.mulExp()
            self.sumExp_()
        elif (data == '<=' or data == '<' or data == '>' or data == '>=' or data == '==' or data == '!=' or data == '&&' or data=="||" or data == ',' or data == ';' or data == ')' or data=="<<"):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def mulExp(self):
        data = self.lookahead.data['value'];
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if (self.lookahead.data['TYPE'] == 'IDENTIFIER' or data == '(' or self.lookahead.data['TYPE'] in CONST):
            self.unaryExp()
            self.mulExp_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def sumExp(self):
        data = self.lookahead.data['value'];
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if (self.lookahead.data['TYPE'] == 'IDENTIFIER' or data == '(' or self.lookahead.data['TYPE'] in CONST):
            self.mulExp()
            self.sumExp_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def relExp_(self):
        data = self.lookahead.data['value'];
        if (data == '<=' or data == '<' or data == '>' or data == '>=' or data == '==' or data == '!='):
            self.relop()
            self.sumExp()
            self.relExp_()
        elif (data == '||' or data == '&&' or data ==',' or data == ';' or data == ')' or data=="<<"):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def relExp(self):
        data = self.lookahead.data['value'];
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if (self.lookahead.data['TYPE'] == 'IDENTIFIER' or data == '(' or self.lookahead.data['TYPE'] in CONST):
            self.sumExp()
            self.relExp_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def unaryRelExp(self):
        data = self.lookahead.data['value'];
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if (data == '!'):
            self.match('!')
            self.unaryRelExp()
        elif (self.lookahead.data['TYPE'] == 'IDENTIFIER' or data == '(' or self.lookahead.data['TYPE'] in CONST ):
            self.relExp()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()


    def andExp_(self):
        data = self.lookahead.data['value'];
        if( data == '&&'):
            self.match("&&")
            self.unaryRelExp()
            self.andExp_()
        elif (data == '||' or data == ',' or data == ';' or data == ')' or data == "<<"):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def andExp(self):
        data = self.lookahead.data['value'];
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if (data == '!' or self.lookahead.data['TYPE'] == 'IDENTIFIER' or data == '(' or self.lookahead.data['TYPE'] in CONST):
            self.unaryRelExp()
            self.andExp_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def SimpleExp_(self):
        data = self.lookahead.data['value'];
        if ( data == '||'):
            self.match('||')
            self.andExp()
            self.SimpleExp_()
        elif (data == ',' or data == ';' or data == ')' or data == "<<"):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def simpleExp(self):
        data = self.lookahead.data['value'];
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if(data == '!' or self.lookahead.data['TYPE'] == 'IDENTIFIER' or  data == '(' or self.lookahead.data['TYPE'] in CONST):
            self.andExp()
            self.SimpleExp_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()


    def vardecinit_(self):
        data = self.lookahead.data['value'];

        if(data == '='):
            self.match('=')
            self.simpleExp()
        elif(data == ',' or data == ';' ):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def vardecinit(self):
        data = self.lookahead.data['value'];

        if (self.lookahead.data["TYPE"] == "IDENTIFIER"):
            self.vardecid()
            self.vardecinit_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def vardeclist(self):
        data = self.lookahead.data['value'];

        if (self.lookahead.data["TYPE"] == "IDENTIFIER"):
            self.vardecinit()
            self.vardeclist_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def varriable(self):
        data = self.lookahead.data['value'];

        if(self.lookahead.data["TYPE"] == "IDENTIFIER"):
            self.vardeclist()
            self.match(';')
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def declaration__(self):
        data = self.lookahead.data['value'];
        data_next = self.lookahead.next
        if (self.lookahead.data['TYPE'] == "IDENTIFIER" and data_next.data['value'] == '('):
            self.function()
        elif (self.lookahead.data['TYPE'] == "IDENTIFIER"):
            self.varriable()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def declaration(self):
        data = self.lookahead.data['value'];

        if (data in datatype):
            self.typeid()
            self.declaration__()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def declaration_(self):
        data = self.lookahead.data['value'];

        if (data in datatype):
            self.declaration()
            self.declaration_()
        elif (data == '$'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def declist(self):
        data = self.lookahead.data['value'];

        if (data in datatype):
            self.declaration()
            self.declaration_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def program(self):
        data = self.lookahead.data['value'];

        if ( data in datatype):
            self.declist()
        elif (data == '$'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def function(self):
        data = self.lookahead.data['value'];
        if(self.lookahead.data['TYPE'] == 'IDENTIFIER'):
            self.matchID(self.lookahead.data['TYPE'])
            self.match('(')
            self.paramas()
            self.match(')')
            self.match('{')
            self.stmtlist()
            self.match('}')
        elif(data == '$'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def stmtlist(self):
        data = self.lookahead.data['value'];
        
        CONST = [
            'INTEGER_CONSTANT',
            'STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS', 'BOOL_CONST'
        ]
        if(data in ['!','(','if','display','read','while','for','switch','return','terminate'] or data in datatype or self.lookahead.data["TYPE"] in ["IDENTIFIER" , CONST]):
            self.statment()
            self.stmtlist_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def iteration(self):
        data = self.lookahead.data['value'];
        if(data == 'for'):
            self.match('for')
            self.match('(')
            self.vardecinit()
            self.match(';')
            self.simpleExp()
            self.match(';')
            self.expression()
            self.match(')')
            self.match('{')
            self.stmtlist()
            self.match('}')
        elif(data == "while"):
        	self.match("while")
        	self.match("(")
        	self.simpleExp()
        	self.match(")")
        	self.match("{")
        	self.stmtlist()
        	self.match("}")
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def switch(self):
    	data=self.lookahead.data["value"]
    	if(data =="switch"):
    		self.match("switch")
    		self.match("(")
    		self.simpleExp()
    		self.match(")")
    		self.match("{")
    		self.caselist()
    		self.default()
    		self.match("}")
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()

    def caselist(self):
    	data = self.lookahead.data["value"]
    	if(data=="case"):
    		self.onecase()
    		self.caselist()
    	elif(data=="default" or data == "}"):
    		return
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()

    		
    def onecase(self):
    		data = self.lookahead.data["value"]
    		if(data=="case"):
    			self.match("case")
    			if(self.lookahead.data["TYPE"] in CONST):
    				self.lookahead =self.nextToken()
    				self.match(":")
    				self.stmtlist()
    			else:
    				print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()

    		else: 
    		    print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
            

    		
    	 	
    def default(self):
    	data=self.lookahead.data["value"]
    	if(data == "default"):
    		self.match("default")
    		self.match(":")
    		self.stmtlist()
    	elif(data == "}"):
    		return
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
        

    def selection(self):
    	data =self.lookahead.data["value"]
    	if(data == "if"):
    		self.match("if")
    		self.match("(")
    		self.simpleExp()
    		self.match(")")
    		self.match("{")
    		self.stmtlist()
    		self.match("}")
    		self.selection_()
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
        

    def selection_(self):
    	data = self.lookahead.data["value"]
    	if(data == ";"):
    		self.match(";")
    	elif(data =="else"):
    		self.match("else")
    		self.match("{")
    		self.stmtlist()
    		self.match("}")
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
    		exit()
    
    def statment(self):
        data = self.lookahead.data['value'];
        if(data in ['for','while']):
            self.iteration()
        elif(data in ['return']):
            self.returnstmt()
        elif(data in ['if']):
            self.selection()
        elif(data in ['switch']):
            self.switch()
        elif(data in ['terminate']):
            self.match("terminate")
            self.match(";")
        elif(data == "continue"):
        	self.match("continue")
        	self.match(";")
        elif(data in ["read","display"]):
        	self.input_output()
        elif(data in datatype):
            self.declaration()
        elif (data in ['!','('] or self.lookahead.data["TYPE"] in ["IDENTIFIER", CONST]):
            self.expression()
            self.match(";")
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def printlist(self):
    	data= self.lookahead.data["value"]
    	if(data == "<<"):
    		self.single()
    		self.printlist_()
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
        

    def single(self):
    	data=self.lookahead.data["value"]
    	if(data == "<<"):
    		self.match("<<")
    		self.expression()
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
        

    def printlist_(self):
    	data =self.lookahead.data["value"]
    	data_next = self.lookahead.next
    	if(data == "<<" and data_next.data["value"] not in ["endl"]):
    		self.single()
    		self.printlist_()
    	elif(data == "<<" or data == ";" ):
    		return 
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
      

    def endstmt(self):
    	data = self.lookahead.data["value"]
    	if(data == "<<"):
    		self.match("<<")
    		self.match("endl")
    		self.match(";")
    	elif(data == ";"):
    		self.match(";")
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
      

    def input_output(self):
    	data = self.lookahead.data["value"]
    	if(data == "display"):
    		self.match("display")
    		self.printlist()
    		self.endstmt()
    	elif(data == "read"):
    		self.match("read")
    		self.inputlist()
    		self.match(";")
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
      

    def inputlist(self):
    	data = self.lookahead.data["value"]
    	if(data == ">>"):
    		self.singleinput()
    		self.inputlist_()
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
       

    def inputlist_(self):
    	data = self.lookahead.data["value"]
    	if(data==">>"):
    		self.singleinput()
    		self.inputlist_()
    	elif(data == ";"):
    		return;
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()

    def singleinput(self):
    	data=self.lookahead.data["value"]
    	if(data == ">>"):
    		self.match(">>")
    		self.matchID(self.lookahead.data["TYPE"])
    	else:
    		print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n"), exit()
       
    def stmtlist_(self):
        data = self.lookahead.data['value'];

        if (data in ['!', '(','display','read','if', 'while', 'for', 'switch', 'return', 'terminate'] or data in datatype or self.lookahead.data["TYPE"] in ["IDENTIFIER", CONST]):
            self.statment()
            self.stmtlist_()
        elif(data in ['}'] or data == "default"):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def returnstmt(self):
        data = self.lookahead.data['value'];
        if(data == 'return'):
            self.match('return')
            self.expression()
            self.match(';')
        elif(data == '}'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def data(self):
        value = self.lookahead.data['TYPE'];
        data = self.lookahead.data['value'];
        conslist = ['INTEGER_CONSTANT','STRING_CONSTANT', 'FLOAT_CONSTANTS', 'CHAR_CONSTANTS','BOOL_CONST']
        if(value in conslist):
            self.lookahead = self.nextToken()

        elif (data == ';'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def paramas(self):
        data = self.lookahead.data['value'];
        if (data in datatype):
            self.paralist()
        elif (data == ')'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def paralist(self):
        data = self.lookahead.data['value'];
        if(data in datatype):
            self.parameter()
            self.paralist_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def paralist_(self):
        data = self.lookahead.data['value'];
        if(data == ','):
            self.match(',')
            self.parameter()
            self.paralist_()
        elif(data == ')'):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def parameter(self):
        data = self.lookahead.data['value'];
        if( data in datatype):
            self.vartypeid()
            self.paraid()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def paraid(self):
        type = self.lookahead.data['TYPE'];
        if(type == 'IDENTIFIER'):
            self.matchID(type)
            self.paraid_()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def paraid_(self):
        data = self.lookahead.data['value'];
        if(data == '['):
            self.match('[')
            self.match(']')
        elif (data == ')' or data == ','):
            return
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def match(self,t):
        if(self.lookahead.data['value'] == t):
            self.lookahead= self.nextToken()

        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()
    def matchID(self,type):

        if(type=='IDENTIFIER'):
            self.lookahead = self.nextToken()
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def typeid(self):
        data = self.lookahead.data['value'];
        type = self.lookahead.data['TYPE'];
        if(data == 'int'):
            self.match('int')
        elif(data == 'float'):
            self.match('float')
        elif(data == 'string'):
            self.match('string')
        elif(data == 'char'):
            self.match('char')
        elif(data == 'bool'):
            self.match('bool')
        elif (data == 'void'):
            self.match('void')
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()

    def vartypeid(self):
        data = self.lookahead.data['value'];
        type = self.lookahead.data['TYPE'];
        if (data == 'int'):
            self.match('int')
        elif (data == 'float'):
            self.match('float')
        elif (data == 'string'):
            self.match('string')
        elif (data == 'char'):
            self.match('char')
        elif (data == 'bool'):
            self.match('bool')
        else:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Invalid Syntax" , "\nLine no.", self.lookahead.data['LINE_NUMBERS'], "\n")
            exit()


def lexer():
    lexer = Lexer()
    lexer.main()
    tok = Tokkens()
    for token in lexer.tokens:
        tok.append(token.value, token.line_number, token.type)
    tok.append('$', token.line_number + 1, "EOF")
    #tok.printList()
    #print("\nSYMBOL TABLE: \n")
    #lexer.sym.printList()
    #print("\n")
    check = parser(tok)
    check.lookahead = check.nextToken()
    check.start()


    if check.lookahead.data['value']  == '$':
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}Syntactically Correct!\n")



if __name__ == '__main__':
    lexer()