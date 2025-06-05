import os

def modify_file_content(input_filename, output_filename):
    """
    Reads content from input_filename, modifies it (converts to uppercase),
    and writes the modified content to output_filename.

    Includes error handling for FileNotFoundError and other IOErrors.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write to.
    """
    input_content = ""
    # --- Step 1: Read from the input file with error handling ---
    try:
        # Open the input file in read mode ('r')
        with open(input_filename, 'r', encoding='utf-8') as file:
            input_content = file.read()
        print(f"Successfully read content from '{input_filename}'.")

    except FileNotFoundError:
        # Handle the case where the input file does not exist
        print(f"Error: The input file '{input_filename}' was not found. "
              "Please make sure the file exists and the path is correct.")
        return # Exit the function if the file is not found
    except IOError as e:
        # Handle other potential I/O errors during reading (e.g., permission issues)
        print(f"Error reading file '{input_filename}': {e}")
        return # Exit the function if an I/O error occurs

    # --- Step 2: Modify the content ---
    # For this example, we'll convert all text to uppercase.
    modified_content = input_content.upper()
    print("Content modified (converted to uppercase).")

    # --- Step 3: Write to the output file with error handling ---
    try:
        # Open the output file in write mode ('w').
        # If the file doesn't exist, it will be created. If it exists, its content will be overwritten.
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        print(f"Successfully wrote modified content to '{output_filename}'.")
        print("Operation completed.")
    except IOError as e:
        # Handle potential I/O errors during writing (e.g., disk full, permission issues)
        print(f"Error writing to file '{output_filename}': {e}")

if __name__ == "__main__":
    # Get filename from user
    input_file = input("Enter the name of the input file (e.g., my_document.txt): ")
    output_file = input("Enter the name for the new output file (e.g., modified_document.txt): ")

    # Call the function to perform the file operations
    modify_file_content(input_file, output_file)

    # Optional: Verify content of output file if it was created successfully
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                print(f"\n--- Content of '{output_file}' ---")
                print(f.read())
                print("---------------------------------")
        except IOError as e:
            print(f"Could not read the newly created output file for verification: {e}")
