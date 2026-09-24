# A. Regular Expression Expressions
# These are the symbols/patterns used to create a regular expression.
# 1. \d — Find digits
import re
text = "My age is 20"
x = re.findall(r"\d", text)
print(x)
# Output:
# ['2', '0']
# Explanation:
# \d matches any digit from 0 to 9. findall() finds all the digits present in the string.
# \D is used to find except digit

# 2. \w — Find letters, digits and underscore
import re
text = "Python_123"
x = re.findall(r"\w", text)
print(x)
# Output:
# ['P', 'y', 't', 'h', 'o', 'n', '_', '1', '2', '3']
# Explanation:
# \w matches letters, numbers and underscore _. It finds each matching character in the string.
# \W is used to match except letterdigits and underscore.

# 3. + — One or more occurrences
import re
text = "I have 123 apples"
x = re.findall(r"\d+", text)
print(x)
# Output:
# ['123']
# Explanation:
# \d finds digits, while + means one or more digits together. Therefore, 123 is treated as one match.

# 4. ^ — Starts with
import re
text = "Python is easy"
if re.search(r"^Python", text):
    print("String starts with Python")
else:
    print("Not found")
# Output:
# String starts with Python
# Explanation:
# ^ checks whether the string starts with the specified pattern. Here, the string starts with Python.


# B. Regular Expression Functions
# These are the functions provided by Python's re module.
# 1. re.search()
import re
text = "I love Python"
x = re.search("Python", text)
if x:
    print("Found")
else:
    print("Not Found")
# Output:
# Found
# Explanation:
# re.search() searches for a pattern anywhere in the string. It returns a match if the pattern is found.

# 2. re.match()
import re
text = "Python is easy"
x = re.match("Python", text)
if x:
    print("Matched")
else:
    print("Not Matched")
# Output:
# Matched
# Explanation:
# re.match() checks the pattern only at the beginning of the string. Here, the string starts with Python.

# 3. re.findall()
import re
text = "cat dog cat rat"
x = re.findall("cat", text)
print(x)
# Output:
# ['cat', 'cat']
# Explanation:
# re.findall() finds all occurrences of a pattern in the string. Here, cat occurs two times.

# 4. re.sub()
import re
text = "I like Java"
x = re.sub("Java", "Python", text)
print(x)
# Output:
# I like Python

# Take input ffrom user for email,password with capital,small,digit,special symbols and no with regular expression
import re

email = input("Enter email: ")
mobile = input("Enter mobile number: ")
password = input("Enter password: ")

# Email
if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
    print("Valid email")
else:
    print("Invalid email")

# Mobile number
if re.fullmatch(r"[0-9]{10}", mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")

# Password
if re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&*!]).{8,}", password):
    print("Valid password")
else:
    print("Invalid password")
# # explanation:
# [A-Za-z0-9._%+-] → Allows uppercase letters, lowercase letters, digits, and symbols such as ., _, %, +, -.
# + → Means one or more of the characters before @.
# @ → Requires the @ symbol.
# [A-Za-z0-9.-] → Allows letters, digits, dot and hyphen in the domain name.
# + → Requires one or more domain characters.
# \. → Matches an actual dot .. The \ is used because . has a special meaning in regex.
# [A-Za-z] → Allows letters after the dot.
# {2,} → Requires at least 2 letters, such as com, in, org
# 2. Mobile Number Regular Expression
# r"[0-9]{10}"

# This expression checks whether the mobile number contains exactly 10 digits.

# [0-9] → Allows any digit from 0 to 9.
# {10} → Requires exactly 10 digits
# 3. Password Regular Expression
# r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&*!]).{8,}"

# This expression checks that the password contains at least one capital letter,
#  one small letter, one digit, one special character, and at least 8 characters