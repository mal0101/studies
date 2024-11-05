import os
import shutil
import re

def move_file(src, dst):
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"File moved from {src} to {dst}")
    else:
        print(f"Source file {src} does not exist")

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def create_file(filename):
    with open(filename, 'w') as file:
        pass
    print(f"File {filename} created")

def add_lines_to_file(filename, lines):
    with open(filename, 'a') as file:
        file.writelines(lines)
    print(f"Lines added to {filename}")

def display_file_content(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    else:
        print(f"File {filename} does not exist")

def display_file_properties(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            num_lines = content.count('\n') + 1
            num_words = count_words(content)
            num_chars = len(content)
            file_size = os.path.getsize(filename)
            print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}, Size: {file_size} bytes")
    else:
        print(f"File {filename} does not exist")

def main():
    while True:
        print("\nMenu:")
        print("1. Move file")
        print("2. Count words in text")
        print("3. Create file")
        print("4. Add lines to file")
        print("5. Display file content")
        print("6. Display file properties")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            src = input("Enter source file path: ")
            dst = input("Enter destination file path: ")
            move_file(src, dst)
        elif choice == '2':
            text = input("Enter text: ")
            print(f"Number of words: {count_words(text)}")
        elif choice == '3':
            filename = input("Enter file name: ")
            create_file(filename)
        elif choice == '4':
            filename = input("Enter file name: ")
            lines = []
            print("Enter lines (type 'done' to finish):")
            while True:
                line = input()
                if line.lower() == 'done':
                    break
                lines.append(line + '\n')
            add_lines_to_file(filename, lines)
        elif choice == '5':
            filename = input("Enter file name: ")
            display_file_content(filename)
        elif choice == '6':
            filename = input("Enter file name: ")
            display_file_properties(filename)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 