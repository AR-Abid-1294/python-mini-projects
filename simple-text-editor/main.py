def readFile(filename):
    with open(filename, "r") as file:
            for lineNo, line in enumerate(file, start=1):
                 print(f"{lineNo}   {line}", end="")

def editContent(filename, editMode):
     print("Enter your text (type 'SAVE' on a new line to save and exit.):")
     with open(filename, editMode) as file:
          while True:
               newContent = input()
               if newContent == 'SAVE':
                    return
               file.write(newContent + "\n")

def searchText(filename):
     text = input("Enter the text you want to search for: ")

     with open(filename, "r") as file:
          for lineNo, line in enumerate(file, start=1):
                if text in line:
                    print(f'"{text}" found in line no. {lineNo}')
                    
def replaceText(filename):
    old_text = input("Text to be replaced: ")
    new_text = input("Text to replace with: ")

    with open(filename, "r") as file:
        content = file.read()
        
    new_content = content.replace(old_text, new_text)

    with open(filename, "w") as file:
         file.write(new_content)

    print(f'All "{old_text}" replaced by "{new_text}"')

instructions = '''
"A" to add new content
"W" to overwrite
"S" to search for a text
"R" to reaplace a text
"N" to do nothing
'''

while True:
    filename = input("Enter the filename to open or create: ")

    if filename == "EXIT":
        break

    try:
        readFile(filename)
        command = input(instructions).upper()
        if command == "A":      editContent(filename, "a")
        elif command == "W":
             confirm = input("This will overwrite the file. Continue? (y/n): ").lower()
             if confirm == "y": editContent(filename, "w")
        elif command == "S":    searchText(filename)
        elif command == "R":    replaceText(filename)
        elif command == "N":    pass
        elif command == "EXIT": break
        else:
             print("Invalid Input")

    except FileNotFoundError:
        print(f"{filename} not found. Creating a new file.")
        editContent(filename, "w")