import nltk
from nltk.tokenize import WordPunctTokenizer

def lexical_analyzer(text):
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(text)
    for token in tokens:
        try:
            int(token)
            print(token, "int")
        except ValueError:
            try:
                float(token)
                print(token, "float")
            except ValueError:
                if token[0] == "'" and token[-1] == "'":
                    print(token, "character")
                elif token[0] == '"' and token[-1] == '"':
                    print(token, "string")
                else:
                    print(token, "unknown")

text = "This is a string, 12.5 is a float, 12 is an int and 'c' is a character"
lexical_analyzer(text)






