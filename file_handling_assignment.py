# file_handling_assignment.py

# File Creation
try:
    with open('my_file.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a text file.\n")
        file.write("Here is a number: 12345\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error creating file: {e}")
finally:
    print("File creation attempt finished.")


# File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error reading file: {e}")
finally:
    print("File reading attempt finished.")


# File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write("Appending new line 1.\n")
        file.write("Appending new line 2.\n")
        file.write("Appending new line 3.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error appending to file: {e}")
finally:
    print("File appending attempt finished.")



# file_handling_assignment.py

def main():
    # File Creation
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is a text file.\n")
            file.write("Here is a number: 12345\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error creating file: {e}")
    finally:
        print("File creation attempt finished.")

    # File Reading and Display
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading file: {e}")
    finally:
        print("File reading attempt finished.")

    # File Appending
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending new line 1.\n")
            file.write("Appending new line 2.\n")
            file.write("Appending new line 3.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("File appending attempt finished.")

if __name__ == "__main__":
    main()
