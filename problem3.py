import os

def print_directory_contents(directory):
    try:
        # List all files and directories in the given directory
        entries = os.listdir(directory)
        
        print(f"Contents of directory '{directory}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"You do not have permission to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_directory_path_here' with the path of the directory you want to list
directory_path = '/'
print_directory_contents(directory_path)
