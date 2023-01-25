import re

# Function to remove quotes and attach 4 to text
def remove_quotes(text):
    # Use regular expression to match quotes
    text = re.sub(r'\"(.*?)\"', r'\1', text) + '4'
    return text

# Input text
text = 'allen carl "deals"'

# Remove quotes and attach 4
output = remove_quotes(text)


# Write output to file
with open('output.txt', 'w') as f:
    f.write(output)

