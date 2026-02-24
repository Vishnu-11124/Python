
full_name = "John Doe"
print(full_name)

multiline_string = """ This is a
    multiline
 code"""

print(multiline_string)

# ------------------------------------------------------

# Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("New user:",full_name)

# ------------------------------------------------------

# String length

course = "JavaScript"
print(len(course))

# ------------------------------------------------------

# Substring
text = "Python for beginners"
print("Substring:", text[0:6])

# ------------------------------------------------------

# Formatting string
first_name = "John"
last_name = "Doe"
message = f"{first_name} {last_name} is a coder"
print(message)

# ------------------------------------------------------

# Escape character
escaped_string = "hey, \n Where are you going?"
print(escaped_string)

# ------------------------------------------------------

# upper() and lower()
text = "Hello, World!"
print(text.upper())
print(text.lower())

# ------------------------------------------------------

# capitalize() and title()
text = "hello, world!"
print(text.capitalize())
print(text.title())

# ------------------------------------------------------

# strip(), lstrip() and rstrip()
text = "   Hello, World!   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# ------------------------------------------------------

# startwith() and endswith()
text = "Hello, World!"
print(text.startswith("Hello"))
print(text.endswith("World!"))

# ------------------------------------------------------

# replace(old, new)
text = "Hello, World!"
print(text.replace("World", "Python"))

# ------------------------------------------------------

# find() and index()
text = "Hello, World!"
print(text.find("World"))
print(text.index("World"))

# ------------------------------------------------------

# split()
text = "Hello, World!"
print(text.split(","))

# ------------------------------------------------------

# count()
text = "Hello, World!"
print(text.count("l"))

# ------------------------------------------------------

