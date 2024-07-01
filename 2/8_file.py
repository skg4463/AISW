with open('files/8_sample.txt', 'w') as file:
    file.write("This is a sample file.")

with open('files/8_sample.txt', 'r') as file:
    content = file.read()
    print(content)  # This is a sample file.
