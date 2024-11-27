import os

# Getting the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Changing the current working directory
os.chdir('/path/to/directory')  # Replace with your directory path
print("Directory changed to:", os.getcwd())

# Listing all files and directories in the specified path
files_and_dirs = os.listdir('/path/to/directory')  # Replace with your directory path
print("Files and directories:", files_and_dirs)

# Creating a new directory
os.mkdir('/path/to/new_directory')  # Replace with your directory path
print("New directory created")

# Creating intermediate directories
os.makedirs('/path/to/parent_directory/new_directory', exist_ok=True)
print("Intermediate directories created")

# Removing a directory
os.rmdir('/path/to/directory')  # This will remove an empty directory
print("Directory removed")

# Removing directories and their contents
import shutil
shutil.rmtree('/path/to/directory')  # Removes a directory and all its contents
print("Directory and its contents removed")

# Checking if a path is a file or directory
print("Is a file?", os.path.isfile('/path/to/file'))
print("Is a directory?", os.path.isdir('/path/to/directory'))

# Checking if a file or directory exists
print("Does the path exist?", os.path.exists('/path/to/file_or_directory'))

# Getting file size
file_size = os.path.getsize('/path/to/file')
print("File size:", file_size, "bytes")

# Getting the absolute path
absolute_path = os.path.abspath('file_or_directory')
print("Absolute path:", absolute_path)

# Renaming a file or directory
os.rename('/path/to/old_name', '/path/to/new_name')
print("File or directory renamed")

# Copying a file
import shutil
shutil.copy('/path/to/source_file', '/path/to/destination_file')
print("File copied")

# Moving a file
shutil.move('/path/to/source_file', '/path/to/destination_file')
print("File moved")

# Removing a file
os.remove('/path/to/file')
print("File removed")

# Checking file permissions
print("Is the file readable?", os.access('/path/to/file', os.R_OK))
print("Is the file writable?", os.access('/path/to/file', os.W_OK))
print("Is the file executable?", os.access('/path/to/file', os.X_OK))

# Changing file permissions
os.chmod('/path/to/file', 0o644)  # Read and write for owner, read for others

# Getting the file status
file_stat = os.stat('/path/to/file')
print("File status:", file_stat)

# Creating a temporary file
import tempfile
temp_file = tempfile.NamedTemporaryFile(delete=False)
print("Temporary file created:", temp_file.name)
temp_file.close()  # Close the file handle

# Removing the temporary file
os.remove(temp_file.name)
print("Temporary file removed")
