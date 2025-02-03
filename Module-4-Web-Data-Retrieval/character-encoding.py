
## Unicode is a universal system that includes many different character sets. 

## UTF-8 is a way of encoding Unicode characters into bytes (numbers). 

## UTF-8 uses the characters from the Unicode standard and encodes them into bytes that computers can store or send


# Encoding a string into bytes
print("Encoding a string into bytes:")
text = "hello"
encoded_text = text.encode('utf-8')  # This turns the string into bytes
print(encoded_text)  # Output: b'hello'

print("-----------------")

# Decoding bytes back into a string
print("Decoding bytes back into a string:")
decoded_text = encoded_text.decode('utf-8')  # This converts the bytes back into a string
print(decoded_text)  # Output: hello

print("-----------------")

# Display Unicode code points
print("Display Unicode code points:")
text = "hello"
for char in text:
    print(f"Character: {char}, Unicode Code Point: {ord(char)}")

