import os


def save_directory_structure(root_dir, output_file):
    with open(output_file, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            f.write(f'Directory: {dirpath}\n')
            for dirname in dirnames:
                f.write(f'\tSub-directory: {dirname}\n')
            for filename in filenames:
                f.write(f'\tFile: {filename}\n')
            f.write('\n')  # Add an extra line for better readability


if __name__ == "__main__":
    # Root directory to start the loop
    root_directory = "Automation_frame"

    # Output file path
    output_path = os.path.join(root_directory, "Docs", "File_loop.txt")

    # Ensure the Docs directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the directory structure to the output file
    save_directory_structure(root_directory, output_path)

    print(f"Directory structure saved to {output_path}")
