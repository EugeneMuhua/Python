# file_read_write_with_error_handling.py

def read_modify_and_write():
    filename = input("Enter the filename you want to read: ")

    try:
        # Read file
        with open(filename, 'r') as f:
            content = f.read()

        # Modify content (example: uppercase)
        modified_content = content.upper()

        # Create a new filename for the modified version
        output_file = f"modified_{filename}"

        # Write to new file
        with open(output_file, 'w') as f:
            f.write(modified_content)

        print(f"\n✅ Successfully created '{output_file}' with modified content.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read/write '{filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    read_modify_and_write()
