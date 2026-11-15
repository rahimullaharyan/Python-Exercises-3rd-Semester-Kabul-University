class DocumentReadError(Exception):
    pass


filename = input("Enter the filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except UnicodeDecodeError:
    print("Error: Unable to decode the file as UTF-8.")

except OSError as e:
    raise DocumentReadError("Unable to read the document.") from e

else:
    print("\nFile content:")
    print(content)

finally:
    print("\nFile reading attempt completed.")