# 🐍 Python's re module
The re module in Python provides support for regular expressions. Regular expressions are a powerful tool for matching and manipulating text. With re, you can search for patterns in strings, replace text, and extract information from text.

## 📚 Module Methods
Here are the methods provided by the re module:

- #### re.compile(pattern, flags=0): Compiles a regular expression pattern into a regular expression object, which can be used for matching operations.
```bash
import re

pattern = re.compile(r"hello")
match = pattern.search("hello world")
print(match.group())  # "hello"
```

- #### re.search(pattern, string, flags=0): Searches the given string for the first occurrence of the regular expression pattern, returning a match object if found, or None otherwise.
```bash
import re

match = re.search(r"world", "hello world")
print(match.group())  # "world"
```
- #### re.match(pattern, string, flags=0): Matches the regular expression pattern at the beginning of the string, returning a match object if found, or None otherwise.

```bash
import re

match = re.match(r"hello", "hello world")
print(match.group())  # "hello"
```
- #### re.fullmatch(pattern, string, flags=0): Matches the entire string against the regular expression pattern, returning a match object if the entire string matches the pattern, or None otherwise.
```bash
import re

match = re.fullmatch(r"hello world", "hello world")
print(match.group())  # "hello world"
```
- #### re.split(pattern, string, maxsplit=0, flags=0): Splits the string at occurrences of the regular expression pattern, returning a list of substrings.
```bash
import re

string = "hello world"
substrings = re.split(r"\s", string)
print(substrings)  # ["hello", "world"]

```
- #### re.finditer(pattern, string, flags=0): Returns an iterator yielding match objects for all non-overlapping occurrences of the regular expression pattern in the string.

```bash 
import re

string = "hello world"
matches = re.finditer(r"l", string)
for match in matches:
    print(match.group())  # "l" "l"
```
- #### re.findall(pattern, string, flags=0): Finds all occurrences of the regular expression pattern in the string, returning a list of all matches.
```bash 
import re

string = "hello world"
matches = re.findall(r"l", string)
print(matches)  # ["l", "l"]

```

## 🧬 Meta Characters
Here are some of the most commonly used meta characters in regular expressions: