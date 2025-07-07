import re

text = input()

# Replace all whitespace characters (space, tab, newline, etc.) with "_"
result = re.sub(r'\s+', '_', text)

print(result)
