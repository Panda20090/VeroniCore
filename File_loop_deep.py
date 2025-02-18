import os


def extract_code_from_files(root_dir, output_file):
    with open(output_file, 'w') as out_file:
        for subdir, _, files in os.walk(root_dir):
            for file in files:
                # Skip .md and .txt files
                if file.endswith('.md') or file.endswith('.txt'):
                    continue

                file_path = os.path.join(subdir, file)
                with open(file_path, 'r') as code_file:
                    code_content = code_file.read()

                # Write the script name and code to the output file
                out_file.write(f"# {file}\n\n")
                out_file.write(f"# {code_content}\n")
                out_file.write("_____________________\n\n")


if __name__ == "__main__":
    # Define the root directory and output file
    root_directory = "VeroniCore"
    output_file_path = os.path.join(
        root_directory, "docs", "File_loop_deep.txt")

    # Run the extraction
    extract_code_from_files(root_directory, output_file_path)
