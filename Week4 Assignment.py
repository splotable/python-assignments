def read_and_modify_file():
    # Ask the user for the file name
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as file:
            contents = file.read()

        # Example modification: convert all text to uppercase
        modified_contents = contents.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_contents)

        print(f"File processed successfully! Modified version saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()

