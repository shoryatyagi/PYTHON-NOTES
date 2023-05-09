<html>
<body>
<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID_HERE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
</body>
</html>

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

- #### `.` (dot): Matches any single character except newline.
```bash 
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = r".x"  # matches any character followed by "x"

match = re.search(pattern, string)
print(match.group())  # "fox"
```
- #### `^` (caret): Matches the beginning of a string.
```bash
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = r"^The"  # matches the string that starts with "The"

match = re.search(pattern, string)
print(match.group())  # "The"

```
- #### `$` (dollar): Matches the end of a string.
```bash 
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = r"dog$"  # matches the string that ends with "dog"

match = re.search(pattern, string)
print(match.group())  # "dog"
```
- #### `*` (asterisk): Matches zero or more occurrences of the preceding character.
```bash
import re

string = "abcccdeeeef"
pattern = r"c*"  # matches zero or more "c"s

match = re.search(pattern, string)
print(match.group())  # "c" (matches the first occurrence of zero "c"s)

```
- #### `+` (plus): Matches one or more occurrences of the preceding character.
```bash
import re

string = "abcccdeeeef"
pattern = r"c+"  # matches one or more "c"s

match = re.search(pattern, string)
print(match.group())  # "ccc" (matches the first occurrence of one or more "c"s)
```
- #### `?` (question mark): Matches zero or one occurrences of the preceding character.
```bash
import re

string = "abcccdeeeef"
pattern = r"c?"  # matches zero or one "c"s

match = re.search(pattern, string)
print(match.group())  # "" (matches the first occurrence of zero "c"s)
```
## 🌟 Special Sequences
Here are some of the most commonly used special sequences in regular expressions:

- `\d`: matches any decimal digit (0-9).
- `\D`: matches any character that is not a decimal digit.
- `\w`: matches any alphanumeric character (a-z, A-Z, 0-9, _).
- `\W`: matches any character that is not alphanumeric.
- `\s`: matches any whitespace character (space, tab, newline, etc.).
- `\S`: matches any non-whitespace character.
- `\b`: matches the boundary between a word and a non-word character.
- `\B`: matches any position that is not a word boundary.

## 📝 Conclusion
The re module in Python is a powerful tool for working with regular expressions. Whether you need to search for patterns in a string, replace text, or extract information, re has you covered. With the methods and flags provided by re, you can easily manipulate text and create powerful data processing pipelines in Python.






