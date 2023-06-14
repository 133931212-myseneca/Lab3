def write_text_file_with_name(name):
    filename = "output.txt"
    with open(filename, "w") as file:
        file.write("My name is: " + name)
    print("Text file '{}' created successfully!".format(filename))

# Example usage:
name = input("Enter your name: ")
write_text_file_with_name(name)

