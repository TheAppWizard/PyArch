# Concat
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World

# Indexing and Slicing
my_string = "Python"
print(my_string[0])     # Output: P
print(my_string[2:5])   # Output: tho

# Length
my_string = "Hello World"
print(len(my_string))   # Output: 11

# Lowercase and Uppercase
my_string = "HELLO"
print(my_string.lower())    # Output: hello
print(my_string.upper())    # Output: HELLO

# Splitting
my_string = "Hello World"
print(my_string.split())    # Output: ['Hello', 'World']

# Stripping
my_string = "   Hello   "
print(my_string.strip())    # Output: Hello

# Replace
my_string = "Hello World"
print(my_string.replace("World", "Universe"))   # Output: Hello Universe

# Checking Substrings
my_string = "Hello World"
print("Hello" in my_string)   # Output: True

# Formatting
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 30 years old.

# Joining
my_list = ["Hello", "World"]
print(" ".join(my_list))   # Output: Hello World

